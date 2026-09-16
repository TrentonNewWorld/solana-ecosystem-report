# Solana Ecosystem Report

_Generated 2026-09-16T19:07:00Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-16T19:07:00Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.52s |
| Snapshots in history | 196 |
| Anomalies flagged | 1 (0 critical) |

## At a glance

- The network is processing **3,373 non-vote TPS** (5,488 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.318s**.
- **677 active validators** (14 delinquent, holding 0.044% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $98.35** (+0.16% over 24h), market cap $57.68B.
- **DeFi TVL $5.71B** (-4.15% 7d, +19.19% 30d), against $15.40B of stablecoins settled on Solana.
- **$2.70B of DEX volume in 24h** across 123 protocols, generating $14.08M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | True TPS (non-vote) | 3373.3 | 1.71e+03 tx/s +/- 489 tx/s (median of last 195) | True TPS (non-vote) is 3.37e+03 tx/s, 3.4 robust standard deviations above its recent median of 1.71e+03 tx/s (+97.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1036 (10.65% complete) |
| Slot | 46,019 of 432,000 in epoch |
| Absolute slot | 447,598,019 |
| Block height | 425,639,421 |
| Lifetime transactions | 549,152,190,052 |
| TPS (now / mean / peak) | 4,799 / 5,488 / 6,501 |
| True TPS, non-vote (now / mean) | 2,653 / 3,373 |
| Slot time (mean / worst) | 0.318s / 0.328s |

Epoch 1036 has **385,981 slots remaining**, about **34h 5m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 14 (2.03% delinquent) |
| Total stake | 439,761,083 SOL |
| Delinquent stake | 191,651 SOL (0.044%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.34% |
| Commission (mean / median) | 12.36% / 5% |
| Zero-commission validators | 243 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,767,428 | 4.040% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,352,114 | 3.718% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,485,145 | 2.839% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,383,247 | 2.589% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,740,877 | 2.215% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,273 | 2.105% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,049,051 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,386,183 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,076,306 | 1.609% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,558,592 | 1.491% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `3r5ZXC1yFqMmk8VwDdUJbEdPmZ8KZvEkzd5ThEYRetTk` | 128,297 | 446,560,438 |
| `4QQqaHgJfrpaS8aU47CkmgAMimGnxiphgwhqzQrotjQU` | 35,253 | 447,484,482 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,659 | 447,595,236 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,812 | 446,874,801 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,044,285 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 807 | 447,552,761 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 197 | 445,809,612 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 89 | 446,995,996 |
| `inQRWLtWjrZYz4z9xiPH9G8oMaGqKdeSeh7DUkGPVDL` | 14 | 445,699,097 |
| `BBzWbWp6WzmoMMCKrHhcAnqSWYdFqVLyn6qNebcX44yo` | 4 | 447,440,141 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $98.35 | +0.16% 24h ↑ |
| Market cap | $57.68B | |
| Spot volume 24h | $3.33B | |
| DeFi TVL | $5.71B | -3.57% 1d / -4.15% 7d / +19.19% 30d |
| TVL 90-day peak | $6.03B | |
| Stablecoin supply (USD peg) | $15.40B | |
| Stablecoin supply (all pegs) | $15.47B | |
| DEX volume 24h | $2.70B | +6.84% 1d |
| DEX volume 7d / 30d | $18.12B / $78.48B | |
| Fees + app revenue 24h | $14.08M | +3.71% 1d |
| Circulating supply | 587,150,395 SOL (92.58% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $519.33M | 19.21% |
| BisonFi | $353.62M | 13.08% |
| HumidiFi | $232.02M | 8.58% |
| fomo Wallet | $226.51M | 8.38% |
| Raydium AMM | $199.75M | 7.39% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-16 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-09-16 |
| - | [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) | 2026-09-15 |
| - | [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) | 2026-09-14 |
| - | [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) | 2026-09-14 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-11 |
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-11 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-09-09 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-16T19:07:00Z | Change |
|---|---|---|---|
| SOL price | $107 | $98 | -8.46% |
| DeFi TVL | $5.94B | $5.71B | -3.99% |
| Stablecoin supply | $15.97B | $15.40B | -3.56% |
| DEX volume 24h | $3.63B | $2.70B | -25.57% |
| Mean TPS | 3,288 | 5,488 | +66.93% |
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
