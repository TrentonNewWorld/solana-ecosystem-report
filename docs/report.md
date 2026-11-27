# Solana Ecosystem Report

_Generated 2026-11-27T21:56:21Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-27T21:56:21Z` |
| Sources healthy | 7 of 8 |
| Collection time | 9.08s |
| Snapshots in history | 706 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,817 non-vote TPS** (1,817 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **654 active validators** (34 delinquent, holding 0.060% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $71.93** (+0.46% over 24h), market cap $42.61B.
- **DeFi TVL $4.62B** (-2.02% 7d, -18.93% 30d), against $12.84B of stablecoins settled on Solana.
- **$870.58M of DEX volume in 24h** across 146 protocols, generating $6.15M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 12839084862.87 | $15,777,382,033 +/- $599,321,062 (median of last 705) | Stablecoin supply is $12,839,084,863, 4.9 robust standard deviations below its recent median of $15,777,382,033 (-18.6%). |
| 🟠 warning | Delinquent validators | 34 | 13 +/- 5.93 (median of last 705) | Delinquent validators is 34, 3.5 robust standard deviations above its recent median of 13 (+161.5%). |
| 🟠 warning | SOL price | 71.93 | $103 +/- $8 (median of last 698) | SOL price is $72, 3.9 robust standard deviations below its recent median of $103 (-30.4%). |
| 🟠 warning | DeFi TVL | 4615619801 | $5,889,229,234 +/- $379,373,279 (median of last 704) | DeFi TVL is $4,615,619,801, 3.4 robust standard deviations below its recent median of $5,889,229,234 (-21.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1098 (86.30% complete) |
| Slot | 372,837 of 432,000 in epoch |
| Absolute slot | 474,708,837 |
| Block height | 452,721,467 |
| Lifetime transactions | 568,676,383,796 |
| TPS (now / mean / peak) | 1,611 / 1,817 / 2,480 |
| True TPS, non-vote (now / mean) | 1,611 / 1,817 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1098 has **59,163 slots remaining**, about **3h 32m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 34 (4.94% delinquent) |
| Total stake | 424,207,451 SOL |
| Delinquent stake | 255,036 SOL (0.060%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.96% / 24.96% |
| Commission (mean / median) | 13.15% / 5.0% |
| Zero-commission validators | 216 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,245 | 3.964% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,826,052 | 3.731% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,437,388 | 2.932% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,238,108 | 2.413% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,920,637 | 2.339% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,617,109 | 2.267% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,296,651 | 2.192% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,037,877 | 1.895% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,972,141 | 1.644% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,741,351 | 1.589% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `DG6fVEB2Qy1jntvHVPui3R12CMqcwNNnjYPYdsbQ9ACP` | 68,776 | 473,749,295 |
| `irKsY8c3sQur1XaYuQ811hzsEQJ5Hq3Yu3AAoXYnp8W` | 60,716 | 474,335,999 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 35,467 | 474,335,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,405 | 473,471,999 |
| `46mwXQRqWwj8Jp4ZR2tL1Yr3Snm99xDfKUs5jz7hLmEK` | 29,437 | 474,288,935 |
| `3Z1N2Fkfha4ThNiRwN8RnU6U8dkFJ92DH2TFyLWJf8cj` | 15,163 | 474,335,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 9,529 | 471,311,999 |
| `DqbRPQXbN8GDKWZkKiHnRjiSKPqE3rQaNgTPxdLGPDMK` | 3,090 | 473,903,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 125 | 472,608,648 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $71.93 | +0.46% 24h ↑ |
| Market cap | $42.61B | |
| Spot volume 24h | $2.63B | |
| DeFi TVL | $4.62B | +0.75% 1d / -2.02% 7d / -18.93% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.84B | |
| Stablecoin supply (all pegs) | $12.92B | |
| DEX volume 24h | $870.58M | -42.38% 1d |
| DEX volume 7d / 30d | $9.85B / $46.90B | |
| Fees + app revenue 24h | $6.15M | -13.95% 1d |
| Circulating supply | 592,238,097 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $139.53M | 16.03% |
| Raydium AMM | $111.99M | 12.86% |
| pump.fun | $107.98M | 12.40% |
| PumpSwap | $86.72M | 9.96% |
| BisonFi | $81.42M | 9.35% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-27T21:56:21Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -33.05% |
| DeFi TVL | $5.94B | $4.62B | -22.36% |
| Stablecoin supply | $15.97B | $12.84B | -19.63% |
| DEX volume 24h | $3.63B | $870.58M | -76.03% |
| Mean TPS | 3,288 | 1,817 | -44.74% |
| Active validators | 689 | 654 | -5.08% |
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
