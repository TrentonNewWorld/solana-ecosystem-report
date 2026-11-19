# Solana Ecosystem Report

_Generated 2026-11-19T02:31:00Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-19T02:31:00Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.86s |
| Snapshots in history | 665 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,801 non-vote TPS** (1,801 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **660 active validators** (25 delinquent, holding 0.015% of stake). It takes **17 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $73.37** (-1.83% over 24h), market cap $43.47B.
- **DeFi TVL $4.71B** (-6.53% 7d, -19.29% 30d), against $12.70B of stablecoins settled on Solana.
- **$1.70B of DEX volume in 24h** across 144 protocols, generating $9.97M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 73.37 | $104 +/- $6 (median of last 657) | SOL price is $73, 4.7 robust standard deviations below its recent median of $104 (-29.2%). |
| 🔴 critical | Stablecoin supply | 12701497497.2 | $15,847,796,478 +/- $546,122,579 (median of last 664) | Stablecoin supply is $12,701,497,497, 5.8 robust standard deviations below its recent median of $15,847,796,478 (-19.9%). |
| 🟠 warning | DeFi TVL | 4706813408 | $5,898,269,013 +/- $312,120,688 (median of last 663) | DeFi TVL is $4,706,813,408, 3.8 robust standard deviations below its recent median of $5,898,269,013 (-20.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1090 (66.93% complete) |
| Slot | 289,135 of 432,000 in epoch |
| Absolute slot | 471,169,135 |
| Block height | 449,183,482 |
| Lifetime transactions | 567,359,950,254 |
| TPS (now / mean / peak) | 1,651 / 1,801 / 2,487 |
| True TPS, non-vote (now / mean) | 1,651 / 1,801 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1090 has **142,865 slots remaining**, about **8h 31m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 (3.65% delinquent) |
| Total stake | 426,746,616 SOL |
| Delinquent stake | 66,021 SOL (0.015%) |
| Nakamoto coefficient | 17 |
| Top 1 / top 10 stake share | 3.99% / 24.98% |
| Commission (mean / median) | 12.76% / 5.0% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,030,759 | 3.991% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,476,078 | 3.861% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,423,470 | 2.911% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,297,722 | 2.413% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,430 | 2.300% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,562 | 2.244% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,715 | 2.161% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,973,220 | 1.868% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,720 | 1.640% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,771,472 | 1.587% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,516 | 469,583,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,469 | 470,879,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `GdFaSCpPf9RqRjxkvXUCzLR62bEjmEPZMS9XRVFC3pDu` | 2 | 469,698,063 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 1 | 462,464,506 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 1 | 462,239,999 |
| `GAoCBDE9ABRYmhWUREDp4po4L8JgCPeQsPS77p1mx3WR` | 1 | 465,702,670 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $73.37 | -1.83% 24h ↓ |
| Market cap | $43.47B | |
| Spot volume 24h | $2.19B | |
| DeFi TVL | $4.71B | -1.87% 1d / -6.53% 7d / -19.29% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.70B | |
| Stablecoin supply (all pegs) | $12.79B | |
| DEX volume 24h | $1.70B | +12.72% 1d |
| DEX volume 7d / 30d | $10.05B / $49.53B | |
| Fees + app revenue 24h | $9.97M | +22.52% 1d |
| Circulating supply | 591,796,328 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $330.65M | 19.43% |
| Orca DEX | $252.77M | 14.85% |
| Meteora DLMM | $172.72M | 10.15% |
| Raydium AMM | $154.14M | 9.06% |
| BisonFi | $149.60M | 8.79% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-11-19 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-18 |
| SIMD-643 | [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) _(draft)_ | 2026-11-17 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-16 |
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-14 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-14 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-19T02:31:00Z | Change |
|---|---|---|---|
| SOL price | $107 | $73 | -31.71% |
| DeFi TVL | $5.94B | $4.71B | -20.82% |
| Stablecoin supply | $15.97B | $12.70B | -20.49% |
| DEX volume 24h | $3.63B | $1.70B | -53.15% |
| Mean TPS | 3,288 | 1,801 | -45.22% |
| Active validators | 689 | 660 | -4.21% |
| Nakamoto coefficient | 18 | 17 | -5.56% |

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
