# Solana Ecosystem Report

_Generated 2026-10-05T10:52:27Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-05T10:52:27Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.86s |
| Snapshots in history | 349 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,450 non-vote TPS** (3,946 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **671 active validators** (15 delinquent, holding 0.027% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $120.72** (-0.58% over 24h), market cap $71.01B.
- **DeFi TVL $6.73B** (+1.36% 7d, +14.53% 30d), against $8.47B of stablecoins settled on Solana.
- **$1.66B of DEX volume in 24h** across 126 protocols, generating $15.99M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 8471261374.17 | $16,069,261,043 +/- $350,577,914 (median of last 348) | Stablecoin supply is $8,471,261,374, 21.7 robust standard deviations below its recent median of $16,069,261,043 (-47.3%). |
| 🟠 warning | DeFi TVL | 6725134724 | $5,942,744,214 +/- $227,896,947 (median of last 348) | DeFi TVL is $6,725,134,724, 3.4 robust standard deviations above its recent median of $5,942,744,214 (+13.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1049 (90.21% complete) |
| Slot | 389,719 of 432,000 in epoch |
| Absolute slot | 453,557,719 |
| Block height | 431,595,835 |
| Lifetime transactions | 556,318,182,486 |
| TPS (now / mean / peak) | 3,961 / 3,946 / 4,320 |
| True TPS, non-vote (now / mean) | 1,476 / 1,450 |
| Slot time (mean / worst) | 0.267s / 0.273s |

Epoch 1049 has **42,281 slots remaining**, about **3h 8m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 15 (2.19% delinquent) |
| Total stake | 441,848,823 SOL |
| Delinquent stake | 120,245 SOL (0.027%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.56% |
| Commission (mean / median) | 13.0% / 5% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,935,562 | 4.059% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,927,649 | 3.605% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,346,574 | 2.794% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,305,935 | 2.559% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,136,537 | 2.520% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,655 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,241,331 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,616,097 | 1.724% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,061,519 | 1.598% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,686,111 | 1.513% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `3jkJVgfz1zrHSy6YLK6g96eTj49kCnDj2i8AbbKLZhkk` | 63,849 | 453,020,473 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 29,392 | 452,980,806 |
| `ACCRENAtboR1MyyoiPvwNZNkjt1GcLARrACh6hZXdddF` | 14,006 | 451,953,922 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,704 | 452,491,297 |
| `NikGQUQqSLtsdHGGx7mQopojZcgd3N9uWFaZQ1r5EXn` | 1,298 | 451,647,060 |
| `6hcGvZypizjf6PPsxboshZHRqefyQKSG9L8vZqYdm7UY` | 640 | 451,830,270 |
| `ViKLknQuks11DLEjZ7Y2aNYAAT7Q3NTKLGxs8rdnLVi` | 284 | 451,647,273 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 63 | 450,345,071 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 453,457,146 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $120.72 | -0.58% 24h ↓ |
| Market cap | $71.01B | |
| Spot volume 24h | $2.49B | |
| DeFi TVL | $6.73B | +1.70% 1d / +1.36% 7d / +14.53% 30d |
| TVL 90-day peak | $6.73B | |
| Stablecoin supply (USD peg) | $8.47B | |
| Stablecoin supply (all pegs) | $8.53B | |
| DEX volume 24h | $1.66B | +6.76% 1d |
| DEX volume 7d / 30d | $15.99B / $77.49B | |
| Fees + app revenue 24h | $15.99M | +23.64% 1d |
| Circulating supply | 588,313,830 SOL (92.61% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $397.81M | 23.98% |
| Orca DEX | $246.33M | 14.85% |
| pump.fun | $184.20M | 11.10% |
| BisonFi | $171.40M | 10.33% |
| fomo Wallet | $152.15M | 9.17% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-685 | [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) | 2026-10-05 |
| SIMD-683 | [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) | 2026-10-05 |
| SIMD-677 | [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) | 2026-10-05 |
| SIMD-684 | [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) | 2026-10-05 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-10-05 |
| SIMD-464 | [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) | 2026-10-05 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-10-05 |
| SIMD-503 | [SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) | 2026-10-05 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | Release v4.5.0-alpha.1 | 2026-10-03 |
| [`v4.4.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | Release v4.4.0-beta.0 | 2026-09-28 |
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |
| [`v4.3.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | Release v4.3.0 | 2026-09-18 |
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-10-05T10:52:27Z | Change |
|---|---|---|---|
| SOL price | $107 | $121 | +12.36% |
| DeFi TVL | $5.94B | $6.73B | +13.13% |
| Stablecoin supply | $15.97B | $8.47B | -46.97% |
| DEX volume 24h | $3.63B | $1.66B | -54.32% |
| Mean TPS | 3,288 | 3,946 | +20.04% |
| Active validators | 689 | 671 | -2.61% |
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
