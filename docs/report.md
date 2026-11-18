# Solana Ecosystem Report

_Generated 2026-11-18T16:43:41Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-18T16:43:41Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.11s |
| Snapshots in history | 662 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,740 non-vote TPS** (2,740 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.217s**.
- **660 active validators** (25 delinquent, holding 0.015% of stake). It takes **17 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $72.32** (+0.22% over 24h), market cap $42.75B.
- **DeFi TVL $4.75B** (-5.59% 7d, -18.63% 30d), against $13.15B of stablecoins settled on Solana.
- **$1.51B of DEX volume in 24h** across 144 protocols, generating $8.20M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 72.32 | $104 +/- $6 (median of last 654) | SOL price is $72, 5.0 robust standard deviations below its recent median of $104 (-30.2%). |
| 🔴 critical | Stablecoin supply | 13152105454.52 | $15,857,989,159 +/- $546,676,756 (median of last 661) | Stablecoin supply is $13,152,105,455, 4.9 robust standard deviations below its recent median of $15,857,989,159 (-17.1%). |
| 🟠 warning | DeFi TVL | 4748529466 | $5,898,952,490 +/- $308,752,587 (median of last 660) | DeFi TVL is $4,748,529,466, 3.7 robust standard deviations below its recent median of $5,898,952,490 (-19.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1090 (29.09% complete) |
| Slot | 125,655 of 432,000 in epoch |
| Absolute slot | 471,005,655 |
| Block height | 449,020,170 |
| Lifetime transactions | 567,282,133,651 |
| TPS (now / mean / peak) | 3,243 / 2,740 / 3,243 |
| True TPS, non-vote (now / mean) | 3,243 / 2,740 |
| Slot time (mean / worst) | 0.217s / 0.223s |

Epoch 1090 has **306,345 slots remaining**, about **18h 27m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 (3.65% delinquent) |
| Total stake | 426,746,616 SOL |
| Delinquent stake | 66,021 SOL (0.015%) |
| Nakamoto coefficient | 17 |
| Top 1 / top 10 stake share | 3.99% / 24.98% |
| Commission (mean / median) | 12.61% / 5.0% |
| Zero-commission validators | 220 |

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
| SOL price | $72.32 | +0.22% 24h ↑ |
| Market cap | $42.75B | |
| Spot volume 24h | $2.28B | |
| DeFi TVL | $4.75B | +0.84% 1d / -5.59% 7d / -18.63% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.15B | |
| Stablecoin supply (all pegs) | $13.23B | |
| DEX volume 24h | $1.51B | +2.01% 1d |
| DEX volume 7d / 30d | $10.72B / $50.40B | |
| Fees + app revenue 24h | $8.20M | -1.59% 1d |
| Circulating supply | 591,794,813 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $229.48M | 15.20% |
| Meteora DLMM | $172.72M | 11.44% |
| PumpSwap | $155.29M | 10.29% |
| BisonFi | $149.60M | 9.91% |
| Raydium AMM | $146.18M | 9.68% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-17 |
| SIMD-643 | [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) _(draft)_ | 2026-11-17 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-16 |
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-14 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-14 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-18T16:43:41Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -32.69% |
| DeFi TVL | $5.94B | $4.75B | -20.12% |
| Stablecoin supply | $15.97B | $13.15B | -17.67% |
| DEX volume 24h | $3.63B | $1.51B | -58.44% |
| Mean TPS | 3,288 | 2,740 | -16.64% |
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
