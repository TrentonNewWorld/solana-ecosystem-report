# Solana Ecosystem Report

_Generated 2026-09-27T14:40:39Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-27T14:40:39Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.7s |
| Snapshots in history | 291 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,063 non-vote TPS** (4,565 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.269s**.
- **673 active validators** (10 delinquent, holding 0.009% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $121.74** (+0.72% over 24h), market cap $71.57B.
- **DeFi TVL $6.73B** (+9.04% 7d, +11.76% 30d), against $16.43B of stablecoins settled on Solana.
- **$2.16B of DEX volume in 24h** across 126 protocols, generating $17.93M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6734873532 | $5,915,721,416 +/- $119,609,426 (median of last 290) | DeFi TVL is $6,734,873,532, 6.8 robust standard deviations above its recent median of $5,915,721,416 (+13.8%). |
| 🟠 warning | SOL price | 121.74 | $104 +/- $5 (median of last 290) | SOL price is $122, 3.6 robust standard deviations above its recent median of $104 (+17.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1044 (4.29% complete) |
| Slot | 18,551 of 432,000 in epoch |
| Absolute slot | 451,026,551 |
| Block height | 429,066,254 |
| Lifetime transactions | 553,290,311,576 |
| TPS (now / mean / peak) | 4,488 / 4,565 / 5,068 |
| True TPS, non-vote (now / mean) | 1,926 / 2,063 |
| Slot time (mean / worst) | 0.269s / 0.279s |

Epoch 1044 has **413,449 slots remaining**, about **30h 53m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 10 (1.46% delinquent) |
| Total stake | 440,549,807 SOL |
| Delinquent stake | 38,225 SOL (0.009%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.46% |
| Commission (mean / median) | 12.55% / 5% |
| Zero-commission validators | 229 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,867,779 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,792 | 3.596% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,570 | 2.799% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,215,732 | 2.546% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,838,730 | 2.460% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,238,854 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,209,776 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,623,407 | 1.730% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,094,526 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,511,334 | 1.478% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `B38JgkTi7Fu2Uxk8JzNw4M7aMhVxzGu2fsRqHNScPkCQ` | 14,326 | 451,026,443 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,755,264 |
| `EwgQDTsgriyM3AdjnBFMMPwPs9RUFxFoGfm24XaN1dUS` | 342 | 451,007,308 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 46 | 451,025,703 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 450,875,517 |
| `E3yMAxUpeeaMBvxYyEHVEnGfZcw39zkvo8S9D3KxZu91` | 1 | 0 |
| `DtZGy3AXE8gWVvxUHJTmQqxpmnzmdKsVXwvRN6NFKvUM` | 1 | 450,994,445 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $121.74 | +0.72% 24h ↑ |
| Market cap | $71.57B | |
| Spot volume 24h | $3.69B | |
| DeFi TVL | $6.73B | +1.50% 1d / +9.04% 7d / +11.76% 30d |
| TVL 90-day peak | $6.73B | |
| Stablecoin supply (USD peg) | $16.43B | |
| Stablecoin supply (all pegs) | $16.49B | |
| DEX volume 24h | $2.16B | -17.52% 1d |
| DEX volume 7d / 30d | $19.19B / $77.53B | |
| Fees + app revenue 24h | $17.93M | +18.95% 1d |
| Circulating supply | 587,783,179 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $513.61M | 23.83% |
| BisonFi | $251.33M | 11.66% |
| pump.fun | $210.79M | 9.78% |
| Orca DEX | $203.45M | 9.44% |
| Raydium AMM | $176.60M | 8.19% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) | 2026-09-27 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-09-27 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-25 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-25 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-23 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-09-27T14:40:39Z | Change |
|---|---|---|---|
| SOL price | $107 | $122 | +13.31% |
| DeFi TVL | $5.94B | $6.73B | +13.29% |
| Stablecoin supply | $15.97B | $16.43B | +2.87% |
| DEX volume 24h | $3.63B | $2.16B | -40.66% |
| Mean TPS | 3,288 | 4,565 | +38.84% |
| Active validators | 689 | 673 | -2.32% |
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
