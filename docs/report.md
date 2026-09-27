# Solana Ecosystem Report

_Generated 2026-09-27T01:51:06Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-27T01:51:06Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.3s |
| Snapshots in history | 288 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **2,066 non-vote TPS** (4,562 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.269s**.
- **673 active validators** (14 delinquent, holding 0.181% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $121.08** (-0.74% over 24h), market cap $71.16B.
- **DeFi TVL $6.63B** (+7.32% 7d, +9.99% 30d), against $16.45B of stablecoins settled on Solana.
- **$2.35B of DEX volume in 24h** across 126 protocols, generating $18.30M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6628175882 | $5,915,350,799 +/- $117,037,269 (median of last 287) | DeFi TVL is $6,628,175,882, 6.1 robust standard deviations above its recent median of $5,915,350,799 (+12.1%). |
| 🟠 warning | Delinquent stake | 0.181 | 0.036% +/- 0.036% (median of last 287) | Delinquent stake is 0.181%, 4.1 robust standard deviations above its recent median of 0.036% (+402.8%). |
| 🟠 warning | SOL price | 121.08 | $104 +/- $5 (median of last 287) | SOL price is $121, 3.4 robust standard deviations above its recent median of $104 (+16.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1043 (64.39% complete) |
| Slot | 278,180 of 432,000 in epoch |
| Absolute slot | 450,854,180 |
| Block height | 428,893,907 |
| Lifetime transactions | 553,093,650,450 |
| TPS (now / mean / peak) | 4,132 / 4,562 / 5,013 |
| True TPS, non-vote (now / mean) | 1,640 / 2,066 |
| Slot time (mean / worst) | 0.269s / 0.278s |

Epoch 1043 has **153,820 slots remaining**, about **11h 29m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 14 (2.04% delinquent) |
| Total stake | 437,542,654 SOL |
| Delinquent stake | 792,432 SOL (0.181%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.08% / 24.61% |
| Commission (mean / median) | 12.94% / 5% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,860,284 | 4.082% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,799,204 | 3.611% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,343,056 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,222,561 | 2.565% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,836,562 | 2.477% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,102 | 2.111% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,182,742 | 2.099% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,606,181 | 1.738% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,093,311 | 1.621% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,506,505 | 1.487% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `Ec55BotYhWgC3xRmZ2UpuJvyySwxZeUrvEDPrxxG7r9B` | 530,431 | 450,822,629 |
| `5cwxevV9u1poNgfc1tKxMfEGX4oKt1DZNSHg48Umubm3` | 181,324 | 450,788,494 |
| `7sBYPueerpq3kKjmuimJkGr7jmiM8ZZ74pXPMEcBSxo5` | 44,386 | 450,836,424 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,755,264 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,758 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 790 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $121.08 | -0.74% 24h ↓ |
| Market cap | $71.16B | |
| Spot volume 24h | $2.90B | |
| DeFi TVL | $6.63B | -0.07% 1d / +7.32% 7d / +9.99% 30d |
| TVL 90-day peak | $6.63B | |
| Stablecoin supply (USD peg) | $16.45B | |
| Stablecoin supply (all pegs) | $16.51B | |
| DEX volume 24h | $2.35B | -10.07% 1d |
| DEX volume 7d / 30d | $18.37B / $76.71B | |
| Fees + app revenue 24h | $18.30M | +17.33% 1d |
| Circulating supply | 587,712,185 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $513.61M | 21.86% |
| BisonFi | $327.83M | 13.95% |
| Orca DEX | $231.35M | 9.84% |
| fomo Wallet | $207.12M | 8.81% |
| Raydium AMM | $189.88M | 8.08% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) | 2026-09-26 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-09-26 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-09-27T01:51:06Z | Change |
|---|---|---|---|
| SOL price | $107 | $121 | +12.70% |
| DeFi TVL | $5.94B | $6.63B | +11.50% |
| Stablecoin supply | $15.97B | $16.45B | +2.99% |
| DEX volume 24h | $3.63B | $2.35B | -35.30% |
| Mean TPS | 3,288 | 4,562 | +38.77% |
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
