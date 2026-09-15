# Solana Ecosystem Report

_Generated 2026-09-15T19:15:20Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-15T19:15:20Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.04s |
| Snapshots in history | 187 |
| Anomalies flagged | 1 (0 critical) |

## At a glance

- The network is processing **3,330 non-vote TPS** (5,453 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **679 active validators** (10 delinquent, holding 0.036% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $98.22** (-5.00% over 24h), market cap $57.66B.
- **DeFi TVL $5.79B** (-2.27% 7d, +20.12% 30d), against $15.66B of stablecoins settled on Solana.
- **$2.53B of DEX volume in 24h** across 123 protocols, generating $13.58M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | True TPS (non-vote) | 3329.5 | 1.69e+03 tx/s +/- 468 tx/s (median of last 186) | True TPS (non-vote) is 3.33e+03 tx/s, 3.5 robust standard deviations above its recent median of 1.69e+03 tx/s (+96.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1035 (47.94% complete) |
| Slot | 207,116 of 432,000 in epoch |
| Absolute slot | 447,327,116 |
| Block height | 425,368,881 |
| Lifetime transactions | 548,792,675,981 |
| TPS (now / mean / peak) | 4,600 / 5,453 / 6,829 |
| True TPS, non-vote (now / mean) | 2,456 / 3,330 |
| Slot time (mean / worst) | 0.318s / 0.33s |

Epoch 1035 has **224,884 slots remaining**, about **19h 51m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 10 (1.45% delinquent) |
| Total stake | 439,248,639 SOL |
| Delinquent stake | 160,291 SOL (0.036%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.32% |
| Commission (mean / median) | 12.33% / 5% |
| Zero-commission validators | 244 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,757,712 | 4.043% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,373,377 | 3.728% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,492,605 | 2.844% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,369,566 | 2.588% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,669,319 | 2.201% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,225 | 2.107% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,035,103 | 2.057% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,372,355 | 1.678% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,944,775 | 1.581% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,553,626 | 1.492% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `3r5ZXC1yFqMmk8VwDdUJbEdPmZ8KZvEkzd5ThEYRetTk` | 128,297 | 446,560,438 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 19,356 | 447,256,040 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,812 | 446,874,801 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,044,285 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 197 | 445,809,612 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 100 | 446,995,996 |
| `inQRWLtWjrZYz4z9xiPH9G8oMaGqKdeSeh7DUkGPVDL` | 14 | 445,699,097 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 2 | 384,048,870 |
| `GdSJPrzj8q1QJV53s1cHMcpbPhodgB9kjG7X9kq8Z56r` | 1 | 446,256,027 |
| `BGDs7o5ef2orSUReKaovgzvZLtdFzbq7fz1UMAaiaRdA` | 1 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $98.22 | -5.00% 24h ↓ |
| Market cap | $57.66B | |
| Spot volume 24h | $3.84B | |
| DeFi TVL | $5.79B | -0.78% 1d / -2.27% 7d / +20.12% 30d |
| TVL 90-day peak | $6.03B | |
| Stablecoin supply (USD peg) | $15.66B | |
| Stablecoin supply (all pegs) | $15.72B | |
| DEX volume 24h | $2.53B | +41.27% 1d |
| DEX volume 7d / 30d | $18.20B / $76.86B | |
| Fees + app revenue 24h | $13.58M | -3.25% 1d |
| Circulating supply | 587,027,752 SOL (92.57% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $445.38M | 17.60% |
| BisonFi | $315.80M | 12.48% |
| Raydium AMM | $241.36M | 9.54% |
| Meteora DLMM | $198.81M | 7.86% |
| fomo Wallet | $187.20M | 7.40% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) | 2026-09-15 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-15 |
| SIMD-582 | [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) | 2026-09-15 |
| - | [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) | 2026-09-14 |
| - | [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) | 2026-09-14 |
| SIMD-558 | [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) | 2026-09-14 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-11 |
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-11 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |
| [`v4.4.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | Release v4.4.0-alpha.2 | 2026-08-28 |
| [`v4.3.0-beta.3`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | Release v4.3.0-beta.3 | 2026-08-28 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-15T19:15:20Z | Change |
|---|---|---|---|
| SOL price | $107 | $98 | -8.58% |
| DeFi TVL | $5.94B | $5.79B | -2.60% |
| Stablecoin supply | $15.97B | $15.66B | -1.97% |
| DEX volume 24h | $3.63B | $2.53B | -30.34% |
| Mean TPS | 3,288 | 5,453 | +65.87% |
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
