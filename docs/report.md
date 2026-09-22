# Solana Ecosystem Report

_Generated 2026-09-22T08:49:15Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-22T08:49:15Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.43s |
| Snapshots in history | 247 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,571 non-vote TPS** (4,096 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **676 active validators** (13 delinquent, holding 0.928% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $117.3** (+1.21% over 24h), market cap $68.88B.
- **DeFi TVL $6.43B** (+8.57% 7d, +15.36% 30d), against $15.87B of stablecoins settled on Solana.
- **$3.37B of DEX volume in 24h** across 125 protocols, generating $18.05M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.928 | 0.036% +/- 0.037% (median of last 246) | Delinquent stake is 0.928%, 24.1 robust standard deviations above its recent median of 0.036% (+2477.8%). |
| 🔴 critical | DeFi TVL | 6425863513 | $5,898,048,908 +/- $76,635,173 (median of last 246) | DeFi TVL is $6,425,863,513, 6.9 robust standard deviations above its recent median of $5,898,048,908 (+8.9%). |
| 🟠 warning | SOL price | 117.3 | $103 +/- $4 (median of last 246) | SOL price is $117, 3.9 robust standard deviations above its recent median of $103 (+13.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1040 (11.44% complete) |
| Slot | 49,415 of 432,000 in epoch |
| Absolute slot | 449,329,415 |
| Block height | 427,369,886 |
| Lifetime transactions | 551,262,671,419 |
| TPS (now / mean / peak) | 4,276 / 4,096 / 4,772 |
| True TPS, non-vote (now / mean) | 1,778 / 1,571 |
| Slot time (mean / worst) | 0.267s / 0.279s |

Epoch 1040 has **382,585 slots remaining**, about **28h 22m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 13 (1.89% delinquent) |
| Total stake | 439,861,749 SOL |
| Delinquent stake | 4,082,171 SOL (0.928%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.05% / 24.32% |
| Commission (mean / median) | 12.39% / 5.0% |
| Zero-commission validators | 240 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,826,722 | 4.053% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,698 | 3.601% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,354,353 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,265,429 | 2.561% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,210,832 | 2.321% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,211,356 | 2.094% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,144,102 | 2.079% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,458,789 | 1.696% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,089,342 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,555,722 | 1.490% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `2tucttroqFNXsrYeMBQ8LfzKNfgwT2rHBzAF6RzbbHEp` | 3,882,420 | 449,328,878 |
| `drXsaoxWGkvjEUveMpbS1RVQmtZ7y1kb9E4YERJxCFt` | 89,154 | 0 |
| `54DYhq7YnjHgVw8fKTEtYbc7qAtctWo8bjj84BrK1199` | 71,154 | 0 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,371 | 447,595,236 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,706 | 449,084,940 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,261 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $117.3 | +1.21% 24h ↑ |
| Market cap | $68.88B | |
| Spot volume 24h | $6.62B | |
| DeFi TVL | $6.43B | +3.55% 1d / +8.57% 7d / +15.36% 30d |
| TVL 90-day peak | $6.43B | |
| Stablecoin supply (USD peg) | $15.87B | |
| Stablecoin supply (all pegs) | $15.93B | |
| DEX volume 24h | $3.37B | +20.57% 1d |
| DEX volume 7d / 30d | $19.33B / $78.36B | |
| Fees + app revenue 24h | $18.05M | +24.78% 1d |
| Circulating supply | 587,507,922 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $539.11M | 16.00% |
| Orca DEX | $430.21M | 12.76% |
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

| Metric | 2026-08-28T06:17:33Z | 2026-09-22T08:49:15Z | Change |
|---|---|---|---|
| SOL price | $107 | $117 | +9.18% |
| DeFi TVL | $5.94B | $6.43B | +8.10% |
| Stablecoin supply | $15.97B | $15.87B | -0.64% |
| DEX volume 24h | $3.63B | $3.37B | -7.21% |
| Mean TPS | 3,288 | 4,096 | +24.58% |
| Active validators | 689 | 676 | -1.89% |
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
