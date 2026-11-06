# Solana Ecosystem Report

_Generated 2026-11-06T12:55:01Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-06T12:55:01Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.38s |
| Snapshots in history | 588 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **1,330 non-vote TPS** (1,330 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **662 active validators** (32 delinquent, holding 0.150% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $90.2** (-5.11% over 24h), market cap $53.26B.
- **DeFi TVL $5.28B** (-1.17% 7d, -19.66% 30d), against $14.47B of stablecoins settled on Solana.
- **$2.20B of DEX volume in 24h** across 141 protocols, generating $9.63M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Mean TPS | 1330.3 | 4.17e+03 tx/s +/- 944 tx/s (median of last 587) | Mean TPS is 1.33e+03 tx/s, 3.0 robust standard deviations below its recent median of 4.17e+03 tx/s (-68.1%). |
| 🟠 warning | Delinquent validators | 32 | 12 +/- 4.448 (median of last 587) | Delinquent validators is 32, 4.5 robust standard deviations above its recent median of 12 (+166.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1078 (97.44% complete) |
| Slot | 420,953 of 432,000 in epoch |
| Absolute slot | 466,116,953 |
| Block height | 444,136,470 |
| Lifetime transactions | 565,506,182,720 |
| TPS (now / mean / peak) | 1,256 / 1,330 / 1,794 |
| True TPS, non-vote (now / mean) | 1,256 / 1,330 |
| Slot time (mean / worst) | 0.214s / 0.221s |

Epoch 1078 has **11,047 slots remaining**, about **39m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 32 (4.61% delinquent) |
| Total stake | 430,872,482 SOL |
| Delinquent stake | 646,460 SOL (0.150%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.96% / 24.74% |
| Commission (mean / median) | 12.84% / 5.0% |
| Zero-commission validators | 224 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,063,613 | 3.960% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,736,546 | 3.884% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,020,024 | 3.022% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,434,901 | 2.422% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,530,733 | 2.212% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,459,109 | 2.195% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,692 | 2.140% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,860,096 | 1.824% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,477 | 1.623% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,293,076 | 1.461% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 234,313 | 462,239,999 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 203,749 | 465,663,873 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 73,365 | 465,263,999 |
| `FH9xcL7Fqkreq1wSkn2Vf7AfnMEyo2KK7QX32LTFndt6` | 69,003 | 466,050,071 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,850 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 131 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $90.2 | -5.11% 24h ↓ |
| Market cap | $53.26B | |
| Spot volume 24h | $3.68B | |
| DeFi TVL | $5.28B | -4.51% 1d / -1.17% 7d / -19.66% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.47B | |
| Stablecoin supply (all pegs) | $14.55B | |
| DEX volume 24h | $2.20B | -7.85% 1d |
| DEX volume 7d / 30d | $12.29B / $57.57B | |
| Fees + app revenue 24h | $9.63M | -14.28% 1d |
| Circulating supply | 590,287,211 SOL (92.66% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $311.46M | 14.17% |
| BisonFi | $231.07M | 10.51% |
| Tessera V | $197.03M | 8.96% |
| PumpSwap | $188.58M | 8.58% |
| Meteora DLMM | $172.58M | 7.85% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-11-06 |
| - | [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) | 2026-11-06 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-11-05 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-05 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-05 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-11-05 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-11-04 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-05 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-06T12:55:01Z | Change |
|---|---|---|---|
| SOL price | $107 | $90 | -16.05% |
| DeFi TVL | $5.94B | $5.28B | -11.16% |
| Stablecoin supply | $15.97B | $14.47B | -9.41% |
| DEX volume 24h | $3.63B | $2.20B | -39.47% |
| Mean TPS | 3,288 | 1,330 | -59.54% |
| Active validators | 689 | 662 | -3.92% |
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
