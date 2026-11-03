# Solana Ecosystem Report

_Generated 2026-11-03T04:03:22Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-03T04:03:22Z` |
| Sources healthy | 5 of 8 |
| Collection time | 319.73s |
| Snapshots in history | 568 |
| Anomalies flagged | 5 (1 critical) |

## At a glance

- The network is processing **1,610 non-vote TPS** (1,610 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **665 active validators** (28 delinquent, holding 1.011% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $92.03** (-3.67% over 24h), market cap $54.32B.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 1.011 | 0.033% +/- 0.037% (median of last 567) | Delinquent stake is 1.011%, 26.4 robust standard deviations above its recent median of 0.033% (+2963.6%). |
| 🟠 warning | Source: tvl | unavailable | ok | The tvl source failed this run (GET https://api.llama.fi/v2/historicalChainTvl/Solana failed: The read operation timed out); its metrics are missing from this snapshot. |
| 🟠 warning | Source: dex | unavailable | ok | The dex source failed this run (GET https://api.llama.fi/overview/dexs/solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true failed: The read operation timed out); its metrics are missing from this snapshot. |
| 🟠 warning | Source: fees | unavailable | ok | The fees source failed this run (GET https://api.llama.fi/overview/fees/solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true failed: The read operation timed out); its metrics are missing from this snapshot. |
| 🟠 warning | Delinquent validators | 28 | 12 +/- 4.448 (median of last 567) | Delinquent validators is 28, 3.6 robust standard deviations above its recent median of 12 (+133.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1075 (82.67% complete) |
| Slot | 357,117 of 432,000 in epoch |
| Absolute slot | 464,757,117 |
| Block height | 442,778,191 |
| Lifetime transactions | 564,960,299,960 |
| TPS (now / mean / peak) | 1,512 / 1,610 / 2,074 |
| True TPS, non-vote (now / mean) | 1,512 / 1,610 |
| Slot time (mean / worst) | 0.214s / 0.219s |

Epoch 1075 has **74,883 slots remaining**, about **4h 27m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 28 (4.04% delinquent) |
| Total stake | 434,160,766 SOL |
| Delinquent stake | 4,389,297 SOL (1.011%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.70% |
| Commission (mean / median) | 12.82% / 5% |
| Zero-commission validators | 224 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,034,354 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,199 | 3.849% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,037,180 | 3.003% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,429,501 | 2.402% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,109 | 2.207% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,453,055 | 2.177% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,805 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,803,392 | 1.797% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,891 | 1.613% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,978,080 | 1.607% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `JEJzKYzyYJJjtn6Yb1P7r6YV75TdSNmmJT49sgDoHvmk` | 1,837,836 | 463,967,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,325,703 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,192 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 250,452 | 462,239,999 |
| `5K8qgC9nHzKHSSyo9fKLsMfYmavYdMgEaYx86cMmVKVv` | 96,831 | 463,967,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 62,325 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 16,587 | 463,967,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 2,688 | 464,160,502 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $92.03 | -3.67% 24h ↓ |
| Market cap | $54.32B | |
| Spot volume 24h | $2.56B | |
| DeFi TVL | n/a | n/a 1d / n/a 7d / n/a 30d |
| TVL 90-day peak | n/a | |
| Stablecoin supply (USD peg) | $15.00B | |
| Stablecoin supply (all pegs) | $15.09B | |
| DEX volume 24h | n/a | n/a 1d |
| DEX volume 7d / 30d | n/a / n/a | |
| Fees + app revenue 24h | n/a | n/a 1d |
| Circulating supply | 590,206,253 SOL (92.67% of total) |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-02 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-11-02 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-02 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-02 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-11-02 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-10-29 |
| SIMD-706 | [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-10-28 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-10-27 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |
| [`v4.4.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | Release v4.4.0-beta.1 | 2026-10-13 |
| [`v4.5.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | Release v4.5.0-alpha.2 | 2026-10-08 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-03T04:03:22Z | Change |
|---|---|---|---|
| SOL price | $107 | $92 | -14.34% |
| Stablecoin supply | $15.97B | $15.00B | -6.07% |
| Mean TPS | 3,288 | 1,610 | -51.03% |
| Active validators | 689 | 665 | -3.48% |
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
