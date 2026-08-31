# Solana Ecosystem Report

_Generated 2026-08-31T01:38:07Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-08-31T01:38:07Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.3s |
| Snapshots in history | 48 |
| Anomalies flagged | 5 (1 critical) |

## At a glance

- The network is processing **2,231 non-vote TPS** (4,342 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.319s**.
- **677 active validators** (20 delinquent, holding 0.067% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $101.67** (-3.31% over 24h), market cap $59.49B.
- **DeFi TVL $5.81B** (+4.45% 7d, +22.26% 30d), against $15.71B of stablecoins settled on Solana.
- **$1.87B of DEX volume in 24h** across 120 protocols, generating $11.07M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DEX volume (24h) | 1866506780.74 | $3,632,065,012 +/- $100,911,558 (median of last 47) | DEX volume (24h) is $1,866,506,781, 17.5 robust standard deviations below its recent median of $3,632,065,012 (-48.6%). |
| 🟠 warning | Mean TPS | 4342.2 | 3.45e+03 tx/s +/- 237 tx/s (median of last 47) | Mean TPS is 4.34e+03 tx/s, 3.8 robust standard deviations above its recent median of 3.45e+03 tx/s (+25.8%). |
| 🟠 warning | Delinquent stake | 0.067 | 0.010% +/- 0.018% (median of last 47) | Delinquent stake is 0.067%, 3.2 robust standard deviations above its recent median of 0.010% (+570.0%). |
| 🟠 warning | Delinquent validators | 20 | 9 +/- 3.516 (median of last 47) | Delinquent validators is 20, 3.1 robust standard deviations above its recent median of 9 (+122.2%). |
| 🟠 warning | SOL price | 101.67 | $107 +/- $1 (median of last 47) | SOL price is $102, 3.3 robust standard deviations below its recent median of $107 (-4.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.1 |
| Current epoch | 1025 (52.87% complete) |
| Slot | 228,393 of 432,000 in epoch |
| Absolute slot | 443,028,393 |
| Block height | 421,076,115 |
| Lifetime transactions | 543,607,655,110 |
| TPS (now / mean / peak) | 4,045 / 4,342 / 4,904 |
| True TPS, non-vote (now / mean) | 1,929 / 2,231 |
| Slot time (mean / worst) | 0.319s / 0.333s |

Epoch 1025 has **203,607 slots remaining**, about **18h 2m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 20 (2.87% delinquent) |
| Total stake | 437,127,890 SOL |
| Delinquent stake | 295,015 SOL (0.067%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.94% / 24.25% |
| Commission (mean / median) | 12.49% / 5% |
| Zero-commission validators | 245 |

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
| `4vqwZsEEEsKtSqqEWbLyFAciWg66jGLP9zrbcZ1Hsrxb` | 158,857 | 443,025,987 |
| `mrgn2vsZ5EJ8YEfAMNPXmRux7th9cNfBasQ1JJvVwPn` | 90,772 | 443,015,256 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 21,787 | 442,981,783 |
| `gangtRyGPTvYWb8K3xS2feJQaCks4iJ7rytFUPtVqSY` | 15,325 | 441,252,679 |
| `QXmsTYFK7YT2BpP2AnvXwuRpfwmsJZpovLcUqdSjoK1` | 3,022 | 442,786,121 |
| `GdSJPrzj8q1QJV53s1cHMcpbPhodgB9kjG7X9kq8Z56r` | 2,126 | 442,919,425 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 1,344 | 442,679,838 |
| `ChaosDKeBjU22B4nnvYWXyTRPuWTzJBR4m3QPfBw6Tta` | 828 | 441,983,754 |
| `Fy6zNoZ1eCPpQX3JXeQ9Yd1HW1BFL8rrFmDvYYDnuxjT` | 315 | 442,800,351 |
| `8sdFdnuKsY5KvpEU7gPi7qH1fP5DdYWfDhiF7NLjtaX8` | 176 | 442,758,837 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $101.67 | -3.31% 24h ↓ |
| Market cap | $59.49B | |
| Spot volume 24h | $3.05B | |
| DeFi TVL | $5.81B | -0.68% 1d / +4.45% 7d / +22.26% 30d |
| TVL 90-day peak | $6.01B | |
| Stablecoin supply (USD peg) | $15.71B | |
| Stablecoin supply (all pegs) | $15.78B | |
| DEX volume 24h | $1.87B | +11.72% 1d |
| DEX volume 7d / 30d | $17.96B / $61.32B | |
| Fees + app revenue 24h | $11.07M | -1.28% 1d |
| Circulating supply | 585,121,506 SOL (92.41% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $732.11M | 39.22% |
| Orca DEX | $215.23M | 11.53% |
| BisonFi | $184.51M | 9.89% |
| Meteora DLMM | $142.67M | 7.64% |
| Raydium AMM | $108.96M | 5.84% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-08-31T01:38:07Z | Change |
|---|---|---|---|
| SOL price | $107 | $102 | -5.37% |
| DeFi TVL | $5.94B | $5.81B | -2.28% |
| Stablecoin supply | $15.97B | $15.71B | -1.64% |
| DEX volume 24h | $3.63B | $1.87B | -48.61% |
| Mean TPS | 3,288 | 4,342 | +32.08% |
| Active validators | 689 | 677 | -1.74% |
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
