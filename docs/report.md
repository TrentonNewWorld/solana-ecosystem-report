# Solana Ecosystem Report

_Generated 2026-11-07T10:42:16Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-07T10:42:16Z` |
| Sources healthy | 8 of 8 |
| Collection time | 6.56s |
| Snapshots in history | 594 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **1,072 non-vote TPS** (1,072 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **660 active validators** (36 delinquent, holding 0.284% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $89.74** (-0.35% over 24h), market cap $53.03B.
- **DeFi TVL $5.22B** (-4.19% 7d, -18.42% 30d), against $14.45B of stablecoins settled on Solana.
- **$1.86B of DEX volume in 24h** across 141 protocols, generating $9.38M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.284 | 0.035% +/- 0.040% (median of last 593) | Delinquent stake is 0.284%, 6.2 robust standard deviations above its recent median of 0.035% (+711.4%). |
| 🔴 critical | Delinquent validators | 36 | 12 +/- 4.448 (median of last 593) | Delinquent validators is 36, 5.4 robust standard deviations above its recent median of 12 (+200.0%). |
| 🟠 warning | Mean TPS | 1072.4 | 4.16e+03 tx/s +/- 956 tx/s (median of last 593) | Mean TPS is 1.07e+03 tx/s, 3.2 robust standard deviations below its recent median of 4.16e+03 tx/s (-74.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1079 (82.09% complete) |
| Slot | 354,641 of 432,000 in epoch |
| Absolute slot | 466,482,641 |
| Block height | 444,501,330 |
| Lifetime transactions | 565,636,863,852 |
| TPS (now / mean / peak) | 855 / 1,072 / 1,476 |
| True TPS, non-vote (now / mean) | 855 / 1,072 |
| Slot time (mean / worst) | 0.214s / 0.219s |

Epoch 1079 has **77,359 slots remaining**, about **4h 35m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 36 (5.17% delinquent) |
| Total stake | 434,917,723 SOL |
| Delinquent stake | 1,236,226 SOL (0.284%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.65% |
| Commission (mean / median) | 12.89% / 5.0% |
| Zero-commission validators | 221 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,039,556 | 3.918% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,722,209 | 3.845% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,017,562 | 2.993% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,436,420 | 2.400% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,531,946 | 2.192% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,519,642 | 2.189% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,519 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,741,933 | 1.780% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,982,918 | 1.606% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,614 | 1.603% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `J1to3BCFP8M2EcgS2VWRRuUzGcZScpnBVtcFYfqHpyqV` | 500,000 | 459,643,077 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 234,313 | 462,239,999 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 194,072 | 465,663,873 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 134,947 | 466,294,271 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 70,761 | 465,263,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `dzufrE42PJjNNRBstdmunAdeDToDA3Cax6WDpFVj36Y` | 35,979 | 466,277,855 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,837 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $89.74 | -0.35% 24h ↓ |
| Market cap | $53.03B | |
| Spot volume 24h | $1.77B | |
| DeFi TVL | $5.22B | -0.72% 1d / -4.19% 7d / -18.42% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.45B | |
| Stablecoin supply (all pegs) | $14.53B | |
| DEX volume 24h | $1.86B | -15.59% 1d |
| DEX volume 7d / 30d | $10.83B / $56.02B | |
| Fees + app revenue 24h | $9.38M | -3.36% 1d |
| Circulating supply | 590,982,541 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $231.07M | 12.45% |
| Tessera V | $197.03M | 10.62% |
| Orca DEX | $190.54M | 10.27% |
| Meteora DLMM | $172.58M | 9.30% |
| Scorch | $147.40M | 7.94% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-06 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-06 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-06 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-06 |
| - | [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) | 2026-11-06 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-11-05 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-11-04 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-07T10:42:16Z | Change |
|---|---|---|---|
| SOL price | $107 | $90 | -16.47% |
| DeFi TVL | $5.94B | $5.22B | -12.15% |
| Stablecoin supply | $15.97B | $14.45B | -9.56% |
| DEX volume 24h | $3.63B | $1.86B | -48.91% |
| Mean TPS | 3,288 | 1,072 | -67.38% |
| Active validators | 689 | 660 | -4.21% |
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
