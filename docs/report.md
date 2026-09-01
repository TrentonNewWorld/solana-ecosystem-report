# Solana Ecosystem Report

_Generated 2026-09-01T18:51:38Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-01T18:51:38Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.85s |
| Snapshots in history | 60 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,530 non-vote TPS** (4,663 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.316s**.
- **678 active validators** (16 delinquent, holding 0.039% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $98.8** (-5.40% over 24h), market cap $57.82B.
- **DeFi TVL $5.76B** (+0.42% 7d, +22.08% 30d), against $15.61B of stablecoins settled on Solana.
- **$2.50B of DEX volume in 24h** across 120 protocols, generating $13.50M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 16 | 9 +/- 1.483 (median of last 59) | Delinquent validators is 16, 4.7 robust standard deviations above its recent median of 9 (+77.8%). |
| 🟠 warning | True TPS (non-vote) | 2529.6 | 1.59e+03 tx/s +/- 269 tx/s (median of last 59) | True TPS (non-vote) is 2.53e+03 tx/s, 3.5 robust standard deviations above its recent median of 1.59e+03 tx/s (+59.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.1 |
| Current epoch | 1026 (61.05% complete) |
| Slot | 263,717 of 432,000 in epoch |
| Absolute slot | 443,495,717 |
| Block height | 421,543,269 |
| Lifetime transactions | 544,201,441,083 |
| TPS (now / mean / peak) | 5,367 / 4,663 / 5,408 |
| True TPS, non-vote (now / mean) | 3,266 / 2,530 |
| Slot time (mean / worst) | 0.316s / 0.333s |

Epoch 1026 has **168,283 slots remaining**, about **14h 46m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 16 (2.31% delinquent) |
| Total stake | 438,201,819 SOL |
| Delinquent stake | 169,518 SOL (0.039%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.17% |
| Commission (mean / median) | 12.49% / 5.0% |
| Zero-commission validators | 244 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,174,436 | 3.919% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,281,426 | 3.716% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,434,730 | 2.838% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,480,709 | 2.620% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,455,250 | 2.158% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,506 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,044,016 | 2.064% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,216,300 | 1.647% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,930,213 | 1.582% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,591,885 | 1.504% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `prt1s9dMM15LdsUX9HugajzqPB5WVN8a2mw3frAiCfj` | 115,247 | 443,486,942 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 20,335 | 443,407,939 |
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `FEjcS4JCTqitjzW4Zj3Va2ioZZKf7MqsCMnrrgGLSvjm` | 10,450 | 443,348,723 |
| `QXmsTYFK7YT2BpP2AnvXwuRpfwmsJZpovLcUqdSjoK1` | 3,021 | 442,786,121 |
| `GdSJPrzj8q1QJV53s1cHMcpbPhodgB9kjG7X9kq8Z56r` | 2,125 | 443,299,656 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 443,438,639 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `Fy6zNoZ1eCPpQX3JXeQ9Yd1HW1BFL8rrFmDvYYDnuxjT` | 212 | 442,800,351 |
| `8sdFdnuKsY5KvpEU7gPi7qH1fP5DdYWfDhiF7NLjtaX8` | 176 | 442,758,837 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $98.8 | -5.40% 24h ↓ |
| Market cap | $57.82B | |
| Spot volume 24h | $3.19B | |
| DeFi TVL | $5.76B | -0.45% 1d / +0.42% 7d / +22.08% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $15.61B | |
| Stablecoin supply (all pegs) | $15.67B | |
| DEX volume 24h | $2.50B | +29.63% 1d |
| DEX volume 7d / 30d | $17.68B / $62.73B | |
| Fees + app revenue 24h | $13.50M | +9.70% 1d |
| Circulating supply | 585,206,598 SOL (92.41% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $939.21M | 37.55% |
| BisonFi | $232.85M | 9.31% |
| Orca DEX | $213.88M | 8.55% |
| Raydium AMM | $153.10M | 6.12% |
| Meteora DLMM | $149.33M | 5.97% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-01 |
| - | [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) | 2026-08-31 |
| SIMD-608 | [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) | 2026-08-31 |
| SIMD-610 | [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) | 2026-08-31 |
| SIMD-609 | [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) | 2026-08-31 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-08-31 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-08-29 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-08-27 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-01T18:51:38Z | Change |
|---|---|---|---|
| SOL price | $107 | $99 | -8.04% |
| DeFi TVL | $5.94B | $5.76B | -3.08% |
| Stablecoin supply | $15.97B | $15.61B | -2.28% |
| DEX volume 24h | $3.63B | $2.50B | -31.13% |
| Mean TPS | 3,288 | 4,663 | +41.84% |
| Active validators | 689 | 678 | -1.60% |
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
