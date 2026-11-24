# Solana Ecosystem Report

_Generated 2026-11-24T19:06:33Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-24T19:06:33Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.63s |
| Snapshots in history | 692 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,025 non-vote TPS** (2,025 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **661 active validators** (25 delinquent, holding 0.012% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $69.15** (-5.96% over 24h), market cap $40.96B.
- **DeFi TVL $4.53B** (-3.83% 7d, -21.38% 30d), against $13.18B of stablecoins settled on Solana.
- **$1.81B of DEX volume in 24h** across 145 protocols, generating $8.46M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 69.15 | $103 +/- $8 (median of last 684) | SOL price is $69, 4.5 robust standard deviations below its recent median of $103 (-33.1%). |
| 🔴 critical | Stablecoin supply | 13183151012.58 | $15,804,033,176 +/- $565,487,003 (median of last 691) | Stablecoin supply is $13,183,151,013, 4.6 robust standard deviations below its recent median of $15,804,033,176 (-16.6%). |
| 🟠 warning | DeFi TVL | 4528503960 | $5,892,191,280 +/- $344,073,488 (median of last 690) | DeFi TVL is $4,528,503,960, 4.0 robust standard deviations below its recent median of $5,892,191,280 (-23.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1095 (96.17% complete) |
| Slot | 415,473 of 432,000 in epoch |
| Absolute slot | 473,455,473 |
| Block height | 451,468,591 |
| Lifetime transactions | 568,209,425,694 |
| TPS (now / mean / peak) | 2,040 / 2,025 / 2,669 |
| True TPS, non-vote (now / mean) | 2,040 / 2,025 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1095 has **16,527 slots remaining**, about **59m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 25 (3.64% delinquent) |
| Total stake | 425,856,004 SOL |
| Delinquent stake | 52,412 SOL (0.012%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.00% / 24.96% |
| Commission (mean / median) | 13.07% / 5% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,046 | 3.999% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,091,420 | 3.779% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,158 | 2.915% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,240,508 | 2.405% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,856,366 | 2.314% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,634,022 | 2.262% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,276,354 | 2.178% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,005,660 | 1.880% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,776 | 1.641% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,778,434 | 1.592% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 37,544 | 472,608,648 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 12,541 | 471,311,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `47hzyKgoz9Fu1HP4mR48tvAFj7akCFZKGzZqWo32sNqG` | 46 | 472,988,210 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `Bithumb3zMpepFaLqtnnpbvNj1e3UiVFG26yKNVEHwux` | 1 | 467,384,112 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $69.15 | -5.96% 24h ↓ |
| Market cap | $40.96B | |
| Spot volume 24h | $2.73B | |
| DeFi TVL | $4.53B | -1.93% 1d / -3.83% 7d / -21.38% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.18B | |
| Stablecoin supply (all pegs) | $13.27B | |
| DEX volume 24h | $1.81B | +85.09% 1d |
| DEX volume 7d / 30d | $11.24B / $48.17B | |
| Fees + app revenue 24h | $8.46M | +43.17% 1d |
| Circulating supply | 592,071,535 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $238.22M | 13.19% |
| BisonFi | $204.07M | 11.30% |
| Raydium AMM | $174.97M | 9.69% |
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

| Metric | 2026-08-28T06:17:33Z | 2026-11-24T19:06:33Z | Change |
|---|---|---|---|
| SOL price | $107 | $69 | -35.64% |
| DeFi TVL | $5.94B | $4.53B | -23.82% |
| Stablecoin supply | $15.97B | $13.18B | -17.47% |
| DEX volume 24h | $3.63B | $1.81B | -50.28% |
| Mean TPS | 3,288 | 2,025 | -38.42% |
| Active validators | 689 | 661 | -4.06% |
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
