# Solana Ecosystem Report

_Generated 2026-09-29T23:13:19Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-29T23:13:19Z` |
| Sources healthy | 7 of 8 |
| Collection time | 10.63s |
| Snapshots in history | 308 |
| Anomalies flagged | 2 (0 critical) |

## At a glance

- The network is processing **2,319 non-vote TPS** (4,811 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.269s**.
- **672 active validators** (11 delinquent, holding 0.092% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **DeFi TVL $6.52B** (+0.98% 7d, +10.10% 30d), against $16.08B of stablecoins settled on Solana.
- **$2.66B of DEX volume in 24h** across 127 protocols, generating $17.51M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Source: market | unavailable | ok | The market source failed this run (GET https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true failed: HTTP Error 403: Forbidden); its metrics are missing from this snapshot. |
| 🟠 warning | DeFi TVL | 6522191777 | $5,924,750,516 +/- $145,886,255 (median of last 307) | DeFi TVL is $6,522,191,777, 4.1 robust standard deviations above its recent median of $5,924,750,516 (+10.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1045 (80.10% complete) |
| Slot | 346,027 of 432,000 in epoch |
| Absolute slot | 451,786,027 |
| Block height | 429,825,487 |
| Lifetime transactions | 554,211,444,589 |
| TPS (now / mean / peak) | 5,037 / 4,811 / 5,339 |
| True TPS, non-vote (now / mean) | 2,513 / 2,319 |
| Slot time (mean / worst) | 0.269s / 0.278s |

Epoch 1045 has **85,973 slots remaining**, about **6h 25m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 11 (1.61% delinquent) |
| Total stake | 441,249,792 SOL |
| Delinquent stake | 406,454 SOL (0.092%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.45% |
| Commission (mean / median) | 12.84% / 5.0% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.040% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.796% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.561% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.540% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.731% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.518% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.477% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FN2BJjzy7WMRAqMNwzZrv5iDmHaNwukyFMfWCc6FxZDw` | 169,459 | 451,736,367 |
| `NikGQUQqSLtsdHGGx7mQopojZcgd3N9uWFaZQ1r5EXn` | 81,783 | 451,647,060 |
| `ViKLknQuks11DLEjZ7Y2aNYAAT7Q3NTKLGxs8rdnLVi` | 74,223 | 451,647,273 |
| `6hcGvZypizjf6PPsxboshZHRqefyQKSG9L8vZqYdm7UY` | 57,478 | 451,784,699 |
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 451,520,406 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 451,518,013 |
| `DtZGy3AXE8gWVvxUHJTmQqxpmnzmdKsVXwvRN6NFKvUM` | 1 | 451,719,791 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $n/a | n/a 24h |
| Market cap | n/a | |
| Spot volume 24h | n/a | |
| DeFi TVL | $6.52B | -1.76% 1d / +0.98% 7d / +10.10% 30d |
| TVL 90-day peak | $6.64B | |
| Stablecoin supply (USD peg) | $16.08B | |
| Stablecoin supply (all pegs) | $16.14B | |
| DEX volume 24h | $2.66B | +38.18% 1d |
| DEX volume 7d / 30d | $17.56B / $77.77B | |
| Fees + app revenue 24h | $17.51M | +13.56% 1d |
| Circulating supply | 587,851,325 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $381.95M | 14.35% |
| Orca DEX | $367.17M | 13.79% |
| Raydium AMM | $291.52M | 10.95% |
| PumpSwap | $268.39M | 10.08% |
| Meteora DLMM | $205.60M | 7.72% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-29 |
| SIMD-511 | [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-09-29 |
| SIMD-630 | [SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-29 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-09-29 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) _(draft)_ | 2026-09-29 |
| SIMD-503 | [SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) | 2026-09-29 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-28 |
| SIMD-161 | [Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) | 2026-09-28 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | Release v4.4.0-beta.0 | 2026-09-28 |
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |
| [`v4.3.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | Release v4.3.0 | 2026-09-18 |
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-29T23:13:19Z | Change |
|---|---|---|---|
| DeFi TVL | $5.94B | $6.52B | +9.72% |
| Stablecoin supply | $15.97B | $16.08B | +0.68% |
| DEX volume 24h | $3.63B | $2.66B | -26.71% |
| Mean TPS | 3,288 | 4,811 | +46.33% |
| Active validators | 689 | 672 | -2.47% |
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
