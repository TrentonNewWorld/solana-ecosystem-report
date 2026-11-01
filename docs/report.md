# Solana Ecosystem Report

_Generated 2026-11-01T17:14:59Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-01T17:14:59Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.59s |
| Snapshots in history | 558 |
| Anomalies flagged | 2 (2 critical) |

## At a glance

- The network is processing **1,828 non-vote TPS** (1,828 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **662 active validators** (34 delinquent, holding 1.050% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $94.7** (-1.19% over 24h), market cap $55.81B.
- **DeFi TVL $5.39B** (-6.39% 7d, -16.43% 30d), against $15.07B of stablecoins settled on Solana.
- **$953.37M of DEX volume in 24h** across 139 protocols, generating $8.27M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 1.05 | 0.032% +/- 0.036% (median of last 557) | Delinquent stake is 1.050%, 28.6 robust standard deviations above its recent median of 0.032% (+3181.2%). |
| 🔴 critical | Delinquent validators | 34 | 12 +/- 4.448 (median of last 557) | Delinquent validators is 34, 4.9 robust standard deviations above its recent median of 12 (+183.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1074 (47.30% complete) |
| Slot | 204,324 of 432,000 in epoch |
| Absolute slot | 464,172,324 |
| Block height | 442,193,790 |
| Lifetime transactions | 564,737,375,103 |
| TPS (now / mean / peak) | 1,450 / 1,828 / 2,320 |
| True TPS, non-vote (now / mean) | 1,450 / 1,828 |
| Slot time (mean / worst) | 0.214s / 0.221s |

Epoch 1074 has **227,676 slots remaining**, about **13h 32m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 34 (4.89% delinquent) |
| Total stake | 433,943,288 SOL |
| Delinquent stake | 4,555,855 SOL (1.050%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.69% |
| Commission (mean / median) | 12.82% / 5.0% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,029,196 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,695,127 | 3.847% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,943,199 | 2.983% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,426,987 | 2.403% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,583,157 | 2.208% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,451,197 | 2.178% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,053 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,791,639 | 1.796% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,293 | 1.613% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,977,108 | 1.608% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `JEJzKYzyYJJjtn6Yb1P7r6YV75TdSNmmJT49sgDoHvmk` | 1,838,200 | 463,967,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,346,016 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,225 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 250,453 | 462,239,999 |
| `7K8DVxtNJGnMtUY1CQJT5jcs8sFGSZTDiG7kowvFpECh` | 145,759 | 463,535,999 |
| `5K8qgC9nHzKHSSyo9fKLsMfYmavYdMgEaYx86cMmVKVv` | 96,624 | 463,967,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 62,325 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 16,589 | 463,967,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 2,688 | 464,160,502 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $94.7 | -1.19% 24h ↓ |
| Market cap | $55.81B | |
| Spot volume 24h | $1.34B | |
| DeFi TVL | $5.39B | -1.07% 1d / -6.39% 7d / -16.43% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.07B | |
| Stablecoin supply (all pegs) | $15.15B | |
| DEX volume 24h | $953.37M | -54.97% 1d |
| DEX volume 7d / 30d | $12.20B / $58.48B | |
| Fees + app revenue 24h | $8.27M | -26.39% 1d |
| Circulating supply | 590,150,367 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $130.68M | 13.71% |
| pump.fun | $103.80M | 10.89% |
| Orca DEX | $86.53M | 9.08% |
| GoonFi | $73.87M | 7.75% |
| Tessera V | $70.33M | 7.38% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-529 | [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) | 2026-10-31 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-11-01T17:14:59Z | Change |
|---|---|---|---|
| SOL price | $107 | $95 | -11.86% |
| DeFi TVL | $5.94B | $5.39B | -9.30% |
| Stablecoin supply | $15.97B | $15.07B | -5.66% |
| DEX volume 24h | $3.63B | $953.37M | -73.75% |
| Mean TPS | 3,288 | 1,828 | -44.39% |
| Active validators | 689 | 662 | -3.92% |
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
