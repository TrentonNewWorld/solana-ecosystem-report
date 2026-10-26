# Solana Ecosystem Report

_Generated 2026-10-26T01:46:58Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-26T01:46:58Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.22s |
| Snapshots in history | 510 |
| Anomalies flagged | 3 (0 critical) |

## At a glance

- The network is processing **1,952 non-vote TPS** (1,952 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.213s**.
- **665 active validators** (25 delinquent, holding 0.123% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $100.6** (-1.73% over 24h), market cap $59.39B.
- **DeFi TVL $5.72B** (-2.22% 7d, -13.40% 30d), against $15.52B of stablecoins settled on Solana.
- **$1.35B of DEX volume in 24h** across 138 protocols, generating $10.09M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Mean TPS | 1952.4 | 4.35e+03 tx/s +/- 724 tx/s (median of last 509) | Mean TPS is 1.95e+03 tx/s, 3.3 robust standard deviations below its recent median of 4.35e+03 tx/s (-55.1%). |
| 🟠 warning | Delinquent stake | 0.123 | 0.027% +/- 0.028% (median of last 509) | Delinquent stake is 0.123%, 3.4 robust standard deviations above its recent median of 0.027% (+355.6%). |
| 🟠 warning | Delinquent validators | 25 | 12 +/- 2.965 (median of last 509) | Delinquent validators is 25, 4.4 robust standard deviations above its recent median of 12 (+108.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1068 (24.74% complete) |
| Slot | 106,882 of 432,000 in epoch |
| Absolute slot | 461,482,882 |
| Block height | 439,510,208 |
| Lifetime transactions | 563,763,821,234 |
| TPS (now / mean / peak) | 2,050 / 1,952 / 2,389 |
| True TPS, non-vote (now / mean) | 2,050 / 1,952 |
| Slot time (mean / worst) | 0.213s / 0.217s |

Epoch 1068 has **325,118 slots remaining**, about **19h 14m** at the current slot time.

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
| SOL price | $100.6 | -1.73% 24h ↓ |
| Market cap | $59.39B | |
| Spot volume 24h | $1.56B | |
| DeFi TVL | $5.72B | -0.45% 1d / -2.22% 7d / -13.40% 30d |
| TVL 90-day peak | $6.61B | |
| Stablecoin supply (USD peg) | $15.52B | |
| Stablecoin supply (all pegs) | $15.60B | |
| DEX volume 24h | $1.35B | -5.30% 1d |
| DEX volume 7d / 30d | $12.50B / $61.28B | |
| Fees + app revenue 24h | $10.09M | +0.41% 1d |
| Circulating supply | 589,819,799 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $219.28M | 16.27% |
| Manifest Trade | $141.65M | 10.51% |
| Tessera V | $135.53M | 10.06% |
| Orca DEX | $134.50M | 9.98% |
| pump.fun | $119.13M | 8.84% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-10-26T01:46:58Z | Change |
|---|---|---|---|
| SOL price | $107 | $101 | -6.37% |
| DeFi TVL | $5.94B | $5.72B | -3.76% |
| Stablecoin supply | $15.97B | $15.52B | -2.87% |
| DEX volume 24h | $3.63B | $1.35B | -62.90% |
| Mean TPS | 3,288 | 1,952 | -40.61% |
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
