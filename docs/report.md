# Solana Ecosystem Report

_Generated 2026-09-30T15:53:43Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-30T15:53:43Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.94s |
| Snapshots in history | 312 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **2,208 non-vote TPS** (4,703 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.268s**.
- **671 active validators** (12 delinquent, holding 0.056% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $119.46** (+0.95% over 24h), market cap $70.21B.
- **DeFi TVL $6.55B** (+0.20% 7d, +12.88% 30d), against $16.32B of stablecoins settled on Solana.
- **$2.53B of DEX volume in 24h** across 127 protocols, generating $14.86M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | SOL price | 119.46 | $104 +/- $5 (median of last 305) | SOL price is $119, 3.1 robust standard deviations above its recent median of $104 (+14.6%). |
| 🟠 warning | DeFi TVL | 6547759595 | $5,924,750,516 +/- $159,789,426 (median of last 311) | DeFi TVL is $6,547,759,595, 3.9 robust standard deviations above its recent median of $5,924,750,516 (+10.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1046 (32.08% complete) |
| Slot | 138,565 of 432,000 in epoch |
| Absolute slot | 452,010,565 |
| Block height | 430,049,885 |
| Lifetime transactions | 554,469,504,529 |
| TPS (now / mean / peak) | 4,845 / 4,703 / 5,657 |
| True TPS, non-vote (now / mean) | 2,328 / 2,208 |
| Slot time (mean / worst) | 0.268s / 0.278s |

Epoch 1046 has **293,435 slots remaining**, about **21h 50m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 12 (1.76% delinquent) |
| Total stake | 440,549,645 SOL |
| Delinquent stake | 247,615 SOL (0.056%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.91% / 24.47% |
| Commission (mean / median) | 12.59% / 5% |
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
| `ACCRENAtboR1MyyoiPvwNZNkjt1GcLARrACh6hZXdddF` | 70,200 | 451,953,922 |
| `ViKLknQuks11DLEjZ7Y2aNYAAT7Q3NTKLGxs8rdnLVi` | 43,391 | 451,647,273 |
| `QUANT7qKUEW4PS4eP9jq4K35rDHpgWkWcgjbW1CwnGJ` | 24,129 | 451,950,298 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 451,962,771 |
| `6hcGvZypizjf6PPsxboshZHRqefyQKSG9L8vZqYdm7UY` | 4,580 | 451,830,270 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 451,518,013 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $119.46 | +0.95% 24h ↑ |
| Market cap | $70.21B | |
| Spot volume 24h | $4.07B | |
| DeFi TVL | $6.55B | +1.41% 1d / +0.20% 7d / +12.88% 30d |
| TVL 90-day peak | $6.64B | |
| Stablecoin supply (USD peg) | $16.32B | |
| Stablecoin supply (all pegs) | $16.38B | |
| DEX volume 24h | $2.53B | -4.80% 1d |
| DEX volume 7d / 30d | $16.90B / $78.33B | |
| Fees + app revenue 24h | $14.86M | -15.16% 1d |
| Circulating supply | 588,005,721 SOL (92.60% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $374.43M | 14.77% |
| BisonFi | $349.04M | 13.77% |
| PumpSwap | $337.46M | 13.32% |
| Raydium AMM | $276.91M | 10.93% |
| Meteora DLMM | $189.70M | 7.49% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-503 | [SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) | 2026-09-30 |
| SIMD-677 | [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) | 2026-09-30 |
| SIMD-511 | [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-09-30 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-09-30 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-29 |
| SIMD-630 | [SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-29 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-09-29 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-28 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-30T15:53:43Z | Change |
|---|---|---|---|
| SOL price | $107 | $119 | +11.19% |
| DeFi TVL | $5.94B | $6.55B | +10.15% |
| Stablecoin supply | $15.97B | $16.32B | +2.14% |
| DEX volume 24h | $3.63B | $2.53B | -30.23% |
| Mean TPS | 3,288 | 4,703 | +43.06% |
| Active validators | 689 | 671 | -2.61% |
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
