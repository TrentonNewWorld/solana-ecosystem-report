# Solana Ecosystem Report

_Generated 2026-09-04T01:23:43Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-04T01:23:43Z` |
| Sources healthy | 8 of 8 |
| Collection time | 13.09s |
| Snapshots in history | 82 |
| Anomalies flagged | 1 (1 critical) |

## At a glance

- The network is processing **1,440 non-vote TPS** (3,564 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.315s**.
- **675 active validators** (19 delinquent, holding 0.070% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $103.74** (+3.62% over 24h), market cap $60.71B.
- **DeFi TVL $5.95B** (-0.98% 7d, +23.90% 30d), against $16.20B of stablecoins settled on Solana.
- **$2.37B of DEX volume in 24h** across 121 protocols, generating $10.73M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.07 | 0.010% +/- 0.003% (median of last 81) | Delinquent stake is 0.070%, 20.2 robust standard deviations above its recent median of 0.010% (+600.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.2 |
| Current epoch | 1028 (5.24% complete) |
| Slot | 22,647 of 432,000 in epoch |
| Absolute slot | 444,118,647 |
| Block height | 422,165,071 |
| Lifetime transactions | 544,945,994,975 |
| TPS (now / mean / peak) | 3,399 / 3,564 / 4,093 |
| True TPS, non-vote (now / mean) | 1,270 / 1,440 |
| Slot time (mean / worst) | 0.315s / 0.326s |

Epoch 1028 has **409,353 slots remaining**, about **35h 49m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 19 (2.74% delinquent) |
| Total stake | 436,898,866 SOL |
| Delinquent stake | 304,348 SOL (0.070%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.98% / 24.39% |
| Commission (mean / median) | 12.24% / 5% |
| Zero-commission validators | 244 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,393,318 | 3.981% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,259 | 3.736% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,459,602 | 2.852% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,379,843 | 2.605% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,567,623 | 2.190% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,278,151 | 2.124% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,042,760 | 2.070% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,376,879 | 1.688% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,127,366 | 1.631% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,593,517 | 1.509% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `vahVByZszdHguLa7U7GLz8UdUFN85mcwdkefiqVjtGt` | 163,335 | 444,087,651 |
| `xLabsqDpN9WHXEXSJXk1yhqh5H8BgcqiBP1CR6Mkjcb` | 78,252 | 443,788,373 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 20,297 | 444,096,006 |
| `prt1s9dMM15LdsUX9HugajzqPB5WVN8a2mw3frAiCfj` | 19,797 | 443,486,942 |
| `FEjcS4JCTqitjzW4Zj3Va2ioZZKf7MqsCMnrrgGLSvjm` | 10,451 | 443,348,723 |
| `8B2Z2R8dRvqFcXuLBwinu3Jq7HQidCaJCnDuRRqeJLC1` | 4,062 | 443,965,922 |
| `QXmsTYFK7YT2BpP2AnvXwuRpfwmsJZpovLcUqdSjoK1` | 3,021 | 442,786,121 |
| `GdSJPrzj8q1QJV53s1cHMcpbPhodgB9kjG7X9kq8Z56r` | 2,125 | 444,096,006 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 443,438,639 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $103.74 | +3.62% 24h ↑ |
| Market cap | $60.71B | |
| Spot volume 24h | $4.27B | |
| DeFi TVL | $5.95B | +0.00% 1d / -0.98% 7d / +23.90% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $16.20B | |
| Stablecoin supply (all pegs) | $16.27B | |
| DEX volume 24h | $2.37B | +3.62% 1d |
| DEX volume 7d / 30d | $15.38B / $64.64B | |
| Fees + app revenue 24h | $10.73M | +1.82% 1d |
| Circulating supply | 585,360,761 SOL (92.41% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $838.66M | 35.36% |
| Orca DEX | $285.64M | 12.04% |
| BisonFi | $232.51M | 9.80% |
| Meteora DLMM | $186.49M | 7.86% |
| Manifest Trade | $174.59M | 7.36% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-558 | [SIMD-0558 - Current Leader Sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/621) | 2026-09-03 |
| SIMD-464 | [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) | 2026-09-03 |
| SIMD-608 | [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) | 2026-09-02 |
| SIMD-609 | [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) | 2026-09-02 |
| SIMD-610 | [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) | 2026-09-02 |
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-01 |
| - | [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) | 2026-08-31 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-08-31 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |
| [`v4.4.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | Release v4.4.0-alpha.2 | 2026-08-28 |
| [`v4.3.0-beta.3`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | Release v4.3.0-beta.3 | 2026-08-28 |
| [`v4.2.2`](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | Release v4.2.2 | 2026-08-28 |
| [`v4.3.0-beta.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | Release v4.3.0-beta.2 | 2026-08-21 |
| [`v4.3.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | Release v4.3.0-beta.1 | 2026-08-21 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-04T01:23:43Z | Change |
|---|---|---|---|
| SOL price | $107 | $104 | -3.44% |
| DeFi TVL | $5.94B | $5.95B | +0.16% |
| Stablecoin supply | $15.97B | $16.20B | +1.44% |
| DEX volume 24h | $3.63B | $2.37B | -34.69% |
| Mean TPS | 3,288 | 3,564 | +8.42% |
| Active validators | 689 | 675 | -2.03% |
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
