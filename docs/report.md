# Solana Ecosystem Report

_Generated 2026-11-17T03:47:26Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-17T03:47:26Z` |
| Sources healthy | 7 of 8 |
| Collection time | 10.3s |
| Snapshots in history | 655 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,511 non-vote TPS** (1,511 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (37 delinquent, holding 0.035% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $72.49** (+0.80% over 24h), market cap $42.91B.
- **DeFi TVL $4.73B** (-6.48% 7d, -19.63% 30d), against $13.99B of stablecoins settled on Solana.
- **$1.40B of DEX volume in 24h** across 142 protocols, generating $7.85M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 72.49 | $104 +/- $6 (median of last 647) | SOL price is $72, 5.0 robust standard deviations below its recent median of $104 (-30.1%). |
| 🟠 warning | Delinquent validators | 37 | 13 +/- 5.93 (median of last 654) | Delinquent validators is 37, 4.0 robust standard deviations above its recent median of 13 (+184.6%). |
| 🟠 warning | DeFi TVL | 4726352896 | $5,900,078,979 +/- $300,655,742 (median of last 653) | DeFi TVL is $4,726,352,896, 3.9 robust standard deviations below its recent median of $5,900,078,979 (-19.9%). |
| 🟠 warning | Stablecoin supply | 13985622260.95 | $15,862,749,603 +/- $541,202,466 (median of last 654) | Stablecoin supply is $13,985,622,261, 3.5 robust standard deviations below its recent median of $15,862,749,603 (-11.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1088 (86.17% complete) |
| Slot | 372,262 of 432,000 in epoch |
| Absolute slot | 470,388,262 |
| Block height | 448,403,106 |
| Lifetime transactions | 567,050,852,958 |
| TPS (now / mean / peak) | 1,513 / 1,511 / 2,034 |
| True TPS, non-vote (now / mean) | 1,513 / 1,511 |
| Slot time (mean / worst) | 0.215s / 0.222s |

Epoch 1088 has **59,738 slots remaining**, about **3h 34m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 (5.29% delinquent) |
| Total stake | 429,145,034 SOL |
| Delinquent stake | 152,189 SOL (0.035%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.95% / 24.77% |
| Commission (mean / median) | 12.78% / 5.0% |
| Zero-commission validators | 220 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,936,855 | 3.947% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,432,361 | 3.829% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,687 | 2.910% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,142,842 | 2.363% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,787,748 | 2.281% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,620,150 | 2.242% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,212,350 | 2.147% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,959,108 | 1.855% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,992,227 | 1.629% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,709,566 | 1.563% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `fuyugZxM5S4NyV3ZYoc6ebs3fmRTrZ3X27MKCFvHpVD` | 68,080 | 470,015,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,516 | 469,583,999 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 13,483 | 467,356,299 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 5,493 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,640 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |
| `PEBBLETUXFPdrwm5heff4x1VsrypGS1fNSRPEF6LiZL` | 162 | 466,127,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $72.49 | +0.80% 24h ↑ |
| Market cap | $42.91B | |
| Spot volume 24h | $2.81B | |
| DeFi TVL | $4.73B | +0.84% 1d / -6.48% 7d / -19.63% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.99B | |
| Stablecoin supply (all pegs) | $14.07B | |
| DEX volume 24h | $1.40B | +3.36% 1d |
| DEX volume 7d / 30d | $9.80B / $49.84B | |
| Fees + app revenue 24h | $7.85M | +10.52% 1d |
| Circulating supply | 591,684,180 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $212.41M | 15.19% |
| BisonFi | $158.79M | 11.36% |
| PumpSwap | $157.21M | 11.25% |
| Raydium AMM | $132.23M | 9.46% |
| Meteora DLMM | $119.67M | 8.56% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-17T03:47:26Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -32.53% |
| DeFi TVL | $5.94B | $4.73B | -20.49% |
| Stablecoin supply | $15.97B | $13.99B | -12.45% |
| DEX volume 24h | $3.63B | $1.40B | -61.51% |
| Mean TPS | 3,288 | 1,511 | -54.05% |
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
