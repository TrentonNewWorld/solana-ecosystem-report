# Solana Ecosystem Report

_Generated 2026-11-04T12:57:11Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-04T12:57:11Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.48s |
| Snapshots in history | 576 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,506 non-vote TPS** (1,506 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **661 active validators** (32 delinquent, holding 0.483% of stake). It takes **17 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $92.48** (-0.65% over 24h), market cap $54.59B.
- **DeFi TVL $5.44B** (-4.44% 7d, -17.24% 30d), against $14.47B of stablecoins settled on Solana.
- **$1.88B of DEX volume in 24h** across 141 protocols, generating $11.33M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.483 | 0.035% +/- 0.040% (median of last 575) | Delinquent stake is 0.483%, 11.2 robust standard deviations above its recent median of 0.035% (+1280.0%). |
| 🟠 warning | Delinquent validators | 32 | 12 +/- 4.448 (median of last 575) | Delinquent validators is 32, 4.5 robust standard deviations above its recent median of 12 (+166.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1077 (10.65% complete) |
| Slot | 46,007 of 432,000 in epoch |
| Absolute slot | 465,310,007 |
| Block height | 443,330,449 |
| Lifetime transactions | 565,171,507,788 |
| TPS (now / mean / peak) | 1,385 / 1,506 / 1,920 |
| True TPS, non-vote (now / mean) | 1,385 / 1,506 |
| Slot time (mean / worst) | 0.214s / 0.221s |

Epoch 1077 has **385,993 slots remaining**, about **22h 56m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 32 (4.62% delinquent) |
| Total stake | 433,017,789 SOL |
| Delinquent stake | 2,090,537 SOL (0.483%) |
| Nakamoto coefficient | 17 |
| Top 1 / top 10 stake share | 3.93% / 24.75% |
| Commission (mean / median) | 12.57% / 5% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,036,631 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,689 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,012,272 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,433,406 | 2.409% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,524,736 | 2.200% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,439,186 | 2.180% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,217,930 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,826,697 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,981,457 | 1.612% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,980,105 | 1.612% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,265,362 | 462,239,999 |
| `Dkj8XzgvjDuZzvAwiWYExt3rwLPqtVEQTpgK49tRirb5` | 300,002 | 465,263,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 237,143 | 462,239,999 |
| `5HScvYkTWL9iojhPv26xK7GqB7oBsj9A2qHCeNRFmdyG` | 112,728 | 465,308,981 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 76,346 | 465,263,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 17,541 | 463,967,999 |
| `2czzKTUoAtscCfEQN6LAjUX9GwzqqGqyemttYcYgYWkr` | 13,445 | 0 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 2,605 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $92.48 | -0.65% 24h ↓ |
| Market cap | $54.59B | |
| Spot volume 24h | $2.78B | |
| DeFi TVL | $5.44B | +0.75% 1d / -4.44% 7d / -17.24% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.47B | |
| Stablecoin supply (all pegs) | $14.56B | |
| DEX volume 24h | $1.88B | +1.54% 1d |
| DEX volume 7d / 30d | $11.74B / $57.10B | |
| Fees + app revenue 24h | $11.33M | +1.11% 1d |
| Circulating supply | 590,262,421 SOL (92.66% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $321.84M | 17.11% |
| BisonFi | $257.10M | 13.67% |
| Orca DEX | $250.14M | 13.30% |
| Raydium AMM | $176.51M | 9.38% |
| Tessera V | $154.41M | 8.21% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-04T12:57:11Z | Change |
|---|---|---|---|
| SOL price | $107 | $92 | -13.92% |
| DeFi TVL | $5.94B | $5.44B | -8.48% |
| Stablecoin supply | $15.97B | $14.47B | -9.43% |
| DEX volume 24h | $3.63B | $1.88B | -48.21% |
| Mean TPS | 3,288 | 1,506 | -54.19% |
| Active validators | 689 | 661 | -4.06% |
| Nakamoto coefficient | 18 | 17 | -5.56% |

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
