# Solana Ecosystem Report

_Generated 2026-09-30T10:00:50Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-30T10:00:50Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.42s |
| Snapshots in history | 311 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **1,430 non-vote TPS** (3,935 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **673 active validators** (10 delinquent, holding 0.035% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $119.31** (-0.45% over 24h), market cap $70.15B.
- **DeFi TVL $6.51B** (-0.41% 7d, +12.20% 30d), against $16.11B of stablecoins settled on Solana.
- **$2.66B of DEX volume in 24h** across 127 protocols, generating $14.65M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | SOL price | 119.31 | $104 +/- $5 (median of last 304) | SOL price is $119, 3.1 robust standard deviations above its recent median of $104 (+14.6%). |
| 🟠 warning | DeFi TVL | 6507784322 | $5,924,750,516 +/- $154,473,801 (median of last 310) | DeFi TVL is $6,507,784,322, 3.8 robust standard deviations above its recent median of $5,924,750,516 (+9.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1046 (13.77% complete) |
| Slot | 59,472 of 432,000 in epoch |
| Absolute slot | 451,931,472 |
| Block height | 429,970,848 |
| Lifetime transactions | 554,373,855,630 |
| TPS (now / mean / peak) | 3,997 / 3,935 / 4,548 |
| True TPS, non-vote (now / mean) | 1,538 / 1,430 |
| Slot time (mean / worst) | 0.267s / 0.276s |

Epoch 1046 has **372,528 slots remaining**, about **27h 37m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 10 (1.46% delinquent) |
| Total stake | 440,549,645 SOL |
| Delinquent stake | 153,285 SOL (0.035%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.91% / 24.47% |
| Commission (mean / median) | 12.53% / 5% |
| Zero-commission validators | 230 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,227,376 | 3.910% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,893,945 | 3.608% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,668 | 2.799% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,384,141 | 2.584% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,206,135 | 2.544% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,721 | 2.101% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,232,740 | 2.096% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,652,675 | 1.737% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,092,577 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,513,562 | 1.479% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `NikGQUQqSLtsdHGGx7mQopojZcgd3N9uWFaZQ1r5EXn` | 81,803 | 451,647,060 |
| `ViKLknQuks11DLEjZ7Y2aNYAAT7Q3NTKLGxs8rdnLVi` | 43,391 | 451,647,273 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 451,858,710 |
| `6hcGvZypizjf6PPsxboshZHRqefyQKSG9L8vZqYdm7UY` | 4,580 | 451,830,270 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 451,518,013 |
| `DtZGy3AXE8gWVvxUHJTmQqxpmnzmdKsVXwvRN6NFKvUM` | 1 | 451,881,193 |
| `QhyTEHb5JkMBki8Lq1npsaixefUyMXWJtbxK6jNjxnn` | 1 | 451,436,763 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $119.31 | -0.45% 24h ↓ |
| Market cap | $70.15B | |
| Spot volume 24h | $3.57B | |
| DeFi TVL | $6.51B | +0.80% 1d / -0.41% 7d / +12.20% 30d |
| TVL 90-day peak | $6.64B | |
| Stablecoin supply (USD peg) | $16.11B | |
| Stablecoin supply (all pegs) | $16.18B | |
| DEX volume 24h | $2.66B | -0.05% 1d |
| DEX volume 7d / 30d | $15.81B / $77.24B | |
| Fees + app revenue 24h | $14.65M | -16.34% 1d |
| Circulating supply | 588,005,974 SOL (92.60% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $381.95M | 14.36% |
| Orca DEX | $372.91M | 14.02% |
| PumpSwap | $337.46M | 12.68% |
| Raydium AMM | $279.98M | 10.52% |
| Meteora DLMM | $189.70M | 7.13% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-511 | [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-09-30 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-29 |
| SIMD-630 | [SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-29 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-09-29 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) _(draft)_ | 2026-09-29 |
| SIMD-503 | [SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) | 2026-09-29 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-28 |
| SIMD-161 | [Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) | 2026-09-28 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-30T10:00:50Z | Change |
|---|---|---|---|
| SOL price | $107 | $119 | +11.05% |
| DeFi TVL | $5.94B | $6.51B | +9.47% |
| Stablecoin supply | $15.97B | $16.11B | +0.88% |
| DEX volume 24h | $3.63B | $2.66B | -26.74% |
| Mean TPS | 3,288 | 3,935 | +19.70% |
| Active validators | 689 | 673 | -2.32% |
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
