# Solana Ecosystem Report

_Generated 2026-09-28T23:57:42Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-28T23:57:42Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.83s |
| Snapshots in history | 301 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **1,894 non-vote TPS** (4,403 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.268s**.
- **675 active validators** (7 delinquent, holding 0.005% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $118.84** (-2.69% over 24h), market cap $69.86B.
- **DeFi TVL $6.52B** (+5.01% 7d, +10.78% 30d), against $16.38B of stablecoins settled on Solana.
- **$1.93B of DEX volume in 24h** across 126 protocols, generating $15.42M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | SOL price | 118.84 | $104 +/- $5 (median of last 300) | SOL price is $119, 3.0 robust standard deviations above its recent median of $104 (+14.3%). |
| 🟠 warning | DeFi TVL | 6516842705 | $5,920,008,537 +/- $133,279,998 (median of last 300) | DeFi TVL is $6,516,842,705, 4.5 robust standard deviations above its recent median of $5,920,008,537 (+10.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1045 (7.70% complete) |
| Slot | 33,275 of 432,000 in epoch |
| Absolute slot | 451,473,275 |
| Block height | 429,512,861 |
| Lifetime transactions | 553,842,730,885 |
| TPS (now / mean / peak) | 4,252 / 4,403 / 5,203 |
| True TPS, non-vote (now / mean) | 1,708 / 1,894 |
| Slot time (mean / worst) | 0.268s / 0.282s |

Epoch 1045 has **398,725 slots remaining**, about **29h 40m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 7 (1.03% delinquent) |
| Total stake | 441,249,792 SOL |
| Delinquent stake | 23,511 SOL (0.005%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.45% |
| Commission (mean / median) | 12.52% / 5% |
| Zero-commission validators | 229 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.040% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.796% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.561% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.540% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.731% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.518% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.477% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 451,280,677 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 451,196,568 |
| `DtZGy3AXE8gWVvxUHJTmQqxpmnzmdKsVXwvRN6NFKvUM` | 1 | 451,396,967 |
| `QhyTEHb5JkMBki8Lq1npsaixefUyMXWJtbxK6jNjxnn` | 1 | 451,436,763 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $118.84 | -2.69% 24h ↓ |
| Market cap | $69.86B | |
| Spot volume 24h | $4.13B | |
| DeFi TVL | $6.52B | -1.63% 1d / +5.01% 7d / +10.78% 30d |
| TVL 90-day peak | $6.64B | |
| Stablecoin supply (USD peg) | $16.38B | |
| Stablecoin supply (all pegs) | $16.44B | |
| DEX volume 24h | $1.93B | -10.61% 1d |
| DEX volume 7d / 30d | $18.32B / $76.81B | |
| Fees + app revenue 24h | $15.42M | -14.03% 1d |
| Circulating supply | 587,852,926 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $424.96M | 22.06% |
| PumpSwap | $297.07M | 15.42% |
| Raydium AMM | $271.05M | 14.07% |
| BisonFi | $270.02M | 14.02% |
| Meteora DLMM | $158.26M | 8.22% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-28 |
| SIMD-503 | [SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) | 2026-09-28 |
| SIMD-161 | [Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) | 2026-09-28 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-09-27 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-25 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-25 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | Release v4.4.0-beta.0 | 2026-09-28 |
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |
| [`v4.3.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | Release v4.3.0 | 2026-09-18 |
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-28T23:57:42Z | Change |
|---|---|---|---|
| SOL price | $107 | $119 | +10.61% |
| DeFi TVL | $5.94B | $6.52B | +9.63% |
| Stablecoin supply | $15.97B | $16.38B | +2.55% |
| DEX volume 24h | $3.63B | $1.93B | -46.96% |
| Mean TPS | 3,288 | 4,403 | +33.92% |
| Active validators | 689 | 675 | -2.03% |
| Nakamoto coefficient | 18 | 18 | +0.00% |

## Data sources

| Source | Used for | Key required |
|---|---|---|
| `https://api.mainnet-beta.solana.com` (Solana JSON-RPC) | epoch, slots, TPS, slot time, supply, validator set | no |
| CoinGecko public API | SOL price, market cap, spot volume | no |
| DeFiLlama | DeFi TVL (90d series), DEX volume, chain fees | no |
| DeFiLlama stablecoins | stablecoin supply settled on Solana, by peg | no |
| GitHub public API | open SIMD proposals, Agave validator client releases | no |

Every request is a plain HTTPS GET/POST from `urllib` in the Python standard library. There are no API keys, no accounts and no third-party packages, so the pipeline runs on a bare `python:3-slim` image or a GitHub Actions runner with no setup step.

---

Report and dashboard regenerated automatically by [`solreport`](README.md). Snapshot history: `data/history.jsonl`.
