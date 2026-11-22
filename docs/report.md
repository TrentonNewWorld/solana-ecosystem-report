# Solana Ecosystem Report

_Generated 2026-11-22T22:26:39Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-22T22:26:39Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.18s |
| Snapshots in history | 685 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,810 non-vote TPS** (1,810 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (23 delinquent, holding 0.012% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $69.99** (-0.30% over 24h), market cap $41.45B.
- **DeFi TVL $4.60B** (-0.25% 7d, -21.26% 30d), against $13.03B of stablecoins settled on Solana.
- **$1.35B of DEX volume in 24h** across 144 protocols, generating $7.59M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 69.99 | $103 +/- $7 (median of last 677) | SOL price is $70, 4.7 robust standard deviations below its recent median of $103 (-32.4%). |
| 🔴 critical | Stablecoin supply | 13034250300.14 | $15,811,775,149 +/- $562,860,394 (median of last 684) | Stablecoin supply is $13,034,250,300, 4.9 robust standard deviations below its recent median of $15,811,775,149 (-17.6%). |
| 🟠 warning | DeFi TVL | 4603298593 | $5,895,037,123 +/- $329,012,798 (median of last 683) | DeFi TVL is $4,603,298,593, 3.9 robust standard deviations below its recent median of $5,895,037,123 (-21.9%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1094 (23.12% complete) |
| Slot | 99,860 of 432,000 in epoch |
| Absolute slot | 472,707,860 |
| Block height | 450,721,468 |
| Lifetime transactions | 567,915,782,059 |
| TPS (now / mean / peak) | 1,707 / 1,810 / 2,559 |
| True TPS, non-vote (now / mean) | 1,707 / 1,810 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1094 has **332,140 slots remaining**, about **19h 50m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 23 (3.36% delinquent) |
| Total stake | 425,691,542 SOL |
| Delinquent stake | 50,496 SOL (0.012%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.99% |
| Commission (mean / median) | 12.89% / 5.0% |
| Zero-commission validators | 220 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,918,440 | 3.974% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,346,959 | 3.840% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,401,889 | 2.913% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,243,005 | 2.406% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,842,253 | 2.312% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,612,896 | 2.258% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,269,555 | 2.178% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,998,895 | 1.879% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,495 | 1.641% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,775,083 | 1.592% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 37,687 | 472,608,648 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 12,767 | 471,311,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `29qPvStb2AxuhQBwyJfZRbnANrZRsUrQAGfyooAZbfKw` | 1 | 460,079,999 |
| `PEBBLETUXFPdrwm5heff4x1VsrypGS1fNSRPEF6LiZL` | 1 | 466,127,999 |
| `CBSrVMzHqnjb1td6diYaqy2Nq1GotkKQBB6i5eaR1ZyR` | 1 | 464,520,717 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $69.99 | -0.30% 24h ↓ |
| Market cap | $41.45B | |
| Spot volume 24h | $1.80B | |
| DeFi TVL | $4.60B | +1.18% 1d / -0.25% 7d / -21.26% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.03B | |
| Stablecoin supply (all pegs) | $13.12B | |
| DEX volume 24h | $1.35B | -28.59% 1d |
| DEX volume 7d / 30d | $11.29B / $48.78B | |
| Fees + app revenue 24h | $7.59M | -8.71% 1d |
| Circulating supply | 592,016,892 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $153.40M | 11.40% |
| Scorch | $127.86M | 9.50% |
| PumpSwap | $124.04M | 9.22% |
| Orca DEX | $122.58M | 9.11% |
| Meteora DLMM | $96.82M | 7.19% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-22T22:26:39Z | Change |
|---|---|---|---|
| SOL price | $107 | $70 | -34.86% |
| DeFi TVL | $5.94B | $4.60B | -22.56% |
| Stablecoin supply | $15.97B | $13.03B | -18.40% |
| DEX volume 24h | $3.63B | $1.35B | -62.94% |
| Mean TPS | 3,288 | 1,810 | -44.95% |
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
