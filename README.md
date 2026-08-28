# solreport — an auto-updating Solana ecosystem report

A self-refreshing report on the state of the Solana network, published in three
formats from one pipeline:

| Output | File | For |
|---|---|---|
| Interactive dashboard | `output/index.html` | humans — dark theme, charts, sortable tables |
| Human-readable report | `output/report.md` | reading in a repo, pasting into a doc |
| Machine-readable data | `output/report.json` | other programs, agents, alerting |

Plus `data/history.jsonl` — an append-only snapshot history that turns single
readings into a time series, and doubles as the baseline for anomaly detection.

**No API keys. No accounts. No third-party packages.** The whole thing is the
Python standard library talking to public endpoints, so it runs on a bare
`python:3-slim` image or a stock GitHub Actions runner with no install step.

```bash
python -m solreport          # that is the entire setup
```

---

## Quick start

Requires Python 3.9+ and nothing else.

```bash
git clone <this repo> && cd solana-ecosystem-report
python -m solreport                       # collect, detect, render
open output/index.html                    # the dashboard (file:// works — it is self-contained)
```

Useful flags:

```bash
python -m solreport --out public --data data     # change output/history directories
python -m solreport --rpc https://your.rpc.node  # use a private RPC instead of public mainnet-beta
python -m solreport --perf-samples 120           # widen the throughput window to ~2 hours
python -m solreport --no-history                 # render without appending a snapshot
python -m solreport --fail-on-critical           # exit 2 on a critical anomaly (for alerting)
python -m unittest discover -s tests             # 18 offline tests, no network needed
```

A run takes about 7 seconds and makes 5 HTTPS requests.

---

## What the report covers

**Network performance** — current/mean/peak TPS and *true* (non-vote) TPS over a
configurable window, mean and worst slot time, epoch number and progress, slot
index, absolute slot, block height, lifetime transaction count, live validator
client version, RPC health, and the projected time remaining in the epoch.

**Validator set** — active vs delinquent counts, delinquent stake in SOL and as a
share of total, total activated stake, commission mean/median, the number of
zero-commission validators, the top validators by stake with their individual
shares, and the delinquent validators ranked by the stake they hold. Stake
concentration is reported as the **Nakamoto coefficient** — the number of
validators that together control a third of stake, which is the threshold at
which the chain stops finalizing. That single integer is more decision-useful
than a list of large validators, and it is the metric the ecosystem argues about.

**Economics** — SOL price, market cap, 24h spot volume and 24h change; DeFi TVL
now with 1d/7d/30d changes, its 90-day peak and full 90-day daily series;
stablecoin supply settled on Solana broken out by peg; DEX volume over 24h/7d/30d
with the top protocols by share; and chain fees plus application revenue, the
public proxy for Real Economic Value. Circulating vs non-circulating supply comes
straight from the chain.

**Trend** — once more than one snapshot exists, the Markdown report gains a
first-snapshot-to-now comparison table and the dashboard gains a cross-snapshot
chart, both drawn from `history.jsonl`.

---

## Data sources and how they are integrated

| Source | Endpoint | Provides | Key |
|---|---|---|---|
| Solana JSON-RPC | `api.mainnet-beta.solana.com` | `getHealth`, `getEpochInfo`, `getRecentPerformanceSamples`, `getSupply`, `getVersion`, `getLatestBlockhash`, `getVoteAccounts` | none |
| CoinGecko | `api.coingecko.com/api/v3/simple/price` | SOL price, market cap, 24h volume and change | none |
| DeFiLlama | `api.llama.fi` | Solana DeFi TVL (90-day series), DEX volume by protocol, chain fees | none |
| DeFiLlama stablecoins | `stablecoins.llama.fi` | stablecoin circulating supply on Solana, by peg | none |
| GitHub REST API | `api.github.com` | open SIMD proposals, Agave validator client releases | none |

Three integration decisions are worth calling out:

**RPC calls are batched.** The six cheap RPC methods go out as a single JSON-RPC
batch — one round trip, not six. That matters on a rate-limited public endpoint,
and it means every number in the network section describes the same moment rather
than six moments a second apart. `getVoteAccounts` is issued separately because it
is heavy (~700 validators) and gets a longer timeout.

**No source can take down the report.** Each collector returns
`{"ok": false, "error": ...}` instead of raising, `build_snapshot` catches
collector bugs on top of that, and the renderers print `n/a` for anything
missing. A DeFiLlama outage costs you the TVL section, not the report — and the
failure itself is surfaced as a `source_down` anomaly rather than silently
appearing as a gap.

**Derived metrics are computed here, not copied.** TPS, true TPS, slot time, the
Nakamoto coefficient, stake shares, epoch ETA and every percentage change are
calculated from raw source data in `sources.py`. Nothing is scraped from another
project's dashboard, so there is no upstream layout change that can break it.

---

## Automation strategy

The report is designed to need zero maintenance, in four layers:

1. **Stateless collection.** A run depends on nothing but the four public
   endpoints. No key to rotate, no account to keep alive, no database to
   provision, no paid tier to outgrow.
2. **Append-only history.** Each run writes one compact JSON line to
   `data/history.jsonl`. The file is the dataset — small enough to live in git,
   so the history travels with the repo and every past report is reproducible.
3. **Scheduled refresh** (`.github/workflows/refresh.yml`). A cron runs every 6
   hours — at `41 1,7,13,19 * * *`, four times a day: it runs the tests,
   regenerates all three outputs, commits the new snapshot back to the repo so
   the time series grows on its own, and publishes `docs/` to GitHub Pages.
   Manual refresh is available from the Actions tab via `workflow_dispatch`.

   The odd minute and odd hour are deliberate, and worth stating because it is
   the one part of "auto-updating" that quietly fails. GitHub's own docs warn
   that the `schedule` event "can be delayed during periods of high load", and a
   dropped run is never retried. Load peaks at the top of every hour and at
   midnight UTC, which is exactly where the obvious `0 */6 * * *` puts you: that
   schedule registered as active here and fired zero times across two
   consecutive windows before it was moved off-peak. Anything relying on
   GitHub cron should assume best-effort delivery and pick an unpopular minute.
4. **Self-monitoring.** `--fail-on-critical` exits 2 when a critical anomaly
   fires, so the same command that generates the report can be the alerting
   check in any cron or monitoring system.

To run it somewhere other than GitHub Actions, the whole job is one cron line:

```cron
41 1,7,13,19 * * * cd /srv/solreport && /usr/bin/python3 -m solreport --out /var/www/solana
```

---

## Anomaly detection

Two detectors, deliberately different, because they fail in different ways.

**Absolute rules** fire on values that are bad regardless of history — delinquent
stake above 2% (warning) or 5% (critical), mean slot time above 0.65s or 0.8s
against a ~0.4s target, a Nakamoto coefficient below 15, TVL moving more than 10%
in a day or 25% in a week, SOL moving more than 10% in 24h, an RPC that reports
itself unhealthy, and any source that failed to answer. These work on the very
first run, when there is no history to compare against — which is exactly when a
purely statistical detector is blind.

**Robust z-scores** fire on values that are unusual *for this chain lately*, over
ten tracked metrics. They use the median and median absolute deviation rather
than mean and standard deviation: a single earlier spike would inflate a
mean-based baseline and mask the next one, whereas the median barely moves.
Rules are directional where direction matters — a *rising* delinquency count is
an anomaly, a falling one is good news, and a *falling* Nakamoto coefficient is
the bad direction. They activate at 8 snapshots and stay quiet before that
rather than reporting noise as signal.

**Materiality gate.** A z-score divides by the spread of the baseline, so after a
quiet stretch the divisor collapses and an ordinary 1% drift scores five sigma.
That is statistically true and editorially useless — a dashboard that shouts
"critical" at normal TPS jitter teaches its reader to ignore it. Every z-finding
therefore has to clear a second, independent gate: the move must also be a
material fraction of the median in its own right (5% for TPS and slot time, 3%
for price, TVL and stablecoin supply, 10% for the Nakamoto coefficient, 15% for
DEX volume, 25% for the small, noisy delinquency counts). Both gates must fire,
so a reported finding is always unusual for this chain *and* big enough to care
about. The percentage move is printed in the finding text so the reader can judge
it directly.

Every finding carries a severity, the observed value, the expected range and a
plain-English sentence, so the identical object renders into the JSON, the
Markdown table and the dashboard without being re-derived three times.

---

## The dashboard

`output/index.html` is one self-contained file. The snapshot is embedded as JSON
and every chart is SVG drawn by about 200 lines of vanilla JavaScript — no CDN,
no build step, no network calls at view time. It therefore opens from `file://`,
from GitHub Pages or from an air-gapped machine, and it will still work in five
years when today's chart library has had four breaking releases.

Interactive: the TVL chart refilters to 7/30/90 days, every table sorts by any
column, and the charts are keyboard- and screen-reader-labelled. Dark theme, and
responsive down to a phone.

---

## Layout

```
solreport/
  http.py         urllib-based HTTP + batching JSON-RPC client, with retries
  sources.py      one collector per data source; none of them raise
  collect.py      orchestration into a versioned snapshot
  store.py        append-only history (summarize / append / load)
  anomaly.py      absolute rules + robust z-scores
  render_md.py    Markdown report (narrative derived from the numbers)
  render_html.py  self-contained interactive dashboard
  cli.py          `python -m solreport`
tests/            18 offline tests — deterministic, no network
.github/workflows/refresh.yml
data/history.jsonl
output/           index.html, report.md, report.json
```

---

## Design notes

**Why no dependencies.** `requests`, `pandas` and a chart library would each save
a few dozen lines and cost the property that makes this maintainable: that it
runs anywhere Python runs, forever, with no lockfile to refresh and no
supply-chain surface. The bounty asked for low maintenance; this is what low
maintenance actually looks like a year later.

**Why the narrative is generated.** The "At a glance" section reads like prose but
every clause is a function of the snapshot. A hand-written summary is accurate on
the day it is written and misleading a week later — the failure mode this report
exists to avoid.

**Why history is a flat JSONL file.** It is diffable, greppable, append-only,
committable, and readable by `pandas`, `jq`, DuckDB or three lines of Python. A
database would need provisioning, backups and credentials to store a few
kilobytes a day.

## Limitations, stated honestly

- Public `api.mainnet-beta.solana.com` is rate-limited and is the right endpoint
  for a report that runs every few hours, not every few seconds. Point `--rpc` at
  a dedicated node for higher frequency.
- `getRecentPerformanceSamples` covers roughly the last hour by default, so TPS
  figures are a recent-window average and not an instantaneous reading.
- CoinGecko's keyless tier is rate-limited; the retry/backoff in `http.py` absorbs
  the occasional 429, and a hard failure degrades to a missing market section
  rather than a failed run.
- Tokenized-equity volumes are not automated. There is no keyless machine-readable
  source for them that would not amount to scraping a page whose layout changes,
  and a number that breaks silently is worse than an absent one.
- Upgrade tracking is automated, but indirectly, and it is worth knowing how. There
  is no roadmap API. What exists is the source of record: every protocol change is
  proposed as a pull request against the Solana Improvement Documents repo and ships
  in a tagged Agave validator release, both readable through the public GitHub API
  with no key. The **Protocol roadmap** section derives from those two feeds, so it
  keeps working with nobody maintaining a list. What it does *not* do is editorialise
  — it will show you SIMD-0612 the day it is opened, but it will not tell you which
  proposal matters most this quarter. Unauthenticated GitHub requests are rate
  limited per IP; a hard failure degrades to a missing roadmap section, as with
  every other source.
