# Solana Ecosystem Report

_Generated 2026-11-01T02:38:32Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-01T02:38:32Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.51s |
| Snapshots in history | 554 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,467 non-vote TPS** (1,467 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.213s**.
- **665 active validators** (27 delinquent, holding 0.847% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $95.34** (-1.45% over 24h), market cap $56.72B.
- **DeFi TVL $5.41B** (-6.01% 7d, -16.09% 30d), against $15.16B of stablecoins settled on Solana.
- **$1.44B of DEX volume in 24h** across 139 protocols, generating $8.59M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.847 | 0.032% +/- 0.034% (median of last 553) | Delinquent stake is 0.847%, 23.9 robust standard deviations above its recent median of 0.032% (+2546.9%). |
| 🟠 warning | Mean TPS | 1467.1 | 4.24e+03 tx/s +/- 841 tx/s (median of last 553) | Mean TPS is 1.47e+03 tx/s, 3.3 robust standard deviations below its recent median of 4.24e+03 tx/s (-65.4%). |
| 🟠 warning | Delinquent validators | 27 | 12 +/- 4.448 (median of last 553) | Delinquent validators is 27, 3.4 robust standard deviations above its recent median of 12 (+125.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1073 (90.46% complete) |
| Slot | 390,777 of 432,000 in epoch |
| Absolute slot | 463,926,777 |
| Block height | 441,948,551 |
| Lifetime transactions | 564,669,677,191 |
| TPS (now / mean / peak) | 1,103 / 1,467 / 2,229 |
| True TPS, non-vote (now / mean) | 1,103 / 1,467 |
| Slot time (mean / worst) | 0.213s / 0.219s |

Epoch 1073 has **41,223 slots remaining**, about **2h 26m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 27 (3.90% delinquent) |
| Total stake | 433,649,347 SOL |
| Delinquent stake | 3,674,724 SOL (0.847%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.71% |
| Commission (mean / median) | 13.07% / 5% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,020,574 | 3.925% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,688,715 | 3.848% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,931,864 | 2.982% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,425,467 | 2.404% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,651,671 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,449,481 | 2.179% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,227,526 | 2.128% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,778,595 | 1.794% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,000,338 | 1.614% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,976,145 | 1.609% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,402,904 | 462,239,999 |
| `HEYbDQwzZxSBSLaV7fpep3oUP8iCEch2265xzgWPW2pQ` | 1,008,724 | 463,535,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,258 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 250,453 | 462,239,999 |
| `7K8DVxtNJGnMtUY1CQJT5jcs8sFGSZTDiG7kowvFpECh` | 153,071 | 463,535,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 62,325 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,613 | 461,807,999 |
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 289 | 0 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $95.34 | -1.45% 24h ↓ |
| Market cap | $56.72B | |
| Spot volume 24h | $1.55B | |
| DeFi TVL | $5.41B | -0.42% 1d / -6.01% 7d / -16.09% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.16B | |
| Stablecoin supply (all pegs) | $15.24B | |
| DEX volume 24h | $1.44B | -31.85% 1d |
| DEX volume 7d / 30d | $11.80B / $58.08B | |
| Fees + app revenue 24h | $8.59M | -23.57% 1d |
| Circulating supply | 590,094,911 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $182.87M | 12.67% |
| Tessera V | $181.44M | 12.57% |
| PumpSwap | $130.68M | 9.06% |
| Orca DEX | $117.74M | 8.16% |
| pump.fun | $113.64M | 7.88% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-567 | [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) | 2026-10-31 |
| SIMD-529 | [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) | 2026-10-31 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-10-30 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-10-30 |
| SIMD-685 | [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) | 2026-10-30 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-29 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-10-29 |
| SIMD-706 | [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-10-28 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-01T02:38:32Z | Change |
|---|---|---|---|
| SOL price | $107 | $95 | -11.26% |
| DeFi TVL | $5.94B | $5.41B | -8.93% |
| Stablecoin supply | $15.97B | $15.16B | -5.12% |
| DEX volume 24h | $3.63B | $1.44B | -60.27% |
| Mean TPS | 3,288 | 1,467 | -55.37% |
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
