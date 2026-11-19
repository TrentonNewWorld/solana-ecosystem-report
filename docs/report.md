# Solana Ecosystem Report

_Generated 2026-11-19T12:12:08Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-19T12:12:08Z` |
| Sources healthy | 7 of 8 |
| Collection time | 9.89s |
| Snapshots in history | 666 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,397 non-vote TPS** (1,397 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.216s**.
- **659 active validators** (26 delinquent, holding 0.025% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $74.6** (+0.20% over 24h), market cap $44.15B.
- **DeFi TVL $4.76B** (-5.47% 7d, -18.36% 30d), against $12.57B of stablecoins settled on Solana.
- **$1.82B of DEX volume in 24h** across 144 protocols, generating $10.88M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 12572981255.26 | $15,845,153,845 +/- $544,468,953 (median of last 665) | Stablecoin supply is $12,572,981,255, 6.0 robust standard deviations below its recent median of $15,845,153,845 (-20.7%). |
| 🟠 warning | SOL price | 74.6 | $104 +/- $6 (median of last 658) | SOL price is $75, 4.5 robust standard deviations below its recent median of $104 (-28.0%). |
| 🟠 warning | DeFi TVL | 4760507476 | $5,898,168,787 +/- $312,948,708 (median of last 664) | DeFi TVL is $4,760,507,476, 3.6 robust standard deviations below its recent median of $5,898,168,787 (-19.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1091 (4.47% complete) |
| Slot | 19,323 of 432,000 in epoch |
| Absolute slot | 471,331,323 |
| Block height | 449,345,606 |
| Lifetime transactions | 567,409,294,754 |
| TPS (now / mean / peak) | 1,451 / 1,397 / 2,041 |
| True TPS, non-vote (now / mean) | 1,451 / 1,397 |
| Slot time (mean / worst) | 0.216s / 0.221s |

Epoch 1091 has **412,677 slots remaining**, about **24h 45m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 26 (3.80% delinquent) |
| Total stake | 428,682,730 SOL |
| Delinquent stake | 108,886 SOL (0.025%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.84% |
| Commission (mean / median) | 12.63% / 5% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,960 | 3.972% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,375,745 | 3.820% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,025 | 2.898% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,299,570 | 2.403% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,431 | 2.290% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,573,248 | 2.233% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,578 | 2.152% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,980,784 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,844 | 1.632% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,772,455 | 1.580% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 42,980 | 471,311,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,450 | 469,583,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,421 | 470,879,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `GdFaSCpPf9RqRjxkvXUCzLR62bEjmEPZMS9XRVFC3pDu` | 2 | 469,698,063 |
| `D3wscqsBCJGFzzoB7dB7wQfJzSEFVzu8Rxugfnfk7rdm` | 1 | 458,009,563 |
| `5DutFKQ8qPmbjFEmp31QH9JDYJXvwh9pma8ap5Phxk6H` | 1 | 465,304,579 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $74.6 | +0.20% 24h ↑ |
| Market cap | $44.15B | |
| Spot volume 24h | $2.08B | |
| DeFi TVL | $4.76B | -0.78% 1d / -5.47% 7d / -18.36% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.57B | |
| Stablecoin supply (all pegs) | $12.66B | |
| DEX volume 24h | $1.82B | +20.25% 1d |
| DEX volume 7d / 30d | $10.91B / $50.39B | |
| Fees + app revenue 24h | $10.88M | +33.77% 1d |
| Circulating supply | 591,851,694 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $330.65M | 18.21% |
| Orca DEX | $261.56M | 14.41% |
| Meteora DLMM | $246.17M | 13.56% |
| Raydium AMM | $201.82M | 11.12% |
| BisonFi | $153.98M | 8.48% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-19T12:12:08Z | Change |
|---|---|---|---|
| SOL price | $107 | $75 | -30.57% |
| DeFi TVL | $5.94B | $4.76B | -19.92% |
| Stablecoin supply | $15.97B | $12.57B | -21.29% |
| DEX volume 24h | $3.63B | $1.82B | -50.02% |
| Mean TPS | 3,288 | 1,397 | -57.52% |
| Active validators | 689 | 659 | -4.35% |
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
