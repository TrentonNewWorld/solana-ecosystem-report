# Solana Ecosystem Report

_Generated 2026-11-02T07:38:11Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-02T07:38:11Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.04s |
| Snapshots in history | 563 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,184 non-vote TPS** (1,184 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **666 active validators** (28 delinquent, holding 1.011% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $94.21** (-1.26% over 24h), market cap $55.61B.
- **DeFi TVL $5.47B** (-3.90% 7d, -15.64% 30d), against $14.97B of stablecoins settled on Solana.
- **$832.67M of DEX volume in 24h** across 140 protocols, generating $8.43M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 1.011 | 0.032% +/- 0.036% (median of last 562) | Delinquent stake is 1.011%, 27.5 robust standard deviations above its recent median of 0.032% (+3059.4%). |
| 🟠 warning | Mean TPS | 1184.5 | 4.21e+03 tx/s +/- 890 tx/s (median of last 562) | Mean TPS is 1.18e+03 tx/s, 3.4 robust standard deviations below its recent median of 4.21e+03 tx/s (-71.8%). |
| 🟠 warning | Delinquent validators | 28 | 12 +/- 4.448 (median of last 562) | Delinquent validators is 28, 3.6 robust standard deviations above its recent median of 12 (+133.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1075 (3.25% complete) |
| Slot | 14,026 of 432,000 in epoch |
| Absolute slot | 464,414,026 |
| Block height | 442,435,223 |
| Lifetime transactions | 564,825,927,503 |
| TPS (now / mean / peak) | 1,163 / 1,184 / 1,443 |
| True TPS, non-vote (now / mean) | 1,163 / 1,184 |
| Slot time (mean / worst) | 0.214s / 0.221s |

Epoch 1075 has **417,974 slots remaining**, about **24h 50m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 28 (4.03% delinquent) |
| Total stake | 434,161,055 SOL |
| Delinquent stake | 4,389,585 SOL (1.011%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.70% |
| Commission (mean / median) | 12.8% / 5.0% |
| Zero-commission validators | 225 |

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
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 289 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $94.21 | -1.26% 24h ↓ |
| Market cap | $55.61B | |
| Spot volume 24h | $1.98B | |
| DeFi TVL | $5.47B | +1.13% 1d / -3.90% 7d / -15.64% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.97B | |
| Stablecoin supply (all pegs) | $15.05B | |
| DEX volume 24h | $832.67M | -12.68% 1d |
| DEX volume 7d / 30d | $11.18B / $56.15B | |
| Fees + app revenue 24h | $8.43M | +1.96% 1d |
| Circulating supply | 590,206,020 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $122.94M | 14.76% |
| Orca DEX | $112.24M | 13.48% |
| pump.fun | $103.80M | 12.47% |
| GoonFi | $73.87M | 8.87% |
| Raydium AMM | $73.33M | 8.81% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-11-02 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-10-30 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-10-30 |
| SIMD-685 | [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) | 2026-10-30 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-29 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-11-02T07:38:11Z | Change |
|---|---|---|---|
| SOL price | $107 | $94 | -12.31% |
| DeFi TVL | $5.94B | $5.47B | -8.04% |
| Stablecoin supply | $15.97B | $14.97B | -6.30% |
| DEX volume 24h | $3.63B | $832.67M | -77.07% |
| Mean TPS | 3,288 | 1,184 | -63.97% |
| Active validators | 689 | 666 | -3.34% |
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
