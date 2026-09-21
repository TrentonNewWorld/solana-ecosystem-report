# Solana Ecosystem Report

_Generated 2026-09-21T09:18:52Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-21T09:18:52Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.91s |
| Snapshots in history | 239 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,786 non-vote TPS** (4,312 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **677 active validators** (13 delinquent, holding 0.043% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $115.3** (+6.57% over 24h), market cap $67.73B.
- **DeFi TVL $6.27B** (+7.50% 7d, +12.74% 30d), against $15.57B of stablecoins settled on Solana.
- **$2.75B of DEX volume in 24h** across 124 protocols, generating $14.38M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6273478361 | $5,896,827,392 +/- $70,843,330 (median of last 238) | DeFi TVL is $6,273,478,361, 5.3 robust standard deviations above its recent median of $5,896,827,392 (+6.4%). |
| 🟠 warning | SOL price | 115.3 | $103 +/- $3 (median of last 238) | SOL price is $115, 3.6 robust standard deviations above its recent median of $103 (+11.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1039 (38.13% complete) |
| Slot | 164,716 of 432,000 in epoch |
| Absolute slot | 449,012,716 |
| Block height | 427,053,353 |
| Lifetime transactions | 550,874,026,627 |
| TPS (now / mean / peak) | 4,048 / 4,312 / 6,029 |
| True TPS, non-vote (now / mean) | 1,499 / 1,786 |
| Slot time (mean / worst) | 0.267s / 0.279s |

Epoch 1039 has **267,284 slots remaining**, about **19h 49m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 13 (1.88% delinquent) |
| Total stake | 439,905,519 SOL |
| Delinquent stake | 189,214 SOL (0.043%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.26% |
| Commission (mean / median) | 12.23% / 5% |
| Zero-commission validators | 242 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,856,583 | 4.059% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,828,384 | 3.598% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,518,302 | 2.846% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,252,588 | 2.558% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,788,818 | 2.225% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,354 | 2.103% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,106,985 | 2.070% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,443,840 | 1.692% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,088,079 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,572,007 | 1.494% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `drXsaoxWGkvjEUveMpbS1RVQmtZ7y1kb9E4YERJxCFt` | 89,154 | 0 |
| `54DYhq7YnjHgVw8fKTEtYbc7qAtctWo8bjj84BrK1199` | 71,154 | 0 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,477 | 447,595,236 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,261 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 65 | 446,995,996 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 448,933,340 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $115.3 | +6.57% 24h ↑ |
| Market cap | $67.73B | |
| Spot volume 24h | $4.19B | |
| DeFi TVL | $6.27B | +1.57% 1d / +7.50% 7d / +12.74% 30d |
| TVL 90-day peak | $6.31B | |
| Stablecoin supply (USD peg) | $15.57B | |
| Stablecoin supply (all pegs) | $15.63B | |
| DEX volume 24h | $2.75B | -4.35% 1d |
| DEX volume 7d / 30d | $18.49B / $78.76B | |
| Fees + app revenue 24h | $14.38M | -5.91% 1d |
| Circulating supply | 587,437,519 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $482.79M | 17.55% |
| BisonFi | $386.77M | 14.06% |
| Raydium AMM | $327.63M | 11.91% |
| Orca DEX | $301.58M | 10.96% |
| HumidiFi | $228.88M | 8.32% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-20 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-09-19 |
| - | [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) | 2026-09-19 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-18 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-18 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-18 |
| SIMD-558 | [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) | 2026-09-18 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-17 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |
| [`v4.3.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | Release v4.3.0 | 2026-09-18 |
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-21T09:18:52Z | Change |
|---|---|---|---|
| SOL price | $107 | $115 | +7.32% |
| DeFi TVL | $5.94B | $6.27B | +5.53% |
| Stablecoin supply | $15.97B | $15.57B | -2.54% |
| DEX volume 24h | $3.63B | $2.75B | -24.26% |
| Mean TPS | 3,288 | 4,312 | +31.15% |
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
