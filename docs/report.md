# Solana Ecosystem Report

_Generated 2026-11-08T21:06:55Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-08T21:06:55Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.59s |
| Snapshots in history | 605 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,694 non-vote TPS** (1,694 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **660 active validators** (37 delinquent, holding 0.166% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $89.02** (+0.12% over 24h), market cap $52.63B.
- **DeFi TVL $5.19B** (-4.03% 7d, -15.71% 30d), against $14.55B of stablecoins settled on Solana.
- **$917.44M of DEX volume in 24h** across 141 protocols, generating $8.03M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 37 | 12 +/- 4.448 (median of last 604) | Delinquent validators is 37, 5.6 robust standard deviations above its recent median of 12 (+208.3%). |
| 🟠 warning | Delinquent stake | 0.166 | 0.036% +/- 0.042% (median of last 604) | Delinquent stake is 0.166%, 3.1 robust standard deviations above its recent median of 0.036% (+361.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1081 (15.73% complete) |
| Slot | 67,950 of 432,000 in epoch |
| Absolute slot | 467,059,950 |
| Block height | 445,078,107 |
| Lifetime transactions | 565,813,046,638 |
| TPS (now / mean / peak) | 1,637 / 1,694 / 2,392 |
| True TPS, non-vote (now / mean) | 1,637 / 1,694 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1081 has **364,050 slots remaining**, about **21h 44m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 37 (5.31% delinquent) |
| Total stake | 433,920,561 SOL |
| Delinquent stake | 720,051 SOL (0.166%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.93% / 24.63% |
| Commission (mean / median) | 12.88% / 5.0% |
| Zero-commission validators | 222 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,050,553 | 3.929% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,720,131 | 3.853% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,021,912 | 3.001% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,279,070 | 2.369% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,388 | 2.202% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,550,278 | 2.201% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,876 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,775,137 | 1.792% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,980,319 | 1.609% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,711,284 | 1.547% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,550 | 462,239,999 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 132,359 | 466,294,271 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 100,939 | 465,663,873 |
| `H1kyn75BFTXr8QRmToRRvuEEmYan5n6M5APyfhMLau3b` | 93,439 | 467,059,847 |
| `FH9xcL7Fqkreq1wSkn2Vf7AfnMEyo2KK7QX32LTFndt6` | 68,837 | 466,991,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 40,426 | 465,263,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,836 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $89.02 | +0.12% 24h ↑ |
| Market cap | $52.63B | |
| Spot volume 24h | $956.21M | |
| DeFi TVL | $5.19B | -0.66% 1d / -4.03% 7d / -15.71% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.55B | |
| Stablecoin supply (all pegs) | $14.64B | |
| DEX volume 24h | $917.44M | -38.01% 1d |
| DEX volume 7d / 30d | $11.62B / $55.12B | |
| Fees + app revenue 24h | $8.03M | -8.71% 1d |
| Circulating supply | 591,093,739 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $217.32M | 23.69% |
| pump.fun | $87.46M | 9.53% |
| BisonFi | $80.20M | 8.74% |
| Meteora DLMM | $79.23M | 8.64% |
| Raydium AMM | $79.08M | 8.62% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-08T21:06:55Z | Change |
|---|---|---|---|
| SOL price | $107 | $89 | -17.14% |
| DeFi TVL | $5.94B | $5.19B | -12.67% |
| Stablecoin supply | $15.97B | $14.55B | -8.89% |
| DEX volume 24h | $3.63B | $917.44M | -74.74% |
| Mean TPS | 3,288 | 1,694 | -48.48% |
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
