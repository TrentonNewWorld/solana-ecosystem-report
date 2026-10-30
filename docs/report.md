# Solana Ecosystem Report

_Generated 2026-10-30T23:16:15Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-30T23:16:15Z` |
| Sources healthy | 8 of 8 |
| Collection time | 11.07s |
| Snapshots in history | 545 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,609 non-vote TPS** (1,609 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **666 active validators** (25 delinquent, holding 0.642% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $95.86** (-0.61% over 24h), market cap $56.56B.
- **DeFi TVL $5.40B** (-7.58% 7d, -16.42% 30d), against $15.16B of stablecoins settled on Solana.
- **$2.30B of DEX volume in 24h** across 139 protocols, generating $12.33M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.642 | 0.032% +/- 0.034% (median of last 544) | Delinquent stake is 0.642%, 17.9 robust standard deviations above its recent median of 0.032% (+1906.2%). |
| 🟠 warning | Mean TPS | 1608.7 | 4.27e+03 tx/s +/- 808 tx/s (median of last 544) | Mean TPS is 1.61e+03 tx/s, 3.3 robust standard deviations below its recent median of 4.27e+03 tx/s (-62.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1072 (83.95% complete) |
| Slot | 362,645 of 432,000 in epoch |
| Absolute slot | 463,466,645 |
| Block height | 441,488,910 |
| Lifetime transactions | 564,531,209,383 |
| TPS (now / mean / peak) | 1,403 / 1,609 / 2,224 |
| True TPS, non-vote (now / mean) | 1,403 / 1,609 |
| Slot time (mean / worst) | 0.214s / 0.22s |

Epoch 1072 has **69,355 slots remaining**, about **4h 7m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 25 (3.62% delinquent) |
| Total stake | 435,357,093 SOL |
| Delinquent stake | 2,794,105 SOL (0.642%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.90% / 24.63% |
| Commission (mean / median) | 12.9% / 5.0% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,965,456 | 3.897% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,678,000 | 3.831% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,919,680 | 2.968% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,502,229 | 2.412% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,659,910 | 2.219% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,473,552 | 2.176% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,406 | 2.118% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,780,140 | 1.787% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,045,150 | 1.618% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,506 | 1.608% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,472,288 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,290 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 379,462 | 462,239,999 |
| `5RCD4pZcKH3NHN4XHxvsnVAawSaConLgsZbreSN5dXpZ` | 82,752 | 463,463,819 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 62,325 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,613 | 461,807,999 |
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 289 | 0 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $95.86 | -0.61% 24h ↓ |
| Market cap | $56.56B | |
| Spot volume 24h | $4.49B | |
| DeFi TVL | $5.40B | -5.13% 1d / -7.58% 7d / -16.42% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.16B | |
| Stablecoin supply (all pegs) | $15.24B | |
| DEX volume 24h | $2.30B | +32.42% 1d |
| DEX volume 7d / 30d | $12.55B / $60.51B | |
| Fees + app revenue 24h | $12.33M | +16.95% 1d |
| Circulating supply | 590,039,679 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $374.14M | 16.30% |
| BisonFi | $301.26M | 13.12% |
| Manifest Trade | $227.38M | 9.91% |
| Tessera V | $209.29M | 9.12% |
| Raydium AMM | $200.04M | 8.71% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-567 | [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) | 2026-10-30 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-10-30 |
| SIMD-529 | [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) | 2026-10-30 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-10-30T23:16:15Z | Change |
|---|---|---|---|
| SOL price | $107 | $96 | -10.78% |
| DeFi TVL | $5.94B | $5.40B | -9.12% |
| Stablecoin supply | $15.97B | $15.16B | -5.07% |
| DEX volume 24h | $3.63B | $2.30B | -36.80% |
| Mean TPS | 3,288 | 1,609 | -51.07% |
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
