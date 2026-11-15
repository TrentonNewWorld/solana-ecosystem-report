# Solana Ecosystem Report

_Generated 2026-11-15T03:07:39Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-15T03:07:39Z` |
| Sources healthy | 8 of 8 |
| Collection time | 6.2s |
| Snapshots in history | 643 |
| Anomalies flagged | 4 (2 critical) |

## At a glance

- The network is processing **1,998 non-vote TPS** (1,998 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (37 delinquent, holding 0.092% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $71.61** (-5.77% over 24h), market cap $42.40B.
- **DeFi TVL $4.58B** (-11.65% 7d, -23.25% 30d), against $13.87B of stablecoins settled on Solana.
- **$1.60B of DEX volume in 24h** across 141 protocols, generating $8.19M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 71.61 | $104 +/- $6 (median of last 636) | SOL price is $72, 5.4 robust standard deviations below its recent median of $104 (-31.0%). |
| 🔴 critical | DeFi TVL | 4578489569 | $5,904,600,747 +/- $293,503,623 (median of last 641) | DeFi TVL is $4,578,489,569, 4.5 robust standard deviations below its recent median of $5,904,600,747 (-22.5%). |
| 🟠 warning | Delinquent validators | 37 | 13 +/- 5.93 (median of last 642) | Delinquent validators is 37, 4.0 robust standard deviations above its recent median of 13 (+184.6%). |
| 🟠 warning | Stablecoin supply | 13870517063.54 | $15,877,952,460 +/- $532,965,289 (median of last 642) | Stablecoin supply is $13,870,517,064, 3.8 robust standard deviations below its recent median of $15,877,952,460 (-12.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1086 (97.45% complete) |
| Slot | 420,965 of 432,000 in epoch |
| Absolute slot | 469,572,965 |
| Block height | 447,587,997 |
| Lifetime transactions | 566,754,534,951 |
| TPS (now / mean / peak) | 1,459 / 1,998 / 3,104 |
| True TPS, non-vote (now / mean) | 1,459 / 1,998 |
| Slot time (mean / worst) | 0.215s / 0.226s |

Epoch 1086 has **11,035 slots remaining**, about **39m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 (5.29% delinquent) |
| Total stake | 429,651,631 SOL |
| Delinquent stake | 395,342 SOL (0.092%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.95% / 24.72% |
| Commission (mean / median) | 12.74% / 5.0% |
| Zero-commission validators | 221 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,955,905 | 3.946% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,374,909 | 3.811% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,611,498 | 2.935% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,140,468 | 2.360% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,736,890 | 2.266% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,439 | 2.228% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,199,377 | 2.141% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,914,792 | 1.842% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,990,062 | 1.627% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,707,745 | 1.561% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 209,267 | 462,239,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 43,199 | 467,356,299 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 42,511 | 467,356,334 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `6M6vB2thgACsfHHuk5KZPdWqSJivm9mArVLxKXynBGbS` | 10,634 | 0 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,643 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $71.61 | -5.77% 24h ↓ |
| Market cap | $42.40B | |
| Spot volume 24h | $4.59B | |
| DeFi TVL | $4.58B | -3.81% 1d / -11.65% 7d / -23.25% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.87B | |
| Stablecoin supply (all pegs) | $13.96B | |
| DEX volume 24h | $1.60B | +2.49% 1d |
| DEX volume 7d / 30d | $9.38B / $50.31B | |
| Fees + app revenue 24h | $8.19M | -10.49% 1d |
| Circulating supply | 591,573,561 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $300.41M | 18.78% |
| BisonFi | $186.88M | 11.68% |
| Meteora DLMM | $164.81M | 10.30% |
| PumpSwap | $156.41M | 9.78% |
| Raydium AMM | $139.38M | 8.71% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-14 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-14 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-12 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-15T03:07:39Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -33.35% |
| DeFi TVL | $5.94B | $4.58B | -22.98% |
| Stablecoin supply | $15.97B | $13.87B | -13.17% |
| DEX volume 24h | $3.63B | $1.60B | -55.96% |
| Mean TPS | 3,288 | 1,998 | -39.24% |
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
