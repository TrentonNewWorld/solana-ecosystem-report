# Solana Ecosystem Report

_Generated 2026-11-14T10:58:28Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-14T10:58:28Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.74s |
| Snapshots in history | 637 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,110 non-vote TPS** (1,110 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **661 active validators** (38 delinquent, holding 0.110% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $75.69** (-5.94% over 24h), market cap $44.82B.
- **DeFi TVL $4.82B** (-7.82% 7d, -18.62% 30d), against $13.88B of stablecoins settled on Solana.
- **$1.47B of DEX volume in 24h** across 141 protocols, generating $9.29M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 75.69 | $104 +/- $6 (median of last 630) | SOL price is $76, 4.7 robust standard deviations below its recent median of $104 (-27.1%). |
| 🟠 warning | Delinquent validators | 38 | 13 +/- 5.93 (median of last 636) | Delinquent validators is 38, 4.2 robust standard deviations above its recent median of 13 (+192.3%). |
| 🟠 warning | DeFi TVL | 4817043713 | $5,907,054,927 +/- $294,193,576 (median of last 635) | DeFi TVL is $4,817,043,713, 3.7 robust standard deviations below its recent median of $5,907,054,927 (-18.5%). |
| 🟠 warning | Stablecoin supply | 13882609683.1 | $15,888,638,087 +/- $528,318,323 (median of last 636) | Stablecoin supply is $13,882,609,683, 3.8 robust standard deviations below its recent median of $15,888,638,087 (-12.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1086 (34.90% complete) |
| Slot | 150,765 of 432,000 in epoch |
| Absolute slot | 469,302,765 |
| Block height | 447,317,856 |
| Lifetime transactions | 566,643,575,246 |
| TPS (now / mean / peak) | 1,209 / 1,110 / 1,672 |
| True TPS, non-vote (now / mean) | 1,209 / 1,110 |
| Slot time (mean / worst) | 0.215s / 0.223s |

Epoch 1086 has **281,235 slots remaining**, about **16h 47m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 38 (5.44% delinquent) |
| Total stake | 429,651,631 SOL |
| Delinquent stake | 474,030 SOL (0.110%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.95% / 24.72% |
| Commission (mean / median) | 12.58% / 5% |
| Zero-commission validators | 223 |

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
| `3xjfK9C9YNcta8MvK1US4sQ3bc6DEjoJoR3qLExGf9xE` | 78,688 | 469,225,428 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 43,199 | 467,356,299 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 42,511 | 467,356,334 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `6M6vB2thgACsfHHuk5KZPdWqSJivm9mArVLxKXynBGbS` | 10,634 | 0 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,643 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $75.69 | -5.94% 24h ↓ |
| Market cap | $44.82B | |
| Spot volume 24h | $3.31B | |
| DeFi TVL | $4.82B | -3.66% 1d / -7.82% 7d / -18.62% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.88B | |
| Stablecoin supply (all pegs) | $13.97B | |
| DEX volume 24h | $1.47B | -2.01% 1d |
| DEX volume 7d / 30d | $8.86B / $51.68B | |
| Fees + app revenue 24h | $9.29M | +16.34% 1d |
| Circulating supply | 591,573,860 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $228.27M | 15.49% |
| PumpSwap | $177.25M | 12.03% |
| Meteora DLMM | $164.81M | 11.19% |
| BisonFi | $147.27M | 10.00% |
| Raydium AMM | $119.70M | 8.12% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-12 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-12 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-09 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-14T10:58:28Z | Change |
|---|---|---|---|
| SOL price | $107 | $76 | -29.55% |
| DeFi TVL | $5.94B | $4.82B | -18.97% |
| Stablecoin supply | $15.97B | $13.88B | -13.09% |
| DEX volume 24h | $3.63B | $1.47B | -59.44% |
| Mean TPS | 3,288 | 1,110 | -66.22% |
| Active validators | 689 | 661 | -4.06% |
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
