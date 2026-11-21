# Solana Ecosystem Report

_Generated 2026-11-21T00:57:48Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-21T00:57:48Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.56s |
| Snapshots in history | 674 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,442 non-vote TPS** (1,442 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (23 delinquent, holding 0.017% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $68.92** (-5.21% over 24h), market cap $40.80B.
- **DeFi TVL $4.56B** (-5.98% 7d, -23.48% 30d), against $13.02B of stablecoins settled on Solana.
- **$1.87B of DEX volume in 24h** across 144 protocols, generating $9.23M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 68.92 | $104 +/- $7 (median of last 666) | SOL price is $69, 5.2 robust standard deviations below its recent median of $104 (-33.4%). |
| 🔴 critical | Stablecoin supply | 13019894729.79 | $15,822,482,575 +/- $549,231,350 (median of last 673) | Stablecoin supply is $13,019,894,730, 5.1 robust standard deviations below its recent median of $15,822,482,575 (-17.7%). |
| 🟠 warning | DeFi TVL | 4562435531 | $5,897,537,772 +/- $317,881,093 (median of last 672) | DeFi TVL is $4,562,435,531, 4.2 robust standard deviations below its recent median of $5,897,537,772 (-22.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1092 (46.84% complete) |
| Slot | 202,347 of 432,000 in epoch |
| Absolute slot | 471,946,347 |
| Block height | 449,960,327 |
| Lifetime transactions | 567,671,166,621 |
| TPS (now / mean / peak) | 1,496 / 1,442 / 2,173 |
| True TPS, non-vote (now / mean) | 1,496 / 1,442 |
| Slot time (mean / worst) | 0.215s / 0.223s |

Epoch 1092 has **229,653 slots remaining**, about **13h 42m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 23 (3.36% delinquent) |
| Total stake | 428,985,797 SOL |
| Delinquent stake | 73,441 SOL (0.017%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.81% |
| Commission (mean / median) | 12.87% / 5.0% |
| Zero-commission validators | 220 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,041,638 | 3.973% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,354,101 | 3.812% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,891 | 2.896% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,309,121 | 2.403% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,779,397 | 2.280% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,564,403 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,683 | 2.152% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,986,182 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,985,765 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,773,182 | 1.579% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 42,980 | 471,311,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,420 | 470,879,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `5DutFKQ8qPmbjFEmp31QH9JDYJXvwh9pma8ap5Phxk6H` | 1 | 465,304,579 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 1 | 462,239,999 |
| `Bithumb3zMpepFaLqtnnpbvNj1e3UiVFG26yKNVEHwux` | 1 | 467,384,112 |
| `CBSrVMzHqnjb1td6diYaqy2Nq1GotkKQBB6i5eaR1ZyR` | 1 | 464,520,717 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $68.92 | -5.21% 24h ↓ |
| Market cap | $40.80B | |
| Spot volume 24h | $3.55B | |
| DeFi TVL | $4.56B | -0.03% 1d / -5.98% 7d / -23.48% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.02B | |
| Stablecoin supply (all pegs) | $13.10B | |
| DEX volume 24h | $1.87B | -1.73% 1d |
| DEX volume 7d / 30d | $10.44B / $48.27B | |
| Fees + app revenue 24h | $9.23M | -0.67% 1d |
| Circulating supply | 591,906,466 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $279.03M | 14.91% |
| Meteora DLMM | $237.03M | 12.67% |
| PumpSwap | $207.82M | 11.11% |
| Raydium AMM | $191.33M | 10.23% |
| BisonFi | $179.10M | 9.57% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-20 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-20 |
| SIMD-83 | [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) | 2026-11-20 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-19 |
| SIMD-706 | [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-11-19 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-19 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-19 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-11-19 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-21T00:57:48Z | Change |
|---|---|---|---|
| SOL price | $107 | $69 | -35.85% |
| DeFi TVL | $5.94B | $4.56B | -23.25% |
| Stablecoin supply | $15.97B | $13.02B | -18.49% |
| DEX volume 24h | $3.63B | $1.87B | -48.48% |
| Mean TPS | 3,288 | 1,442 | -56.14% |
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
