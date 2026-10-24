# Solana Ecosystem Report

_Generated 2026-10-24T18:22:15Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-24T18:22:15Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.75s |
| Snapshots in history | 497 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **1,791 non-vote TPS** (1,791 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.211s**.
- **665 active validators** (25 delinquent, holding 0.049% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $100.71** (-3.36% over 24h), market cap $59.39B.
- **DeFi TVL $5.68B** (-4.11% 7d, -10.76% 30d), against $15.51B of stablecoins settled on Solana.
- **$2.00B of DEX volume in 24h** across 138 protocols, generating $10.55M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Mean TPS | 1791.4 | 4.37e+03 tx/s +/- 689 tx/s (median of last 496) | Mean TPS is 1.79e+03 tx/s, 3.7 robust standard deviations below its recent median of 4.37e+03 tx/s (-59.0%). |
| 🟠 warning | Delinquent validators | 25 | 12 +/- 2.965 (median of last 496) | Delinquent validators is 25, 4.4 robust standard deviations above its recent median of 12 (+108.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1067 (1.48% complete) |
| Slot | 6,401 of 432,000 in epoch |
| Absolute slot | 460,950,401 |
| Block height | 438,980,167 |
| Lifetime transactions | 563,577,977,123 |
| TPS (now / mean / peak) | 1,402 / 1,791 / 2,715 |
| True TPS, non-vote (now / mean) | 1,402 / 1,791 |
| Slot time (mean / worst) | 0.211s / 0.222s |

Epoch 1067 has **425,599 slots remaining**, about **24h 56m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 25 (3.62% delinquent) |
| Total stake | 437,191,006 SOL |
| Delinquent stake | 214,659 SOL (0.049%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.91% / 24.58% |
| Commission (mean / median) | 12.91% / 5% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,099,113 | 3.911% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,646,121 | 3.808% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,588,035 | 2.879% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,881,430 | 2.489% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,721,918 | 2.224% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,483,244 | 2.169% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,837 | 2.108% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,036 | 1.781% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,038,249 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,006,653 | 1.603% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `9RXDftY5xyhtYyzk4z7U9ddvBF2Z8DMfXmV6P6du9dxS` | 136,180 | 460,943,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 43,045 | 460,511,999 |
| `SANDhe6azby4EMLJd8N77QTk5K92n2tCi4NXba7iwuc` | 34,634 | 460,079,999 |
| `4KfAqBj3Jvi9GGngFK1MbZkjHTcSFyvhFnVwc2QrNiEh` | 398 | 460,079,999 |
| `D3wscqsBCJGFzzoB7dB7wQfJzSEFVzu8Rxugfnfk7rdm` | 375 | 458,009,563 |
| `29qPvStb2AxuhQBwyJfZRbnANrZRsUrQAGfyooAZbfKw` | 4 | 460,079,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `F3Bv6jaD8dAK8UwTshyKbji58fUDWUP36oee8hu53pRP` | 2 | 0 |
| `J5C5REtd4q6zCpMQYsZ3t9tijQkZbkqhCiZNjRJBbu75` | 1 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $100.71 | -3.36% 24h ↓ |
| Market cap | $59.39B | |
| Spot volume 24h | $2.57B | |
| DeFi TVL | $5.68B | -3.09% 1d / -4.11% 7d / -10.76% 30d |
| TVL 90-day peak | $6.61B | |
| Stablecoin supply (USD peg) | $15.51B | |
| Stablecoin supply (all pegs) | $15.60B | |
| DEX volume 24h | $2.00B | -2.07% 1d |
| DEX volume 7d / 30d | $13.52B / $64.48B | |
| Fees + app revenue 24h | $10.55M | -8.04% 1d |
| Circulating supply | 589,764,586 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $342.50M | 17.15% |
| PumpSwap | $266.43M | 13.34% |
| Orca DEX | $183.81M | 9.20% |
| Tessera V | $162.38M | 8.13% |
| Manifest Trade | $153.94M | 7.71% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-10-24 |
| SIMD-690 | [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) | 2026-10-24 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-10-24 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-23 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-10-23 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-10-23 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-10-22 |
| SIMD-550 | [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) | 2026-10-21 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-10-24T18:22:15Z | Change |
|---|---|---|---|
| SOL price | $107 | $101 | -6.26% |
| DeFi TVL | $5.94B | $5.68B | -4.44% |
| Stablecoin supply | $15.97B | $15.51B | -2.89% |
| DEX volume 24h | $3.63B | $2.00B | -45.02% |
| Mean TPS | 3,288 | 1,791 | -45.51% |
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
