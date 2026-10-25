# Solana Ecosystem Report

_Generated 2026-10-25T23:13:37Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-25T23:13:37Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.12s |
| Snapshots in history | 509 |
| Anomalies flagged | 3 (0 critical) |

## At a glance

- The network is processing **1,740 non-vote TPS** (1,740 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.213s**.
- **665 active validators** (25 delinquent, holding 0.123% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $101.48** (-0.05% over 24h), market cap $59.86B.
- **DeFi TVL $5.73B** (-2.81% 7d, -11.24% 30d), against $15.53B of stablecoins settled on Solana.
- **$1.42B of DEX volume in 24h** across 138 protocols, generating $10.05M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Mean TPS | 1740.1 | 4.35e+03 tx/s +/- 721 tx/s (median of last 508) | Mean TPS is 1.74e+03 tx/s, 3.6 robust standard deviations below its recent median of 4.35e+03 tx/s (-60.0%). |
| 🟠 warning | Delinquent stake | 0.123 | 0.027% +/- 0.028% (median of last 508) | Delinquent stake is 0.123%, 3.4 robust standard deviations above its recent median of 0.027% (+355.6%). |
| 🟠 warning | Delinquent validators | 25 | 12 +/- 2.965 (median of last 508) | Delinquent validators is 25, 4.4 robust standard deviations above its recent median of 12 (+108.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1068 (14.73% complete) |
| Slot | 63,632 of 432,000 in epoch |
| Absolute slot | 461,439,632 |
| Block height | 439,467,018 |
| Lifetime transactions | 563,744,284,117 |
| TPS (now / mean / peak) | 1,293 / 1,740 / 2,303 |
| True TPS, non-vote (now / mean) | 1,293 / 1,740 |
| Slot time (mean / worst) | 0.213s / 0.219s |

Epoch 1068 has **368,368 slots remaining**, about **21h 47m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 25 (3.62% delinquent) |
| Total stake | 437,716,746 SOL |
| Delinquent stake | 540,246 SOL (0.123%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.91% / 24.54% |
| Commission (mean / median) | 12.91% / 5% |
| Zero-commission validators | 229 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,102,487 | 3.907% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,635,523 | 3.801% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,594,585 | 2.877% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,882,967 | 2.486% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,720,520 | 2.221% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,492,382 | 2.169% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,187,388 | 2.099% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,787,018 | 1.779% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,039,209 | 1.608% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,989,716 | 1.597% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `8LMatbjxgUW1S7CyuBhGk89BC9vhRzCRLwtXbyJru4Qi` | 266,141 | 461,375,999 |
| `9RXDftY5xyhtYyzk4z7U9ddvBF2Z8DMfXmV6P6du9dxS` | 135,667 | 460,943,999 |
| `D3DfFvmLBKkX9JJNEpJRXpM1pYTVPQ5dpPQRc9F49xk4` | 102,995 | 461,375,999 |
| `SANDhe6azby4EMLJd8N77QTk5K92n2tCi4NXba7iwuc` | 34,643 | 460,079,999 |
| `4KfAqBj3Jvi9GGngFK1MbZkjHTcSFyvhFnVwc2QrNiEh` | 398 | 460,079,999 |
| `D3wscqsBCJGFzzoB7dB7wQfJzSEFVzu8Rxugfnfk7rdm` | 375 | 458,009,563 |
| `29qPvStb2AxuhQBwyJfZRbnANrZRsUrQAGfyooAZbfKw` | 4 | 460,079,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `AGXZemZbyZjz5NBhufcob2pf8AXnr9HaGFUGNCfooWrB` | 2 | 402,784,479 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $101.48 | -0.05% 24h ↓ |
| Market cap | $59.86B | |
| Spot volume 24h | $1.42B | |
| DeFi TVL | $5.73B | -0.77% 1d / -2.81% 7d / -11.24% 30d |
| TVL 90-day peak | $6.61B | |
| Stablecoin supply (USD peg) | $15.53B | |
| Stablecoin supply (all pegs) | $15.62B | |
| DEX volume 24h | $1.42B | -28.74% 1d |
| DEX volume 7d / 30d | $13.69B / $63.42B | |
| Fees + app revenue 24h | $10.05M | -4.82% 1d |
| Circulating supply | 589,819,851 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $219.28M | 15.41% |
| Manifest Trade | $137.22M | 9.64% |
| Tessera V | $135.53M | 9.52% |
| Orca DEX | $123.01M | 8.64% |
| pump.fun | $119.13M | 8.37% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-10-25 |
| SIMD-690 | [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) | 2026-10-24 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-23 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-10-23 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-10-23 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-10-22 |
| SIMD-550 | [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) | 2026-10-21 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) | 2026-10-21 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0) | Release v4.4.0-rc.0 | 2026-10-24 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |
| [`v4.4.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | Release v4.4.0-beta.1 | 2026-10-13 |
| [`v4.5.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | Release v4.5.0-alpha.2 | 2026-10-08 |
| [`v4.5.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | Release v4.5.0-alpha.1 | 2026-10-03 |
| [`v4.4.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | Release v4.4.0-beta.0 | 2026-09-28 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-10-25T23:13:37Z | Change |
|---|---|---|---|
| SOL price | $107 | $101 | -5.55% |
| DeFi TVL | $5.94B | $5.73B | -3.60% |
| Stablecoin supply | $15.97B | $15.53B | -2.76% |
| DEX volume 24h | $3.63B | $1.42B | -60.82% |
| Mean TPS | 3,288 | 1,740 | -47.07% |
| Active validators | 689 | 665 | -3.48% |
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
