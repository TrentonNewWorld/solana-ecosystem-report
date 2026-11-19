# Solana Ecosystem Report

_Generated 2026-11-19T01:31:14Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-19T01:31:14Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.41s |
| Snapshots in history | 664 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,847 non-vote TPS** (1,847 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.216s**.
- **660 active validators** (25 delinquent, holding 0.015% of stake). It takes **17 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $73.1** (-1.72% over 24h), market cap $43.27B.
- **DeFi TVL $4.72B** (-6.34% 7d, -19.12% 30d), against $12.71B of stablecoins settled on Solana.
- **$1.53B of DEX volume in 24h** across 144 protocols, generating $10.04M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 73.1 | $104 +/- $6 (median of last 656) | SOL price is $73, 4.8 robust standard deviations below its recent median of $104 (-29.5%). |
| 🔴 critical | Stablecoin supply | 12708345959.06 | $15,850,439,112 +/- $545,154,873 (median of last 663) | Stablecoin supply is $12,708,345,959, 5.8 robust standard deviations below its recent median of $15,850,439,112 (-19.8%). |
| 🟠 warning | DeFi TVL | 4716274656 | $5,898,602,886 +/- $311,015,509 (median of last 662) | DeFi TVL is $4,716,274,656, 3.8 robust standard deviations below its recent median of $5,898,602,886 (-20.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1090 (63.07% complete) |
| Slot | 272,467 of 432,000 in epoch |
| Absolute slot | 471,152,467 |
| Block height | 449,166,818 |
| Lifetime transactions | 567,353,493,722 |
| TPS (now / mean / peak) | 1,874 / 1,847 / 2,547 |
| True TPS, non-vote (now / mean) | 1,874 / 1,847 |
| Slot time (mean / worst) | 0.216s / 0.222s |

Epoch 1090 has **159,533 slots remaining**, about **9h 34m** at the current slot time.

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
| SOL price | $73.1 | -1.72% 24h ↓ |
| Market cap | $43.27B | |
| Spot volume 24h | $2.21B | |
| DeFi TVL | $4.72B | -0.00% 1d / -6.34% 7d / -19.12% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.71B | |
| Stablecoin supply (all pegs) | $12.79B | |
| DEX volume 24h | $1.53B | +1.53% 1d |
| DEX volume 7d / 30d | $9.70B / $49.18B | |
| Fees + app revenue 24h | $10.04M | +23.41% 1d |
| Circulating supply | 591,796,346 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $246.07M | 16.05% |
| Meteora DLMM | $172.72M | 11.27% |
| PumpSwap | $155.29M | 10.13% |
| Raydium AMM | $155.03M | 10.11% |
| BisonFi | $149.60M | 9.76% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-19T01:31:14Z | Change |
|---|---|---|---|
| SOL price | $107 | $73 | -31.96% |
| DeFi TVL | $5.94B | $4.72B | -20.66% |
| Stablecoin supply | $15.97B | $12.71B | -20.44% |
| DEX volume 24h | $3.63B | $1.53B | -57.80% |
| Mean TPS | 3,288 | 1,847 | -43.81% |
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
