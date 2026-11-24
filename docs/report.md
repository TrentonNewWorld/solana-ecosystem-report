# Solana Ecosystem Report

_Generated 2026-11-24T20:07:11Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-24T20:07:11Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.27s |
| Snapshots in history | 693 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,137 non-vote TPS** (2,137 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **660 active validators** (27 delinquent, holding 0.019% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $68.96** (-5.48% over 24h), market cap $40.83B.
- **DeFi TVL $4.52B** (-3.93% 7d, -21.46% 30d), against $13.19B of stablecoins settled on Solana.
- **$1.81B of DEX volume in 24h** across 145 protocols, generating $8.46M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 68.96 | $103 +/- $8 (median of last 685) | SOL price is $69, 4.6 robust standard deviations below its recent median of $103 (-33.3%). |
| 🔴 critical | Stablecoin supply | 13191083860.09 | $15,803,265,626 +/- $566,754,067 (median of last 692) | Stablecoin supply is $13,191,083,860, 4.6 robust standard deviations below its recent median of $15,803,265,626 (-16.5%). |
| 🟠 warning | DeFi TVL | 4523914526 | $5,890,756,500 +/- $342,833,429 (median of last 691) | DeFi TVL is $4,523,914,526, 4.0 robust standard deviations below its recent median of $5,890,756,500 (-23.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1096 (0.10% complete) |
| Slot | 436 of 432,000 in epoch |
| Absolute slot | 473,472,436 |
| Block height | 451,485,554 |
| Lifetime transactions | 568,217,196,879 |
| TPS (now / mean / peak) | 2,153 / 2,137 / 3,279 |
| True TPS, non-vote (now / mean) | 2,153 / 2,137 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1096 has **431,564 slots remaining**, about **25h 46m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 27 (3.93% delinquent) |
| Total stake | 424,790,146 SOL |
| Delinquent stake | 82,684 SOL (0.019%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.00% / 24.99% |
| Commission (mean / median) | 13.07% / 5.0% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,003,336 | 4.003% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,962,347 | 3.758% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,418,809 | 2.924% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,242,837 | 2.411% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,885,206 | 2.327% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,157 | 2.264% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,283,706 | 2.185% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,015,948 | 1.887% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,968,352 | 1.640% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,779,304 | 1.596% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 37,402 | 472,608,648 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,417 | 473,471,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 12,537 | 471,311,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `47hzyKgoz9Fu1HP4mR48tvAFj7akCFZKGzZqWo32sNqG` | 46 | 472,988,210 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $68.96 | -5.48% 24h ↓ |
| Market cap | $40.83B | |
| Spot volume 24h | $2.66B | |
| DeFi TVL | $4.52B | -2.03% 1d / -3.93% 7d / -21.46% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.19B | |
| Stablecoin supply (all pegs) | $13.27B | |
| DEX volume 24h | $1.81B | +85.09% 1d |
| DEX volume 7d / 30d | $11.24B / $48.17B | |
| Fees + app revenue 24h | $8.46M | +43.17% 1d |
| Circulating supply | 592,120,475 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $238.22M | 13.19% |
| BisonFi | $204.07M | 11.30% |
| Raydium AMM | $171.17M | 9.48% |
| Meteora DLMM | $166.92M | 9.24% |
| Scorch | $159.21M | 8.82% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-24 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-24 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-11-24 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-24 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-24 |
| - | [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) | 2026-11-24 |
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-23 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-23 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-24T20:07:11Z | Change |
|---|---|---|---|
| SOL price | $107 | $69 | -35.82% |
| DeFi TVL | $5.94B | $4.52B | -23.90% |
| Stablecoin supply | $15.97B | $13.19B | -17.42% |
| DEX volume 24h | $3.63B | $1.81B | -50.28% |
| Mean TPS | 3,288 | 2,137 | -35.00% |
| Active validators | 689 | 660 | -4.21% |
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
