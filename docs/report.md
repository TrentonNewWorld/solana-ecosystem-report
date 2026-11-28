# Solana Ecosystem Report

_Generated 2026-11-28T05:00:52Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-28T05:00:52Z` |
| Sources healthy | 8 of 8 |
| Collection time | 25.53s |
| Snapshots in history | 708 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,549 non-vote TPS** (1,549 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **655 active validators** (10 delinquent, holding 0.027% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $71.55** (-1.55% over 24h), market cap $42.39B.
- **DeFi TVL $4.61B** (+1.36% 7d, -19.02% 30d), against $13.04B of stablecoins settled on Solana.
- **$885.19M of DEX volume in 24h** across 146 protocols, generating $5.61M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 13038119792.53 | $15,774,416,846 +/- $604,421,587 (median of last 707) | Stablecoin supply is $13,038,119,793, 4.5 robust standard deviations below its recent median of $15,774,416,846 (-17.3%). |
| 🟠 warning | SOL price | 71.55 | $103 +/- $8 (median of last 700) | SOL price is $72, 3.8 robust standard deviations below its recent median of $103 (-30.7%). |
| 🟠 warning | DeFi TVL | 4611731843 | $5,888,951,836 +/- $382,636,437 (median of last 706) | DeFi TVL is $4,611,731,843, 3.3 robust standard deviations below its recent median of $5,888,951,836 (-21.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.2 |
| Current epoch | 1099 (13.79% complete) |
| Slot | 59,562 of 432,000 in epoch |
| Absolute slot | 474,827,562 |
| Block height | 452,840,066 |
| Lifetime transactions | 568,714,387,454 |
| TPS (now / mean / peak) | 1,644 / 1,549 / 2,642 |
| True TPS, non-vote (now / mean) | 1,644 / 1,549 |
| Slot time (mean / worst) | 0.215s / 0.222s |

Epoch 1099 has **372,438 slots remaining**, about **22h 14m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 655 / 10 (1.50% delinquent) |
| Total stake | 423,553,544 SOL |
| Delinquent stake | 113,578 SOL (0.027%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.94% |
| Commission (mean / median) | 13.13% / 5% |
| Zero-commission validators | 217 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,820,639 | 3.971% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,937,964 | 3.763% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,430,259 | 2.935% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,239,621 | 2.418% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,920,125 | 2.342% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,625,966 | 2.273% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,299,548 | 2.196% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,045,358 | 1.899% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,973,110 | 1.646% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,346,579 | 1.498% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 35,467 | 474,335,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,399 | 473,471,999 |
| `46mwXQRqWwj8Jp4ZR2tL1Yr3Snm99xDfKUs5jz7hLmEK` | 29,237 | 474,288,935 |
| `3Z1N2Fkfha4ThNiRwN8RnU6U8dkFJ92DH2TFyLWJf8cj` | 12,904 | 474,335,999 |
| `DqbRPQXbN8GDKWZkKiHnRjiSKPqE3rQaNgTPxdLGPDMK` | 3,090 | 473,903,999 |
| `DG6fVEB2Qy1jntvHVPui3R12CMqcwNNnjYPYdsbQ9ACP` | 2,295 | 473,749,295 |
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 125 | 472,608,648 |
| `47hzyKgoz9Fu1HP4mR48tvAFj7akCFZKGzZqWo32sNqG` | 46 | 472,988,210 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 14 | 462,239,999 |
| `8XEwA3UstYg2FJxRHagPBj2rKWZQrr5UG5x8AfuPvNPo` | 1 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $71.55 | -1.55% 24h ↓ |
| Market cap | $42.39B | |
| Spot volume 24h | $2.42B | |
| DeFi TVL | $4.61B | -0.34% 1d / +1.36% 7d / -19.02% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.04B | |
| Stablecoin supply (all pegs) | $13.12B | |
| DEX volume 24h | $885.19M | +1.68% 1d |
| DEX volume 7d / 30d | $8.32B / $45.52B | |
| Fees + app revenue 24h | $5.61M | -8.53% 1d |
| Circulating supply | 592,430,559 SOL (92.81% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $139.53M | 15.76% |
| Raydium AMM | $111.99M | 12.65% |
| pump.fun | $107.98M | 12.20% |
| PumpSwap | $86.72M | 9.80% |
| BisonFi | $81.42M | 9.20% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-26 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-26 |
| - | [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) | 2026-11-25 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-11-25 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-24 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-24 |
| SIMD-675 | [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) | 2026-11-24 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.1) | Release v4.5.0-rc.1 | 2026-11-27 |
| [`v4.4.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.2) | Release v4.4.2 | 2026-11-27 |
| [`v4.5.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | Release v4.5.0-rc.0 | 2026-11-25 |
| [`v5.0.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | Release v5.0.0-alpha.1 | 2026-11-19 |
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-28T05:00:52Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -33.40% |
| DeFi TVL | $5.94B | $4.61B | -22.42% |
| Stablecoin supply | $15.97B | $13.04B | -18.38% |
| DEX volume 24h | $3.63B | $885.19M | -75.63% |
| Mean TPS | 3,288 | 1,549 | -52.89% |
| Active validators | 689 | 655 | -4.93% |
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
