# Solana Ecosystem Report

_Generated 2026-09-28T02:00:11Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-28T02:00:11Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.69s |
| Snapshots in history | 296 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,554 non-vote TPS** (5,044 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.270s**.
- **675 active validators** (8 delinquent, holding 0.005% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $120.71** (-0.57% over 24h), market cap $70.95B.
- **DeFi TVL $6.67B** (+7.47% 7d, +13.37% 30d), against $16.37B of stablecoins settled on Solana.
- **$1.91B of DEX volume in 24h** across 126 protocols, generating $16.22M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6669169779 | $5,916,726,321 +/- $121,774,956 (median of last 295) | DeFi TVL is $6,669,169,779, 6.2 robust standard deviations above its recent median of $5,916,726,321 (+12.7%). |
| 🟠 warning | SOL price | 120.71 | $104 +/- $5 (median of last 295) | SOL price is $121, 3.4 robust standard deviations above its recent median of $104 (+16.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1044 (39.42% complete) |
| Slot | 170,288 of 432,000 in epoch |
| Absolute slot | 451,178,288 |
| Block height | 429,217,943 |
| Lifetime transactions | 553,479,533,734 |
| TPS (now / mean / peak) | 4,393 / 5,044 / 5,867 |
| True TPS, non-vote (now / mean) | 1,913 / 2,554 |
| Slot time (mean / worst) | 0.27s / 0.286s |

Epoch 1044 has **261,712 slots remaining**, about **19h 37m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 8 (1.17% delinquent) |
| Total stake | 440,549,807 SOL |
| Delinquent stake | 23,853 SOL (0.005%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.06% / 24.46% |
| Commission (mean / median) | 12.66% / 5% |
| Zero-commission validators | 230 |

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
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,755,264 |
| `EwgQDTsgriyM3AdjnBFMMPwPs9RUFxFoGfm24XaN1dUS` | 342 | 451,007,308 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 450,875,517 |
| `E3yMAxUpeeaMBvxYyEHVEnGfZcw39zkvo8S9D3KxZu91` | 1 | 0 |
| `DtZGy3AXE8gWVvxUHJTmQqxpmnzmdKsVXwvRN6NFKvUM` | 1 | 451,155,382 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $120.71 | -0.57% 24h ↓ |
| Market cap | $70.95B | |
| Spot volume 24h | $4.15B | |
| DeFi TVL | $6.67B | -0.01% 1d / +7.47% 7d / +13.37% 30d |
| TVL 90-day peak | $6.67B | |
| Stablecoin supply (USD peg) | $16.37B | |
| Stablecoin supply (all pegs) | $16.43B | |
| DEX volume 24h | $1.91B | -11.58% 1d |
| DEX volume 7d / 30d | $17.32B / $75.81B | |
| Fees + app revenue 24h | $16.22M | -9.59% 1d |
| Circulating supply | 587,782,482 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $297.07M | 15.59% |
| Orca DEX | $284.77M | 14.94% |
| BisonFi | $251.33M | 13.19% |
| pump.fun | $210.79M | 11.06% |
| Raydium AMM | $191.08M | 10.03% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-161 | [Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) | 2026-09-28 |
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-09-27 |
| - | [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) | 2026-09-27 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-25 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-25 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-23 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-28T02:00:11Z | Change |
|---|---|---|---|
| SOL price | $107 | $121 | +12.35% |
| DeFi TVL | $5.94B | $6.67B | +12.19% |
| Stablecoin supply | $15.97B | $16.37B | +2.48% |
| DEX volume 24h | $3.63B | $1.91B | -47.53% |
| Mean TPS | 3,288 | 5,044 | +53.43% |
| Active validators | 689 | 675 | -2.03% |
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
