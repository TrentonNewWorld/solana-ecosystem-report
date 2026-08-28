# Solana Ecosystem Report

_Generated 2026-08-28T20:23:02Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-28T20:23:02Z` |
| Sources healthy | 8 of 8 |
| Collection time | 11.23s |
| Snapshots in history | 26 |
| Anomalies flagged | 3 (3 critical) |

## At a glance

- The network is processing **2,456 non-vote TPS** (4,608 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **689 active validators** (8 delinquent, holding 0.004% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $103.39** (-5.62% over 24h), market cap $60.40B.
- **DeFi TVL $5.81B** (+8.91% 7d, +21.14% 30d), against $15.90B of stablecoins settled on Solana.
- **$3.70B of DEX volume in 24h** across 119 protocols, generating $16.30M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Mean TPS | 4608.2 | 3.37e+03 tx/s +/- 101 tx/s (median of last 25) | Mean TPS is 4.61e+03 tx/s, 12.2 robust standard deviations above its recent median of 3.37e+03 tx/s (+36.7%). |
| 🔴 critical | True TPS (non-vote) | 2456.3 | 1.49e+03 tx/s +/- 103 tx/s (median of last 25) | True TPS (non-vote) is 2.46e+03 tx/s, 9.4 robust standard deviations above its recent median of 1.49e+03 tx/s (+64.8%). |
| 🔴 critical | SOL price | 103.39 | $107 +/- $0 (median of last 25) | SOL price is $103, 12.7 robust standard deviations below its recent median of $107 (-3.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-beta.2 |
| Current epoch | 1024 (12.93% complete) |
| Slot | 55,839 of 432,000 in epoch |
| Absolute slot | 442,423,839 |
| Block height | 420,471,877 |
| Lifetime transactions | 542,858,292,430 |
| TPS (now / mean / peak) | 4,528 / 4,608 / 5,127 |
| True TPS, non-vote (now / mean) | 2,404 / 2,456 |
| Slot time (mean / worst) | 0.318s / 0.328s |

Epoch 1024 has **376,161 slots remaining**, about **33h 13m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 689 / 8 (1.15% delinquent) |
| Total stake | 436,134,289 SOL |
| Delinquent stake | 18,165 SOL (0.004%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.90% / 24.15% |
| Commission (mean / median) | 12.87% / 5% |
| Zero-commission validators | 251 |

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
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 442,346,701 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `25quQGzrtcU224Kk7G5YDJ9oJXgYsiur8pZ7pAnCMhhV` | 663 | 440,636,516 |
| `8Ug1zHMVDHAra2TaMFkUa6oWyLYoEhWGzcxL81yA5zmy` | 2 | 0 |
| `34kE8AGJazhgrsovREiB2Uru1CuhN4gCznNAmVUxB9AB` | 2 | 442,337,841 |
| `97zQpQHRnkxvgCkHg3yJhrWVbm8224v39QMCjjcxLkUL` | 1 | 442,179,355 |
| `93jNtLuu5MF3Me4MGidwQFq8Pg7iVWiRHioXm3aYhsv6` | 0 | 440,639,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $103.39 | -5.62% 24h ↓ |
| Market cap | $60.40B | |
| Spot volume 24h | $6.09B | |
| DeFi TVL | $5.81B | +0.58% 1d / +8.91% 7d / +21.14% 30d |
| TVL 90-day peak | $5.81B | |
| Stablecoin supply (USD peg) | $15.90B | |
| Stablecoin supply (all pegs) | $15.97B | |
| DEX volume 24h | $3.70B | +57.34% 1d |
| DEX volume 7d / 30d | $22.25B / $60.53B | |
| Fees + app revenue 24h | $16.30M | +7.19% 1d |
| Circulating supply | 584,162,166 SOL (92.27% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $1.46B | 39.47% |
| BisonFi | $416.99M | 11.27% |
| Orca DEX | $353.00M | 9.54% |
| Meteora DLMM | $245.52M | 6.64% |
| Raydium AMM | $186.41M | 5.04% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-08-28 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-08-28T20:23:02Z | Change |
|---|---|---|---|
| SOL price | $107 | $103 | -3.77% |
| DeFi TVL | $5.94B | $5.81B | -2.31% |
| Stablecoin supply | $15.97B | $15.90B | -0.47% |
| DEX volume 24h | $3.63B | $3.70B | +1.87% |
| Mean TPS | 3,288 | 4,608 | +40.17% |
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
