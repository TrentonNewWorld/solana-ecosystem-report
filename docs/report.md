# Solana Ecosystem Report

_Generated 2026-09-22T01:54:44Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-22T01:54:44Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.06s |
| Snapshots in history | 245 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,152 non-vote TPS** (4,669 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.268s**.
- **677 active validators** (14 delinquent, holding 0.045% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $117.53** (+5.67% over 24h), market cap $69.02B.
- **DeFi TVL $6.48B** (+9.51% 7d, +16.37% 30d), against $16.81B of stablecoins settled on Solana.
- **$3.37B of DEX volume in 24h** across 125 protocols, generating $17.59M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6481778262 | $5,897,971,342 +/- $74,641,434 (median of last 244) | DeFi TVL is $6,481,778,262, 7.8 robust standard deviations above its recent median of $5,897,971,342 (+9.9%). |
| 🟠 warning | SOL price | 117.53 | $103 +/- $3 (median of last 244) | SOL price is $118, 4.1 robust standard deviations above its recent median of $103 (+13.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1039 (89.86% complete) |
| Slot | 388,175 of 432,000 in epoch |
| Absolute slot | 449,236,175 |
| Block height | 427,276,705 |
| Lifetime transactions | 551,157,166,187 |
| TPS (now / mean / peak) | 4,291 / 4,669 / 5,410 |
| True TPS, non-vote (now / mean) | 1,762 / 2,152 |
| Slot time (mean / worst) | 0.268s / 0.284s |

Epoch 1039 has **43,825 slots remaining**, about **3h 15m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 14 (2.03% delinquent) |
| Total stake | 439,905,519 SOL |
| Delinquent stake | 200,027 SOL (0.045%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.26% |
| Commission (mean / median) | 12.67% / 5% |
| Zero-commission validators | 239 |

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
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,813 | 449,084,940 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,261 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 65 | 446,995,996 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $117.53 | +5.67% 24h ↑ |
| Market cap | $69.02B | |
| Spot volume 24h | $6.60B | |
| DeFi TVL | $6.48B | +1.79% 1d / +9.51% 7d / +16.37% 30d |
| TVL 90-day peak | $6.48B | |
| Stablecoin supply (USD peg) | $16.81B | |
| Stablecoin supply (all pegs) | $16.87B | |
| DEX volume 24h | $3.37B | +20.57% 1d |
| DEX volume 7d / 30d | $19.33B / $78.36B | |
| Fees + app revenue 24h | $17.59M | +21.60% 1d |
| Circulating supply | 587,436,777 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $577.99M | 17.15% |
| Orca DEX | $444.69M | 13.19% |
| BisonFi | $424.26M | 12.59% |
| PumpSwap | $390.12M | 11.58% |
| Meteora DLMM | $259.61M | 7.70% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-558 | [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) | 2026-09-22 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-21 |
| SIMD-558 | [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) | 2026-09-21 |
| SIMD-649 | [SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) | 2026-09-21 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-21 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-21 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-20 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-09-19 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-22T01:54:44Z | Change |
|---|---|---|---|
| SOL price | $107 | $118 | +9.39% |
| DeFi TVL | $5.94B | $6.48B | +9.04% |
| Stablecoin supply | $15.97B | $16.81B | +5.25% |
| DEX volume 24h | $3.63B | $3.37B | -7.21% |
| Mean TPS | 3,288 | 4,669 | +42.03% |
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
