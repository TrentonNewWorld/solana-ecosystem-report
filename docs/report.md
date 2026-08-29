# Solana Ecosystem Report

_Generated 2026-08-29T03:09:03Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-29T03:09:03Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.42s |
| Snapshots in history | 30 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,765 non-vote TPS** (3,914 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **687 active validators** (10 delinquent, holding 0.009% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $103.97** (-1.94% over 24h), market cap $60.73B.
- **DeFi TVL $5.87B** (+5.77% 7d, +22.40% 30d), against $15.95B of stablecoins settled on Solana.
- **$2.62B of DEX volume in 24h** across 119 protocols, generating $15.45M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 103.97 | $107 +/- $0 (median of last 29) | SOL price is $104, 9.4 robust standard deviations below its recent median of $107 (-3.1%). |
| 🔴 critical | DEX volume (24h) | 2615026955.2200003 | $3,632,065,012 +/- $189,528,870 (median of last 29) | DEX volume (24h) is $2,615,026,955, 5.4 robust standard deviations below its recent median of $3,632,065,012 (-28.0%). |
| 🟠 warning | Mean TPS | 3914.0 | 3.41e+03 tx/s +/- 121 tx/s (median of last 29) | Mean TPS is 3.91e+03 tx/s, 4.2 robust standard deviations above its recent median of 3.41e+03 tx/s (+14.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.1 |
| Current epoch | 1024 (30.70% complete) |
| Slot | 132,625 of 432,000 in epoch |
| Absolute slot | 442,500,625 |
| Block height | 420,548,571 |
| Lifetime transactions | 542,961,316,182 |
| TPS (now / mean / peak) | 3,794 / 3,914 / 4,356 |
| True TPS, non-vote (now / mean) | 1,618 / 1,765 |
| Slot time (mean / worst) | 0.318s / 0.33s |

Epoch 1024 has **299,375 slots remaining**, about **26h 26m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 687 / 10 (1.43% delinquent) |
| Total stake | 436,134,289 SOL |
| Delinquent stake | 38,674 SOL (0.009%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.90% / 24.15% |
| Commission (mean / median) | 13.04% / 5% |
| Zero-commission validators | 249 |

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
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 20,333 | 442,454,940 |
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 442,346,701 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `25quQGzrtcU224Kk7G5YDJ9oJXgYsiur8pZ7pAnCMhhV` | 663 | 440,636,516 |
| `8sdFdnuKsY5KvpEU7gPi7qH1fP5DdYWfDhiF7NLjtaX8` | 176 | 442,424,477 |
| `8Ug1zHMVDHAra2TaMFkUa6oWyLYoEhWGzcxL81yA5zmy` | 2 | 0 |
| `34kE8AGJazhgrsovREiB2Uru1CuhN4gCznNAmVUxB9AB` | 2 | 442,337,841 |
| `97zQpQHRnkxvgCkHg3yJhrWVbm8224v39QMCjjcxLkUL` | 1 | 442,179,355 |
| `93jNtLuu5MF3Me4MGidwQFq8Pg7iVWiRHioXm3aYhsv6` | 0 | 440,639,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $103.97 | -1.94% 24h ↓ |
| Market cap | $60.73B | |
| Spot volume 24h | $5.43B | |
| DeFi TVL | $5.87B | -1.22% 1d / +5.77% 7d / +22.40% 30d |
| TVL 90-day peak | $5.94B | |
| Stablecoin supply (USD peg) | $15.95B | |
| Stablecoin supply (all pegs) | $16.01B | |
| DEX volume 24h | $2.62B | -29.33% 1d |
| DEX volume 7d / 30d | $20.95B / $60.86B | |
| Fees + app revenue 24h | $15.45M | -5.24% 1d |
| Circulating supply | 584,161,895 SOL (92.27% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $576.29M | 22.04% |
| Orca DEX | $338.68M | 12.95% |
| BisonFi | $331.44M | 12.67% |
| Meteora DLMM | $279.39M | 10.68% |
| Raydium AMM | $170.74M | 6.53% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-08-29T03:09:03Z | Change |
|---|---|---|---|
| SOL price | $107 | $104 | -3.23% |
| DeFi TVL | $5.94B | $5.87B | -1.22% |
| Stablecoin supply | $15.97B | $15.95B | -0.17% |
| DEX volume 24h | $3.63B | $2.62B | -28.00% |
| Mean TPS | 3,288 | 3,914 | +19.05% |
| Active validators | 689 | 687 | -0.29% |
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
