# Solana Ecosystem Report

_Generated 2026-11-15T00:59:54Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-15T00:59:54Z` |
| Sources healthy | 7 of 8 |
| Collection time | 9.23s |
| Snapshots in history | 642 |
| Anomalies flagged | 5 (1 critical) |

## At a glance

- The network is processing **2,037 non-vote TPS** (2,037 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (37 delinquent, holding 0.092% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $69.43** (-10.61% over 24h), market cap $41.07B.
- **DeFi TVL $4.61B** (-11.12% 7d, -22.79% 30d), against $13.85B of stablecoins settled on Solana.
- **$1.58B of DEX volume in 24h** across 141 protocols, generating $8.65M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 69.43 | $104 +/- $6 (median of last 635) | SOL price is $69, 5.8 robust standard deviations below its recent median of $104 (-33.1%). |
| 🟠 warning | SOL 24h change | -10.61 | |change| < 10% | SOL moved -10.61% in 24h. |
| 🟠 warning | Delinquent validators | 37 | 13 +/- 5.93 (median of last 641) | Delinquent validators is 37, 4.0 robust standard deviations above its recent median of 13 (+184.6%). |
| 🟠 warning | DeFi TVL | 4605467588 | $5,905,247,626 +/- $293,802,955 (median of last 640) | DeFi TVL is $4,605,467,588, 4.4 robust standard deviations below its recent median of $5,905,247,626 (-22.0%). |
| 🟠 warning | Stablecoin supply | 13852080190.24 | $15,883,673,939 +/- $530,672,728 (median of last 641) | Stablecoin supply is $13,852,080,190, 3.8 robust standard deviations below its recent median of $15,883,673,939 (-12.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1086 (89.21% complete) |
| Slot | 385,374 of 432,000 in epoch |
| Absolute slot | 469,537,374 |
| Block height | 447,552,418 |
| Lifetime transactions | 566,738,622,833 |
| TPS (now / mean / peak) | 1,960 / 2,037 / 2,662 |
| True TPS, non-vote (now / mean) | 1,960 / 2,037 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1086 has **46,626 slots remaining**, about **2h 47m** at the current slot time.

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
| SOL price | $69.43 | -10.61% 24h ↓ |
| Market cap | $41.07B | |
| Spot volume 24h | $4.16B | |
| DeFi TVL | $4.61B | -0.00% 1d / -11.12% 7d / -22.79% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.85B | |
| Stablecoin supply (all pegs) | $13.94B | |
| DEX volume 24h | $1.58B | +1.35% 1d |
| DEX volume 7d / 30d | $9.10B / $50.03B | |
| Fees + app revenue 24h | $8.65M | -5.37% 1d |
| Circulating supply | 591,573,603 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $284.65M | 18.00% |
| BisonFi | $186.88M | 11.82% |
| PumpSwap | $177.25M | 11.21% |
| Meteora DLMM | $164.81M | 10.42% |
| Raydium AMM | $136.33M | 8.62% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-15T00:59:54Z | Change |
|---|---|---|---|
| SOL price | $107 | $69 | -35.38% |
| DeFi TVL | $5.94B | $4.61B | -22.53% |
| Stablecoin supply | $15.97B | $13.85B | -13.28% |
| DEX volume 24h | $3.63B | $1.58B | -56.45% |
| Mean TPS | 3,288 | 2,037 | -38.03% |
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
