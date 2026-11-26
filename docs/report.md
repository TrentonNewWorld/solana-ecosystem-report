# Solana Ecosystem Report

_Generated 2026-11-26T13:12:25Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-26T13:12:25Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.31s |
| Snapshots in history | 701 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,289 non-vote TPS** (1,289 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **657 active validators** (31 delinquent, holding 0.032% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $70.93** (+4.67% over 24h), market cap $42.00B.
- **DeFi TVL $4.58B** (-2.87% 7d, -18.98% 30d), against $12.64B of stablecoins settled on Solana.
- **$1.51B of DEX volume in 24h** across 146 protocols, generating $7.56M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 12638520679.95 | $15,783,339,816 +/- $584,711,650 (median of last 700) | Stablecoin supply is $12,638,520,680, 5.4 robust standard deviations below its recent median of $15,783,339,816 (-19.9%). |
| 🟠 warning | Delinquent validators | 31 | 13 +/- 5.93 (median of last 700) | Delinquent validators is 31, 3.0 robust standard deviations above its recent median of 13 (+138.5%). |
| 🟠 warning | SOL price | 70.93 | $103 +/- $8 (median of last 693) | SOL price is $71, 4.2 robust standard deviations below its recent median of $103 (-31.3%). |
| 🟠 warning | DeFi TVL | 4577425093 | $5,889,981,629 +/- $369,345,591 (median of last 699) | DeFi TVL is $4,577,425,093, 3.6 robust standard deviations below its recent median of $5,889,981,629 (-22.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1097 (59.38% complete) |
| Slot | 256,500 of 432,000 in epoch |
| Absolute slot | 474,160,500 |
| Block height | 452,173,358 |
| Lifetime transactions | 568,481,881,316 |
| TPS (now / mean / peak) | 1,425 / 1,289 / 1,659 |
| True TPS, non-vote (now / mean) | 1,425 / 1,289 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1097 has **175,500 slots remaining**, about **10h 28m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 31 (4.51% delinquent) |
| Total stake | 423,675,927 SOL |
| Delinquent stake | 134,069 SOL (0.032%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.98% |
| Commission (mean / median) | 13.24% / 5% |
| Zero-commission validators | 218 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,805,000 | 3.966% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,814,431 | 3.733% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,430,859 | 2.934% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,236,589 | 2.416% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,910,258 | 2.339% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,394 | 2.270% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,281,563 | 2.191% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,032,075 | 1.896% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,305 | 1.645% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,740,287 | 1.591% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `DG6fVEB2Qy1jntvHVPui3R12CMqcwNNnjYPYdsbQ9ACP` | 88,583 | 473,749,295 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,411 | 473,471,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 9,529 | 471,311,999 |
| `DqbRPQXbN8GDKWZkKiHnRjiSKPqE3rQaNgTPxdLGPDMK` | 3,090 | 473,903,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 125 | 472,608,648 |
| `47hzyKgoz9Fu1HP4mR48tvAFj7akCFZKGzZqWo32sNqG` | 46 | 472,988,210 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 10 | 462,239,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $70.93 | +4.67% 24h ↑ |
| Market cap | $42.00B | |
| Spot volume 24h | $3.00B | |
| DeFi TVL | $4.58B | +1.23% 1d / -2.87% 7d / -18.98% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.64B | |
| Stablecoin supply (all pegs) | $12.72B | |
| DEX volume 24h | $1.51B | +3.72% 1d |
| DEX volume 7d / 30d | $10.88B / $47.62B | |
| Fees + app revenue 24h | $7.56M | +5.75% 1d |
| Circulating supply | 592,183,200 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $213.24M | 14.11% |
| BisonFi | $190.65M | 12.62% |
| Raydium AMM | $147.01M | 9.73% |
| Meteora DLMM | $119.43M | 7.90% |
| Scorch | $104.62M | 6.92% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-26 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-26 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-11-25 |
| - | [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) | 2026-11-25 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-11-25 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-24 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-24 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | Release v4.5.0-rc.0 | 2026-11-25 |
| [`v5.0.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | Release v5.0.0-alpha.1 | 2026-11-19 |
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-26T13:12:25Z | Change |
|---|---|---|---|
| SOL price | $107 | $71 | -33.98% |
| DeFi TVL | $5.94B | $4.58B | -23.00% |
| Stablecoin supply | $15.97B | $12.64B | -20.88% |
| DEX volume 24h | $3.63B | $1.51B | -58.40% |
| Mean TPS | 3,288 | 1,289 | -60.79% |
| Active validators | 689 | 657 | -4.64% |
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
