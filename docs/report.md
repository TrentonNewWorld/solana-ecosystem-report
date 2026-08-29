# Solana Ecosystem Report

_Generated 2026-08-29T19:43:34Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-29T19:43:34Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.29s |
| Snapshots in history | 36 |
| Anomalies flagged | 2 (2 critical) |

## At a glance

- The network is processing **2,202 non-vote TPS** (4,360 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **689 active validators** (8 delinquent, holding 0.004% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $105.62** (+1.86% over 24h), market cap $61.67B.
- **DeFi TVL $5.90B** (+6.19% 7d, +22.90% 30d), against $15.89B of stablecoins settled on Solana.
- **$2.59B of DEX volume in 24h** across 119 protocols, generating $15.73M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Mean TPS | 4360.5 | 3.42e+03 tx/s +/- 135 tx/s (median of last 35) | Mean TPS is 4.36e+03 tx/s, 7.0 robust standard deviations above its recent median of 3.42e+03 tx/s (+27.7%). |
| 🔴 critical | True TPS (non-vote) | 2202.1 | 1.54e+03 tx/s +/- 145 tx/s (median of last 35) | True TPS (non-vote) is 2.2e+03 tx/s, 4.6 robust standard deviations above its recent median of 1.54e+03 tx/s (+43.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-beta.2 |
| Current epoch | 1024 (74.28% complete) |
| Slot | 320,901 of 432,000 in epoch |
| Absolute slot | 442,688,901 |
| Block height | 420,736,743 |
| Lifetime transactions | 543,188,783,158 |
| TPS (now / mean / peak) | 4,070 / 4,360 / 5,308 |
| True TPS, non-vote (now / mean) | 1,879 / 2,202 |
| Slot time (mean / worst) | 0.318s / 0.328s |

Epoch 1024 has **111,099 slots remaining**, about **9h 48m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 689 / 8 (1.15% delinquent) |
| Total stake | 436,134,289 SOL |
| Delinquent stake | 18,165 SOL (0.004%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.90% / 24.15% |
| Commission (mean / median) | 13.3% / 5% |
| Zero-commission validators | 248 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,991,835 | 3.896% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,737 | 3.677% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,393,242 | 2.842% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,460,007 | 2.628% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,292,131 | 2.131% | 7% |
| 6 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,081,213 | 2.082% | 0% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,001,204 | 2.064% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,294,487 | 1.673% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,192,557 | 1.649% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,585,996 | 1.510% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 442,679,838 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `25quQGzrtcU224Kk7G5YDJ9oJXgYsiur8pZ7pAnCMhhV` | 663 | 440,636,516 |
| `8Ug1zHMVDHAra2TaMFkUa6oWyLYoEhWGzcxL81yA5zmy` | 2 | 0 |
| `34kE8AGJazhgrsovREiB2Uru1CuhN4gCznNAmVUxB9AB` | 2 | 442,337,841 |
| `97zQpQHRnkxvgCkHg3yJhrWVbm8224v39QMCjjcxLkUL` | 1 | 442,179,355 |
| `93jNtLuu5MF3Me4MGidwQFq8Pg7iVWiRHioXm3aYhsv6` | 0 | 440,639,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $105.62 | +1.86% 24h ↑ |
| Market cap | $61.67B | |
| Spot volume 24h | $2.60B | |
| DeFi TVL | $5.90B | -1.95% 1d / +6.19% 7d / +22.90% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $15.89B | |
| Stablecoin supply (all pegs) | $15.96B | |
| DEX volume 24h | $2.59B | -29.99% 1d |
| DEX volume 7d / 30d | $21.24B / $61.20B | |
| Fees + app revenue 24h | $15.73M | -3.52% 1d |
| Circulating supply | 584,161,297 SOL (92.27% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $576.29M | 22.25% |
| BisonFi | $331.44M | 12.79% |
| Meteora DLMM | $279.39M | 10.78% |
| Orca DEX | $187.43M | 7.23% |
| Raydium AMM | $135.80M | 5.24% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-08-29T19:43:34Z | Change |
|---|---|---|---|
| SOL price | $107 | $106 | -1.69% |
| DeFi TVL | $5.94B | $5.90B | -0.82% |
| Stablecoin supply | $15.97B | $15.89B | -0.50% |
| DEX volume 24h | $3.63B | $2.59B | -28.67% |
| Mean TPS | 3,288 | 4,360 | +32.63% |
| Active validators | 689 | 689 | +0.00% |
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
