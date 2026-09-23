# Solana Ecosystem Report

_Generated 2026-09-23T14:12:54Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-23T14:12:54Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.6s |
| Snapshots in history | 257 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,054 non-vote TPS** (4,583 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.266s**.
- **676 active validators** (11 delinquent, holding 0.051% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $115.49** (-1.86% over 24h), market cap $68.04B.
- **DeFi TVL $6.49B** (+13.35% 7d, +16.41% 30d), against $15.86B of stablecoins settled on Solana.
- **$3.20B of DEX volume in 24h** across 125 protocols, generating $17.78M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6488668295 | $5,899,896,424 +/- $82,854,428 (median of last 256) | DeFi TVL is $6,488,668,295, 7.1 robust standard deviations above its recent median of $5,899,896,424 (+10.0%). |
| 🟠 warning | SOL price | 115.49 | $103 +/- $4 (median of last 256) | SOL price is $115, 3.3 robust standard deviations above its recent median of $103 (+11.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1041 (3.48% complete) |
| Slot | 15,035 of 432,000 in epoch |
| Absolute slot | 449,727,035 |
| Block height | 427,767,274 |
| Lifetime transactions | 551,726,854,184 |
| TPS (now / mean / peak) | 6,105 / 4,583 / 6,105 |
| True TPS, non-vote (now / mean) | 3,571 / 2,054 |
| Slot time (mean / worst) | 0.266s / 0.273s |

Epoch 1041 has **416,965 slots remaining**, about **30h 48m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 11 (1.60% delinquent) |
| Total stake | 439,964,137 SOL |
| Delinquent stake | 225,920 SOL (0.051%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.38% |
| Commission (mean / median) | 12.29% / 5.0% |
| Zero-commission validators | 237 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.560% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.349% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.082% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.728% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.490% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `drXsaoxWGkvjEUveMpbS1RVQmtZ7y1kb9E4YERJxCFt` | 89,154 | 0 |
| `54DYhq7YnjHgVw8fKTEtYbc7qAtctWo8bjj84BrK1199` | 71,154 | 0 |
| `EwgQDTsgriyM3AdjnBFMMPwPs9RUFxFoGfm24XaN1dUS` | 36,931 | 449,713,930 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,371 | 447,595,236 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $115.49 | -1.86% 24h ↓ |
| Market cap | $68.04B | |
| Spot volume 24h | $4.48B | |
| DeFi TVL | $6.49B | +0.46% 1d / +13.35% 7d / +16.41% 30d |
| TVL 90-day peak | $6.49B | |
| Stablecoin supply (USD peg) | $15.86B | |
| Stablecoin supply (all pegs) | $15.92B | |
| DEX volume 24h | $3.20B | -6.82% 1d |
| DEX volume 7d / 30d | $21.22B / $79.96B | |
| Fees + app revenue 24h | $17.78M | -4.61% 1d |
| Circulating supply | 587,578,258 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $634.15M | 19.85% |
| Raydium AMM | $371.49M | 11.63% |
| BisonFi | $368.17M | 11.52% |
| Orca DEX | $327.86M | 10.26% |
| Meteora DLMM | $266.83M | 8.35% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) | 2026-09-23 |
| SIMD-215 | [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) | 2026-09-23 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-23 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-23 |
| - | [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) | 2026-09-23 |
| SIMD-174 | [SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) | 2026-09-23 |
| SIMD-649 | [SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) | 2026-09-23 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-23T14:12:54Z | Change |
|---|---|---|---|
| SOL price | $107 | $115 | +7.49% |
| DeFi TVL | $5.94B | $6.49B | +9.15% |
| Stablecoin supply | $15.97B | $15.86B | -0.71% |
| DEX volume 24h | $3.63B | $3.20B | -12.03% |
| Mean TPS | 3,288 | 4,583 | +39.40% |
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
