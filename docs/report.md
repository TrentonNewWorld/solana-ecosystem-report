# Solana Ecosystem Report

_Generated 2026-08-30T14:24:25Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-30T14:24:25Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.97s |
| Snapshots in history | 42 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,682 non-vote TPS** (3,813 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.317s**.
- **678 active validators** (19 delinquent, holding 0.057% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $106.83** (+2.36% over 24h), market cap $62.51B.
- **DeFi TVL $5.90B** (+6.21% 7d, +22.25% 30d), against $15.84B of stablecoins settled on Solana.
- **$1.67B of DEX volume in 24h** across 120 protocols, generating $11.21M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 19 | 9 +/- 2.038 (median of last 41) | Delinquent validators is 19, 4.9 robust standard deviations above its recent median of 9 (+111.1%). |
| 🟠 warning | DEX volume (24h) | 1670710752.31 | $3,632,065,012 +/- $601,071,515 (median of last 41) | DEX volume (24h) is $1,670,710,752, 3.3 robust standard deviations below its recent median of $3,632,065,012 (-54.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.1 |
| Current epoch | 1025 (23.42% complete) |
| Slot | 101,153 of 432,000 in epoch |
| Absolute slot | 442,901,153 |
| Block height | 420,948,932 |
| Lifetime transactions | 543,437,246,427 |
| TPS (now / mean / peak) | 3,610 / 3,813 / 4,386 |
| True TPS, non-vote (now / mean) | 1,506 / 1,682 |
| Slot time (mean / worst) | 0.317s / 0.33s |

Epoch 1025 has **330,847 slots remaining**, about **29h 7m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 19 (2.73% delinquent) |
| Total stake | 437,127,890 SOL |
| Delinquent stake | 250,466 SOL (0.057%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.94% / 24.25% |
| Commission (mean / median) | 12.18% / 5.0% |
| Zero-commission validators | 247 |

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
| `nymsndUdAZyUPpWYz5VEg8Ghj9cFvwTRgciLogpmYaQ` | 116,435 | 442,886,028 |
| `mrgn2vsZ5EJ8YEfAMNPXmRux7th9cNfBasQ1JJvVwPn` | 90,772 | 442,876,058 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 21,787 | 442,803,737 |
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `QXmsTYFK7YT2BpP2AnvXwuRpfwmsJZpovLcUqdSjoK1` | 3,022 | 442,786,121 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 442,679,838 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `Fy6zNoZ1eCPpQX3JXeQ9Yd1HW1BFL8rrFmDvYYDnuxjT` | 315 | 442,800,351 |
| `8sdFdnuKsY5KvpEU7gPi7qH1fP5DdYWfDhiF7NLjtaX8` | 176 | 442,758,837 |
| `qjUuLxWo29QCBr7ZQw4EPLkAtmjHS2ZdZpZcH9g7fRb` | 153 | 442,800,457 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $106.83 | +2.36% 24h ↑ |
| Market cap | $62.51B | |
| Spot volume 24h | $2.34B | |
| DeFi TVL | $5.90B | +0.57% 1d / +6.21% 7d / +22.25% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $15.84B | |
| Stablecoin supply (all pegs) | $15.90B | |
| DEX volume 24h | $1.67B | -35.51% 1d |
| DEX volume 7d / 30d | $19.18B / $61.29B | |
| Fees + app revenue 24h | $11.21M | -28.70% 1d |
| Circulating supply | 585,121,953 SOL (92.41% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $584.75M | 35.00% |
| BisonFi | $149.87M | 8.97% |
| Meteora DLMM | $142.97M | 8.56% |
| Orca DEX | $130.58M | 7.82% |
| pump.fun | $110.08M | 6.59% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-08-29 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-08-27 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-08-27 |
| - | [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) | 2026-08-26 |
| SIMD-612 | [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) | 2026-08-26 |
| SIMD-608 | [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) | 2026-08-26 |
| SIMD-610 | [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) | 2026-08-26 |
| SIMD-609 | [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) | 2026-08-26 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-08-30T14:24:25Z | Change |
|---|---|---|---|
| SOL price | $107 | $107 | -0.57% |
| DeFi TVL | $5.94B | $5.90B | -0.70% |
| Stablecoin supply | $15.97B | $15.84B | -0.86% |
| DEX volume 24h | $3.63B | $1.67B | -54.00% |
| Mean TPS | 3,288 | 3,813 | +15.98% |
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
