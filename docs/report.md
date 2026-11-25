# Solana Ecosystem Report

_Generated 2026-11-25T15:32:39Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-25T15:32:39Z` |
| Sources healthy | 8 of 8 |
| Collection time | 11.56s |
| Snapshots in history | 697 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,481 non-vote TPS** (2,481 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **659 active validators** (28 delinquent, holding 0.042% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $66.9** (-2.96% over 24h), market cap $39.62B.
- **DeFi TVL $4.42B** (-7.90% 7d, -22.32% 30d), against $12.85B of stablecoins settled on Solana.
- **$1.46B of DEX volume in 24h** across 145 protocols, generating $7.15M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 66.9 | $103 +/- $8 (median of last 689) | SOL price is $67, 4.8 robust standard deviations below its recent median of $103 (-35.3%). |
| 🔴 critical | Stablecoin supply | 12852672345.07 | $15,788,053,142 +/- $576,317,756 (median of last 696) | Stablecoin supply is $12,852,672,345, 5.1 robust standard deviations below its recent median of $15,788,053,142 (-18.6%). |
| 🟠 warning | DeFi TVL | 4419128253 | $5,890,203,126 +/- $351,884,584 (median of last 695) | DeFi TVL is $4,419,128,253, 4.2 robust standard deviations below its recent median of $5,890,203,126 (-25.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1096 (75.41% complete) |
| Slot | 325,776 of 432,000 in epoch |
| Absolute slot | 473,797,776 |
| Block height | 451,810,810 |
| Lifetime transactions | 568,336,998,475 |
| TPS (now / mean / peak) | 2,847 / 2,481 / 3,312 |
| True TPS, non-vote (now / mean) | 2,847 / 2,481 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1096 has **106,224 slots remaining**, about **6h 20m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 28 (4.08% delinquent) |
| Total stake | 424,794,569 SOL |
| Delinquent stake | 178,974 SOL (0.042%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.00% / 24.99% |
| Commission (mean / median) | 13.13% / 5% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,003,542 | 4.003% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,962,658 | 3.758% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,418,812 | 2.923% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,242,949 | 2.411% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,885,209 | 2.327% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,268 | 2.264% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,283,847 | 2.185% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,016,085 | 1.887% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,968,432 | 1.640% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,779,378 | 1.596% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `DG6fVEB2Qy1jntvHVPui3R12CMqcwNNnjYPYdsbQ9ACP` | 96,290 | 473,749,295 |
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 37,402 | 472,608,648 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,417 | 473,471,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 12,537 | 471,311,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `47hzyKgoz9Fu1HP4mR48tvAFj7akCFZKGzZqWo32sNqG` | 46 | 472,988,210 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $66.9 | -2.96% 24h ↓ |
| Market cap | $39.62B | |
| Spot volume 24h | $2.70B | |
| DeFi TVL | $4.42B | -4.65% 1d / -7.90% 7d / -22.32% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.85B | |
| Stablecoin supply (all pegs) | $12.93B | |
| DEX volume 24h | $1.46B | -19.33% 1d |
| DEX volume 7d / 30d | $11.19B / $48.18B | |
| Fees + app revenue 24h | $7.15M | -15.53% 1d |
| Circulating supply | 592,128,180 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $190.49M | 13.08% |
| Orca DEX | $184.70M | 12.68% |
| Manifest Trade | $170.96M | 11.74% |
| Raydium AMM | $139.68M | 9.59% |
| Scorch | $134.08M | 9.20% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-25 |
| SIMD-506 | [Withdraw SIMD-0506](https://github.com/solana-foundation/solana-improvement-documents/pull/738) | 2026-11-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-11-25 |
| - | [100M CUs Pt2](https://github.com/solana-foundation/solana-improvement-documents/pull/698) | 2026-11-25 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-24 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-24 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-11-24 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-24 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v5.0.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | Release v5.0.0-alpha.1 | 2026-11-19 |
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-25T15:32:39Z | Change |
|---|---|---|---|
| SOL price | $107 | $67 | -37.73% |
| DeFi TVL | $5.94B | $4.42B | -25.66% |
| Stablecoin supply | $15.97B | $12.85B | -19.54% |
| DEX volume 24h | $3.63B | $1.46B | -59.89% |
| Mean TPS | 3,288 | 2,481 | -24.54% |
| Active validators | 689 | 659 | -4.35% |
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
