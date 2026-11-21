# Solana Ecosystem Report

_Generated 2026-11-21T22:09:52Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-21T22:09:52Z` |
| Sources healthy | 8 of 8 |
| Collection time | 11.11s |
| Snapshots in history | 679 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,940 non-vote TPS** (1,940 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **661 active validators** (24 delinquent, holding 0.017% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $70.09** (+1.63% over 24h), market cap $41.50B.
- **DeFi TVL $4.61B** (-5.08% 7d, -22.74% 30d), against $13.02B of stablecoins settled on Solana.
- **$1.88B of DEX volume in 24h** across 144 protocols, generating $8.30M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 70.09 | $104 +/- $7 (median of last 671) | SOL price is $70, 4.8 robust standard deviations below its recent median of $104 (-32.3%). |
| 🔴 critical | Stablecoin supply | 13021755531.42 | $15,821,149,382 +/- $554,732,402 (median of last 678) | Stablecoin supply is $13,021,755,531, 5.0 robust standard deviations below its recent median of $15,821,149,382 (-17.7%). |
| 🟠 warning | DeFi TVL | 4606268989 | $5,896,694,283 +/- $320,456,685 (median of last 677) | DeFi TVL is $4,606,268,989, 4.0 robust standard deviations below its recent median of $5,896,694,283 (-21.9%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1093 (29.01% complete) |
| Slot | 125,304 of 432,000 in epoch |
| Absolute slot | 472,301,304 |
| Block height | 450,315,235 |
| Lifetime transactions | 567,790,070,804 |
| TPS (now / mean / peak) | 2,154 / 1,940 / 2,521 |
| True TPS, non-vote (now / mean) | 2,154 / 1,940 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1093 has **306,696 slots remaining**, about **18h 18m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 (3.50% delinquent) |
| Total stake | 428,316,392 SOL |
| Delinquent stake | 73,431 SOL (0.017%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.98% / 24.85% |
| Commission (mean / median) | 12.74% / 5% |
| Zero-commission validators | 220 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,043,671 | 3.979% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,329,817 | 3.813% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,620 | 2.898% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,241,724 | 2.391% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,826,793 | 2.294% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,616,961 | 2.245% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,166 | 2.157% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,985,737 | 1.864% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,985,062 | 1.631% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,774,154 | 1.582% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 42,969 | 471,311,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,418 | 470,879,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `5DutFKQ8qPmbjFEmp31QH9JDYJXvwh9pma8ap5Phxk6H` | 1 | 465,304,579 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1 | 464,160,502 |
| `CBSrVMzHqnjb1td6diYaqy2Nq1GotkKQBB6i5eaR1ZyR` | 1 | 464,520,717 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $70.09 | +1.63% 24h ↑ |
| Market cap | $41.50B | |
| Spot volume 24h | $3.75B | |
| DeFi TVL | $4.61B | -2.22% 1d / -5.08% 7d / -22.74% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.02B | |
| Stablecoin supply (all pegs) | $13.10B | |
| DEX volume 24h | $1.88B | -1.02% 1d |
| DEX volume 7d / 30d | $11.64B / $49.47B | |
| Fees + app revenue 24h | $8.30M | -10.84% 1d |
| Circulating supply | 591,961,658 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $209.15M | 11.10% |
| BisonFi | $206.37M | 10.95% |
| Meteora DLMM | $177.91M | 9.44% |
| PumpSwap | $166.14M | 8.82% |
| Raydium AMM | $149.60M | 7.94% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-21T22:09:52Z | Change |
|---|---|---|---|
| SOL price | $107 | $70 | -34.76% |
| DeFi TVL | $5.94B | $4.61B | -22.51% |
| Stablecoin supply | $15.97B | $13.02B | -18.48% |
| DEX volume 24h | $3.63B | $1.88B | -48.11% |
| Mean TPS | 3,288 | 1,940 | -40.99% |
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
