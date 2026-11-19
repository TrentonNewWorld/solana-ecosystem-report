# Solana Ecosystem Report

_Generated 2026-11-19T14:22:42Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-19T14:22:42Z` |
| Sources healthy | 7 of 8 |
| Collection time | 10.36s |
| Snapshots in history | 667 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,662 non-vote TPS** (1,662 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **659 active validators** (26 delinquent, holding 0.025% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $75.05** (+0.99% over 24h), market cap $44.42B.
- **DeFi TVL $4.76B** (-5.44% 7d, -18.34% 30d), against $12.59B of stablecoins settled on Solana.
- **$1.82B of DEX volume in 24h** across 144 protocols, generating $10.95M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 12590276319.57 | $15,842,053,513 +/- $548,753,400 (median of last 666) | Stablecoin supply is $12,590,276,320, 5.9 robust standard deviations below its recent median of $15,842,053,513 (-20.5%). |
| 🟠 warning | SOL price | 75.05 | $104 +/- $6 (median of last 659) | SOL price is $75, 4.4 robust standard deviations below its recent median of $104 (-27.6%). |
| 🟠 warning | DeFi TVL | 4761875833 | $5,898,068,561 +/- $313,776,728 (median of last 665) | DeFi TVL is $4,761,875,833, 3.6 robust standard deviations below its recent median of $5,898,068,561 (-19.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1091 (12.89% complete) |
| Slot | 55,693 of 432,000 in epoch |
| Absolute slot | 471,367,693 |
| Block height | 449,381,963 |
| Lifetime transactions | 567,421,888,000 |
| TPS (now / mean / peak) | 1,894 / 1,662 / 2,090 |
| True TPS, non-vote (now / mean) | 1,894 / 1,662 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1091 has **376,307 slots remaining**, about **22h 28m** at the current slot time.

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
| SOL price | $75.05 | +0.99% 24h ↑ |
| Market cap | $44.42B | |
| Spot volume 24h | $2.17B | |
| DeFi TVL | $4.76B | -0.75% 1d / -5.44% 7d / -18.34% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.59B | |
| Stablecoin supply (all pegs) | $12.67B | |
| DEX volume 24h | $1.82B | +20.25% 1d |
| DEX volume 7d / 30d | $10.91B / $50.39B | |
| Fees + app revenue 24h | $10.95M | +33.50% 1d |
| Circulating supply | 591,851,599 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $330.65M | 18.21% |
| Orca DEX | $254.46M | 14.02% |
| Meteora DLMM | $246.17M | 13.56% |
| Raydium AMM | $196.64M | 10.83% |
| BisonFi | $153.98M | 8.48% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-19T14:22:42Z | Change |
|---|---|---|---|
| SOL price | $107 | $75 | -30.15% |
| DeFi TVL | $5.94B | $4.76B | -19.90% |
| Stablecoin supply | $15.97B | $12.59B | -21.18% |
| DEX volume 24h | $3.63B | $1.82B | -50.02% |
| Mean TPS | 3,288 | 1,662 | -49.43% |
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
