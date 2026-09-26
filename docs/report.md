# Solana Ecosystem Report

_Generated 2026-09-26T23:35:30Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-26T23:35:30Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.06s |
| Snapshots in history | 287 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **2,373 non-vote TPS** (4,872 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.269s**.
- **674 active validators** (13 delinquent, holding 0.171% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $121.43** (-0.47% over 24h), market cap $71.36B.
- **DeFi TVL $6.63B** (+5.16% 7d, +14.59% 30d), against $17.56B of stablecoins settled on Solana.
- **$2.61B of DEX volume in 24h** across 126 protocols, generating $15.60M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6630934099 | $5,914,728,430 +/- $114,762,614 (median of last 286) | DeFi TVL is $6,630,934,099, 6.2 robust standard deviations above its recent median of $5,914,728,430 (+12.1%). |
| 🟠 warning | Delinquent stake | 0.171 | 0.036% +/- 0.036% (median of last 286) | Delinquent stake is 0.171%, 3.8 robust standard deviations above its recent median of 0.036% (+375.0%). |
| 🟠 warning | SOL price | 121.43 | $104 +/- $5 (median of last 286) | SOL price is $121, 3.6 robust standard deviations above its recent median of $104 (+16.9%). |
| 🟠 warning | Stablecoin supply | 17559763059.22 | $15,975,438,003 +/- $369,842,547 (median of last 286) | Stablecoin supply is $17,559,763,059, 4.3 robust standard deviations above its recent median of $15,975,438,003 (+9.9%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1043 (57.37% complete) |
| Slot | 247,835 of 432,000 in epoch |
| Absolute slot | 450,823,835 |
| Block height | 428,863,566 |
| Lifetime transactions | 553,056,395,111 |
| TPS (now / mean / peak) | 4,650 / 4,872 / 5,306 |
| True TPS, non-vote (now / mean) | 2,112 / 2,373 |
| Slot time (mean / worst) | 0.269s / 0.283s |

Epoch 1043 has **184,165 slots remaining**, about **13h 45m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 13 (1.89% delinquent) |
| Total stake | 437,542,654 SOL |
| Delinquent stake | 748,045 SOL (0.171%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.08% / 24.61% |
| Commission (mean / median) | 12.92% / 5.0% |
| Zero-commission validators | 229 |

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
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,755,264 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,758 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 790 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $121.43 | -0.47% 24h ↓ |
| Market cap | $71.36B | |
| Spot volume 24h | $2.96B | |
| DeFi TVL | $6.63B | +2.25% 1d / +5.16% 7d / +14.59% 30d |
| TVL 90-day peak | $6.63B | |
| Stablecoin supply (USD peg) | $17.56B | |
| Stablecoin supply (all pegs) | $17.62B | |
| DEX volume 24h | $2.61B | +6.62% 1d |
| DEX volume 7d / 30d | $19.91B / $79.14B | |
| Fees + app revenue 24h | $15.60M | -2.38% 1d |
| Circulating supply | 587,712,282 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $425.99M | 16.30% |
| BisonFi | $327.83M | 12.55% |
| Orca DEX | $231.68M | 8.87% |
| fomo Wallet | $209.57M | 8.02% |
| Raydium AMM | $205.50M | 7.86% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-26T23:35:30Z | Change |
|---|---|---|---|
| SOL price | $107 | $121 | +13.02% |
| DeFi TVL | $5.94B | $6.63B | +11.55% |
| Stablecoin supply | $15.97B | $17.56B | +9.93% |
| DEX volume 24h | $3.63B | $2.61B | -28.06% |
| Mean TPS | 3,288 | 4,872 | +48.21% |
| Active validators | 689 | 674 | -2.18% |
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
