# Solana Ecosystem Report

_Generated 2026-11-08T10:47:08Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-08T10:47:08Z` |
| Sources healthy | 7 of 8 |
| Collection time | 29.73s |
| Snapshots in history | 602 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **927 non-vote TPS** (927 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **662 active validators** (35 delinquent, holding 0.156% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $89.11** (-0.79% over 24h), market cap $52.67B.
- **DeFi TVL $5.18B** (-4.19% 7d, -15.85% 30d), against $14.58B of stablecoins settled on Solana.
- **$1.30B of DEX volume in 24h** across 141 protocols, generating $7.97M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 35 | 12 +/- 4.448 (median of last 601) | Delinquent validators is 35, 5.2 robust standard deviations above its recent median of 12 (+191.7%). |
| 🟠 warning | Mean TPS | 927.4 | 4.15e+03 tx/s +/- 978 tx/s (median of last 601) | Mean TPS is 927 tx/s, 3.3 robust standard deviations below its recent median of 4.15e+03 tx/s (-77.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1080 (75.64% complete) |
| Slot | 326,763 of 432,000 in epoch |
| Absolute slot | 466,886,763 |
| Block height | 444,905,085 |
| Lifetime transactions | 565,759,118,331 |
| TPS (now / mean / peak) | 1,128 / 927 / 1,170 |
| True TPS, non-vote (now / mean) | 1,128 / 927 |
| Slot time (mean / worst) | 0.214s / 0.219s |

Epoch 1080 has **105,237 slots remaining**, about **6h 15m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 35 (5.02% delinquent) |
| Total stake | 434,780,965 SOL |
| Delinquent stake | 677,695 SOL (0.156%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.63% |
| Commission (mean / median) | 13.0% / 5.0% |
| Zero-commission validators | 222 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,043,402 | 3.920% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,729,016 | 3.848% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,015,291 | 2.994% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,277,563 | 2.364% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,558,411 | 2.198% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,520,070 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,242,930 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,750,589 | 1.783% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,983,623 | 1.606% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,973,337 | 1.604% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,555 | 462,239,999 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 140,397 | 465,663,873 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 134,485 | 466,294,271 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 70,733 | 465,263,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `FXcZJuQwkcQpw2YrkTaxWJ6rnw4P12wvULttviMRn655` | 48,369 | 466,816,251 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,836 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $89.11 | -0.79% 24h ↓ |
| Market cap | $52.67B | |
| Spot volume 24h | $847.80M | |
| DeFi TVL | $5.18B | -0.82% 1d / -4.19% 7d / -15.85% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.58B | |
| Stablecoin supply (all pegs) | $14.66B | |
| DEX volume 24h | $1.30B | -12.25% 1d |
| DEX volume 7d / 30d | $11.17B / $54.67B | |
| Fees + app revenue 24h | $7.97M | -9.36% 1d |
| Circulating supply | 591,038,080 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $217.32M | 16.73% |
| BisonFi | $170.16M | 13.10% |
| Tessera V | $153.42M | 11.81% |
| Meteora DLMM | $128.65M | 9.91% |
| pump.fun | $108.28M | 8.34% |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-08T10:47:08Z | Change |
|---|---|---|---|
| SOL price | $107 | $89 | -17.06% |
| DeFi TVL | $5.94B | $5.18B | -12.82% |
| Stablecoin supply | $15.97B | $14.58B | -8.72% |
| DEX volume 24h | $3.63B | $1.30B | -64.24% |
| Mean TPS | 3,288 | 927 | -71.79% |
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
