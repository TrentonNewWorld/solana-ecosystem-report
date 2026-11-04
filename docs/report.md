# Solana Ecosystem Report

_Generated 2026-11-04T01:18:22Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-04T01:18:22Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.54s |
| Snapshots in history | 573 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,411 non-vote TPS** (2,411 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **666 active validators** (27 delinquent, holding 0.419% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $91.78** (-0.69% over 24h), market cap $54.15B.
- **DeFi TVL $5.43B** (-4.57% 7d, -17.35% 30d), against $14.57B of stablecoins settled on Solana.
- **$1.81B of DEX volume in 24h** across 141 protocols, generating $11.28M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.419 | 0.034% +/- 0.039% (median of last 572) | Delinquent stake is 0.419%, 10.0 robust standard deviations above its recent median of 0.034% (+1132.4%). |
| 🟠 warning | Delinquent validators | 27 | 12 +/- 4.448 (median of last 572) | Delinquent validators is 27, 3.4 robust standard deviations above its recent median of 12 (+125.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1076 (65.34% complete) |
| Slot | 282,249 of 432,000 in epoch |
| Absolute slot | 465,114,249 |
| Block height | 443,134,851 |
| Lifetime transactions | 565,102,532,156 |
| TPS (now / mean / peak) | 2,085 / 2,411 / 3,863 |
| True TPS, non-vote (now / mean) | 2,085 / 2,411 |
| Slot time (mean / worst) | 0.214s / 0.22s |

Epoch 1076 has **149,751 slots remaining**, about **8h 54m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 27 (3.90% delinquent) |
| Total stake | 434,699,177 SOL |
| Delinquent stake | 1,819,919 SOL (0.419%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.67% |
| Commission (mean / median) | 12.79% / 5.0% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,030,641 | 3.918% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,704,340 | 3.843% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,043,664 | 3.001% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,431,126 | 2.400% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,561,007 | 2.199% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,435,905 | 2.171% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,232,746 | 2.124% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,810 | 1.798% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,008,986 | 1.612% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,979,031 | 1.605% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,283,412 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 241,107 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 214,167 | 462,239,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 16,586 | 463,967,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,850 | 464,160,502 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $91.78 | -0.69% 24h ↓ |
| Market cap | $54.15B | |
| Spot volume 24h | $2.10B | |
| DeFi TVL | $5.43B | +0.00% 1d / -4.57% 7d / -17.35% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.57B | |
| Stablecoin supply (all pegs) | $14.65B | |
| DEX volume 24h | $1.81B | -2.32% 1d |
| DEX volume 7d / 30d | $10.34B / $55.70B | |
| Fees + app revenue 24h | $11.28M | +0.61% 1d |
| Circulating supply | 590,265,779 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $261.06M | 14.43% |
| BisonFi | $250.54M | 13.84% |
| Orca DEX | $183.04M | 10.11% |
| Tessera V | $149.85M | 8.28% |
| Raydium AMM | $127.04M | 7.02% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-11-04 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-03 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-11-03 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-03 |
| SIMD-706 | [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-11-03 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-03 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-10-29 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-11-04T01:18:22Z | Change |
|---|---|---|---|
| SOL price | $107 | $92 | -14.58% |
| DeFi TVL | $5.94B | $5.43B | -8.61% |
| Stablecoin supply | $15.97B | $14.57B | -8.82% |
| DEX volume 24h | $3.63B | $1.81B | -50.18% |
| Mean TPS | 3,288 | 2,411 | -26.65% |
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
