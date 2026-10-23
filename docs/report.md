# Solana Ecosystem Report

_Generated 2026-10-23T15:55:58Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-23T15:55:58Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.81s |
| Snapshots in history | 488 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,324 non-vote TPS** (2,324 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.212s**.
- **656 active validators** (20 delinquent, holding 0.295% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $104.5** (-0.05% over 24h), market cap $61.62B.
- **DeFi TVL $5.84B** (-2.40% 7d, -10.23% 30d), against $15.51B of stablecoins settled on Solana.
- **$2.04B of DEX volume in 24h** across 138 protocols, generating $11.29M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.295 | 0.024% +/- 0.027% (median of last 487) | Delinquent stake is 0.295%, 10.2 robust standard deviations above its recent median of 0.024% (+1129.2%). |
| 🟠 warning | Mean TPS | 2324.4 | 4.39e+03 tx/s +/- 675 tx/s (median of last 487) | Mean TPS is 2.32e+03 tx/s, 3.1 robust standard deviations below its recent median of 4.39e+03 tx/s (-47.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1065 (97.64% complete) |
| Slot | 421,823 of 432,000 in epoch |
| Absolute slot | 460,501,823 |
| Block height | 438,534,014 |
| Lifetime transactions | 563,408,760,030 |
| TPS (now / mean / peak) | 2,302 / 2,324 / 2,983 |
| True TPS, non-vote (now / mean) | 2,302 / 2,324 |
| Slot time (mean / worst) | 0.212s / 0.217s |

Epoch 1065 has **10,177 slots remaining**, about **35m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 656 / 20 (2.96% delinquent) |
| Total stake | 438,318,926 SOL |
| Delinquent stake | 1,294,795 SOL (0.295%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.91% / 24.38% |
| Commission (mean / median) | 13.21% / 5.0% |
| Zero-commission validators | 221 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,133,144 | 3.909% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,621 | 3.643% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,556,096 | 2.865% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,936,237 | 2.495% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,726,420 | 2.219% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,476,174 | 2.162% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,244,629 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,797,559 | 1.779% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,036,293 | 1.605% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,002,101 | 1.597% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `7tKWFaaLi2FJSqukHxUrnXph8M3ynrqn3kEkKPpgcNHZ` | 558,475 | 460,079,999 |
| `GVYt3tbokX7mH4i86AA6Nh5hPiHEekercNZyNevviotL` | 234,444 | 460,079,999 |
| `SyNdica7qx3njeVKNgXvV7KC1NjPYNS4fyb3NxgevLH` | 156,876 | 460,079,999 |
| `HdQ1Ap8wm6Mz65FaP8jMNBVfCDv5T9NdS8UTSvHmcotn` | 115,580 | 460,079,999 |
| `5K8qgC9nHzKHSSyo9fKLsMfYmavYdMgEaYx86cMmVKVv` | 99,964 | 460,079,999 |
| `SANDhe6azby4EMLJd8N77QTk5K92n2tCi4NXba7iwuc` | 43,615 | 460,079,999 |
| `reyYoUdFgtDLxAWW1hyn5xk2PHstA3j8zUrerQi9Ayq` | 42,390 | 460,079,999 |
| `Fe5zMqkmoYbwnXH9RHjFy7YMRnak9so2bzPBroPJ4iiX` | 20,435 | 460,079,999 |
| `BfxZj7ckfRGHxByn7aHgH2puyXhfjAUvULtRjJo4rd8C` | 11,735 | 459,643,077 |
| `DzPT1ZWDeURdTj38QBSceWnrpYFxZRBLPRXmUgHVDAGR` | 10,274 | 460,079,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $104.5 | -0.05% 24h ↓ |
| Market cap | $61.62B | |
| Spot volume 24h | $2.17B | |
| DeFi TVL | $5.84B | -2.36% 1d / -2.40% 7d / -10.23% 30d |
| TVL 90-day peak | $6.61B | |
| Stablecoin supply (USD peg) | $15.51B | |
| Stablecoin supply (all pegs) | $15.60B | |
| DEX volume 24h | $2.04B | -10.18% 1d |
| DEX volume 7d / 30d | $13.69B / $65.07B | |
| Fees + app revenue 24h | $11.29M | -5.61% 1d |
| Circulating supply | 589,653,167 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $312.02M | 15.30% |
| PumpSwap | $259.02M | 12.70% |
| Orca DEX | $200.70M | 9.84% |
| Tessera V | $187.55M | 9.20% |
| pump.fun | $142.23M | 6.97% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-23 |
| SIMD-690 | [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) | 2026-10-23 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-10-23 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-10-23 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-10-22 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-10-22 |
| SIMD-550 | [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) | 2026-10-21 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) | 2026-10-21 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |
| [`v4.4.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | Release v4.4.0-beta.1 | 2026-10-13 |
| [`v4.5.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | Release v4.5.0-alpha.2 | 2026-10-08 |
| [`v4.5.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | Release v4.5.0-alpha.1 | 2026-10-03 |
| [`v4.4.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | Release v4.4.0-beta.0 | 2026-09-28 |
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-10-23T15:55:58Z | Change |
|---|---|---|---|
| SOL price | $107 | $104 | -2.74% |
| DeFi TVL | $5.94B | $5.84B | -1.80% |
| Stablecoin supply | $15.97B | $15.51B | -2.89% |
| DEX volume 24h | $3.63B | $2.04B | -43.85% |
| Mean TPS | 3,288 | 2,324 | -29.30% |
| Active validators | 689 | 656 | -4.79% |
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
