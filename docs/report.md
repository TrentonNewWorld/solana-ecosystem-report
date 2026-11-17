# Solana Ecosystem Report

_Generated 2026-11-17T23:49:40Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-17T23:49:40Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.67s |
| Snapshots in history | 659 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **2,020 non-vote TPS** (2,020 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.216s**.
- **660 active validators** (6 delinquent, holding 0.028% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $74.98** (+5.20% over 24h), market cap $44.36B.
- **DeFi TVL $4.72B** (-6.51% 7d, -19.66% 30d), against $13.59B of stablecoins settled on Solana.
- **$1.48B of DEX volume in 24h** across 144 protocols, generating $8.33M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 74.98 | $104 +/- $6 (median of last 651) | SOL price is $75, 4.6 robust standard deviations below its recent median of $104 (-27.7%). |
| 🟠 warning | DeFi TVL | 4724643516 | $5,899,713,868 +/- $305,221,537 (median of last 657) | DeFi TVL is $4,724,643,516, 3.8 robust standard deviations below its recent median of $5,899,713,868 (-19.9%). |
| 🟠 warning | Stablecoin supply | 13586671321.66 | $15,860,089,173 +/- $542,515,810 (median of last 658) | Stablecoin supply is $13,586,671,322, 4.2 robust standard deviations below its recent median of $15,860,089,173 (-14.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1089 (63.80% complete) |
| Slot | 275,612 of 432,000 in epoch |
| Absolute slot | 470,723,612 |
| Block height | 448,738,379 |
| Lifetime transactions | 567,174,090,027 |
| TPS (now / mean / peak) | 1,468 / 2,020 / 2,767 |
| True TPS, non-vote (now / mean) | 1,468 / 2,020 |
| Slot time (mean / worst) | 0.216s / 0.225s |

Epoch 1089 has **156,388 slots remaining**, about **9h 22m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 6 (0.90% delinquent) |
| Total stake | 428,796,576 SOL |
| Delinquent stake | 120,009 SOL (0.028%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.93% / 24.77% |
| Commission (mean / median) | 12.86% / 5.0% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,834,343 | 3.926% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,442,668 | 3.835% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,432,778 | 2.899% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,144,846 | 2.366% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,802,677 | 2.286% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,625,021 | 2.245% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,745 | 2.150% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,970,891 | 1.859% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,288 | 1.632% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,472 | 1.570% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `4QQqaHgJfrpaS8aU47CkmgAMimGnxiphgwhqzQrotjQU` | 64,655 | 470,721,023 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,516 | 469,583,999 |
| `3Z1N2Fkfha4ThNiRwN8RnU6U8dkFJ92DH2TFyLWJf8cj` | 19,833 | 470,447,999 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `GdFaSCpPf9RqRjxkvXUCzLR62bEjmEPZMS9XRVFC3pDu` | 2 | 469,698,063 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 1 | 467,356,334 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $74.98 | +5.20% 24h ↑ |
| Market cap | $44.36B | |
| Spot volume 24h | $3.24B | |
| DeFi TVL | $4.72B | +1.03% 1d / -6.51% 7d / -19.66% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.59B | |
| Stablecoin supply (all pegs) | $13.68B | |
| DEX volume 24h | $1.48B | +9.42% 1d |
| DEX volume 7d / 30d | $10.55B / $50.59B | |
| Fees + app revenue 24h | $8.33M | +16.23% 1d |
| Circulating supply | 591,739,520 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $229.99M | 15.54% |
| PumpSwap | $157.21M | 10.62% |
| Meteora DLMM | $155.76M | 10.52% |
| BisonFi | $148.83M | 10.06% |
| Raydium AMM | $138.03M | 9.33% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-17 |
| SIMD-643 | [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) _(draft)_ | 2026-11-17 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-16 |
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-14 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-14 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-17T23:49:40Z | Change |
|---|---|---|---|
| SOL price | $107 | $75 | -30.21% |
| DeFi TVL | $5.94B | $4.72B | -20.52% |
| Stablecoin supply | $15.97B | $13.59B | -14.95% |
| DEX volume 24h | $3.63B | $1.48B | -59.25% |
| Mean TPS | 3,288 | 2,020 | -38.55% |
| Active validators | 689 | 660 | -4.21% |
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
