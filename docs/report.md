# Solana Ecosystem Report

_Generated 2026-09-24T20:28:28Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-24T20:28:28Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.18s |
| Snapshots in history | 268 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,348 non-vote TPS** (4,858 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.268s**.
- **676 active validators** (10 delinquent, holding 0.009% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $116.72** (+2.28% over 24h), market cap $68.58B.
- **DeFi TVL $6.47B** (+11.81% 7d, +12.44% 30d), against $15.96B of stablecoins settled on Solana.
- **$2.55B of DEX volume in 24h** across 125 protocols, generating $16.12M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6465024760 | $5,905,894,504 +/- $91,932,654 (median of last 267) | DeFi TVL is $6,465,024,760, 6.1 robust standard deviations above its recent median of $5,905,894,504 (+9.5%). |
| 🟠 warning | SOL price | 116.72 | $104 +/- $4 (median of last 267) | SOL price is $117, 3.1 robust standard deviations above its recent median of $104 (+12.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1041 (98.34% complete) |
| Slot | 424,842 of 432,000 in epoch |
| Absolute slot | 450,136,842 |
| Block height | 428,176,864 |
| Lifetime transactions | 552,225,899,503 |
| TPS (now / mean / peak) | 5,282 / 4,858 / 5,490 |
| True TPS, non-vote (now / mean) | 2,747 / 2,348 |
| Slot time (mean / worst) | 0.268s / 0.28s |

Epoch 1041 has **7,158 slots remaining**, about **31m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 10 (1.46% delinquent) |
| Total stake | 439,964,137 SOL |
| Delinquent stake | 39,449 SOL (0.009%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.38% |
| Commission (mean / median) | 12.87% / 5.0% |
| Zero-commission validators | 233 |

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
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,371 | 447,595,236 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,015,156 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 449,904,508 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $116.72 | +2.28% 24h ↑ |
| Market cap | $68.58B | |
| Spot volume 24h | $4.34B | |
| DeFi TVL | $6.47B | -1.06% 1d / +11.81% 7d / +12.44% 30d |
| TVL 90-day peak | $6.53B | |
| Stablecoin supply (USD peg) | $15.96B | |
| Stablecoin supply (all pegs) | $16.03B | |
| DEX volume 24h | $2.55B | -20.10% 1d |
| DEX volume 7d / 30d | $20.98B / $79.47B | |
| Fees + app revenue 24h | $16.12M | -7.77% 1d |
| Circulating supply | 587,576,828 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $344.04M | 13.48% |
| BisonFi | $323.94M | 12.69% |
| Orca DEX | $318.45M | 12.47% |
| PumpSwap | $270.19M | 10.58% |
| Meteora DLMM | $233.66M | 9.15% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-24 |
| SIMD-215 | [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) | 2026-09-24 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-24 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-23 |
| SIMD-174 | [SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) | 2026-09-23 |
| - | [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) | 2026-09-23 |
| SIMD-138 | [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) | 2026-09-23 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-24T20:28:28Z | Change |
|---|---|---|---|
| SOL price | $107 | $117 | +8.64% |
| DeFi TVL | $5.94B | $6.47B | +8.75% |
| Stablecoin supply | $15.97B | $15.96B | -0.06% |
| DEX volume 24h | $3.63B | $2.55B | -29.71% |
| Mean TPS | 3,288 | 4,858 | +47.77% |
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
