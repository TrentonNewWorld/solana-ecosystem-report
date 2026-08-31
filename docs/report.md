# Solana Ecosystem Report

_Generated 2026-08-31T17:02:48Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-31T17:02:48Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.7s |
| Snapshots in history | 51 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,511 non-vote TPS** (4,641 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **679 active validators** (18 delinquent, holding 0.010% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $102.85** (-3.62% over 24h), market cap $60.17B.
- **DeFi TVL $5.79B** (+4.04% 7d, +21.78% 30d), against $15.68B of stablecoins settled on Solana.
- **$1.93B of DEX volume in 24h** across 120 protocols, generating $12.31M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Mean TPS | 4640.8 | 3.47e+03 tx/s +/- 260 tx/s (median of last 50) | Mean TPS is 4.64e+03 tx/s, 4.5 robust standard deviations above its recent median of 3.47e+03 tx/s (+33.9%). |
| 🔴 critical | DEX volume (24h) | 1929632644.74 | $3,632,065,012 +/- $100,911,558 (median of last 50) | DEX volume (24h) is $1,929,632,645, 16.9 robust standard deviations below its recent median of $3,632,065,012 (-46.9%). |
| 🟠 warning | True TPS (non-vote) | 2511.3 | 1.58e+03 tx/s +/- 264 tx/s (median of last 50) | True TPS (non-vote) is 2.51e+03 tx/s, 3.5 robust standard deviations above its recent median of 1.58e+03 tx/s (+58.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.1 |
| Current epoch | 1025 (93.34% complete) |
| Slot | 403,229 of 432,000 in epoch |
| Absolute slot | 443,203,229 |
| Block height | 421,250,895 |
| Lifetime transactions | 543,829,973,241 |
| TPS (now / mean / peak) | 4,495 / 4,641 / 5,715 |
| True TPS, non-vote (now / mean) | 2,370 / 2,511 |
| Slot time (mean / worst) | 0.318s / 0.328s |

Epoch 1025 has **28,771 slots remaining**, about **2h 32m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 18 (2.58% delinquent) |
| Total stake | 437,127,890 SOL |
| Delinquent stake | 45,385 SOL (0.010%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.94% / 24.25% |
| Commission (mean / median) | 12.46% / 5% |
| Zero-commission validators | 246 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,203,741 | 3.936% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,085,807 | 3.680% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,389,824 | 2.834% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,479,512 | 2.626% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,452,658 | 2.162% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,293,056 | 2.126% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,023,631 | 2.064% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,295,972 | 1.669% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,201,762 | 1.648% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,589,845 | 1.508% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 21,787 | 443,198,814 |
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `QXmsTYFK7YT2BpP2AnvXwuRpfwmsJZpovLcUqdSjoK1` | 3,022 | 442,786,121 |
| `GdSJPrzj8q1QJV53s1cHMcpbPhodgB9kjG7X9kq8Z56r` | 2,126 | 442,919,425 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 443,150,836 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `Fy6zNoZ1eCPpQX3JXeQ9Yd1HW1BFL8rrFmDvYYDnuxjT` | 315 | 442,800,351 |
| `8sdFdnuKsY5KvpEU7gPi7qH1fP5DdYWfDhiF7NLjtaX8` | 176 | 442,758,837 |
| `qjUuLxWo29QCBr7ZQw4EPLkAtmjHS2ZdZpZcH9g7fRb` | 153 | 442,800,457 |
| `53ANFYA6BCDzdtiEeWawm5bqsH1Qgmjog8oMo5N4o4wU` | 132 | 442,786,073 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $102.85 | -3.62% 24h ↓ |
| Market cap | $60.17B | |
| Spot volume 24h | $3.74B | |
| DeFi TVL | $5.79B | -2.11% 1d / +4.04% 7d / +21.78% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $15.68B | |
| Stablecoin supply (all pegs) | $15.74B | |
| DEX volume 24h | $1.93B | +15.50% 1d |
| DEX volume 7d / 30d | $18.17B / $61.53B | |
| Fees + app revenue 24h | $12.31M | +9.75% 1d |
| Circulating supply | 585,120,830 SOL (92.41% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $732.11M | 37.94% |
| Orca DEX | $258.15M | 13.38% |
| BisonFi | $184.51M | 9.56% |
| Meteora DLMM | $142.67M | 7.39% |
| Manifest Trade | $134.61M | 6.98% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) | 2026-08-31 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-08-31 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-08-29 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-08-27 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-08-27 |
| SIMD-612 | [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) | 2026-08-26 |
| SIMD-608 | [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) | 2026-08-26 |
| SIMD-610 | [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) | 2026-08-26 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | Release v4.4.0-alpha.2 | 2026-08-28 |
| [`v4.3.0-beta.3`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | Release v4.3.0-beta.3 | 2026-08-28 |
| [`v4.2.2`](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | Release v4.2.2 | 2026-08-28 |
| [`v4.3.0-beta.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | Release v4.3.0-beta.2 | 2026-08-21 |
| [`v4.3.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | Release v4.3.0-beta.1 | 2026-08-21 |
| [`v4.2.1`](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | Release v4.2.1 | 2026-08-13 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-08-31T17:02:48Z | Change |
|---|---|---|---|
| SOL price | $107 | $103 | -4.27% |
| DeFi TVL | $5.94B | $5.79B | -2.67% |
| Stablecoin supply | $15.97B | $15.68B | -1.84% |
| DEX volume 24h | $3.63B | $1.93B | -46.87% |
| Mean TPS | 3,288 | 4,641 | +41.16% |
| Active validators | 689 | 679 | -1.45% |
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
