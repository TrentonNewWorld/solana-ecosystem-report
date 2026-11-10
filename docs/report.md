# Solana Ecosystem Report

_Generated 2026-11-10T21:26:20Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-10T21:26:20Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.04s |
| Snapshots in history | 616 |
| Anomalies flagged | 4 (2 critical) |

## At a glance

- The network is processing **1,893 non-vote TPS** (1,893 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.213s**.
- **657 active validators** (42 delinquent, holding 1.382% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $83.33** (-3.55% over 24h), market cap $49.27B.
- **DeFi TVL $4.98B** (-7.87% 7d, -19.21% 30d), against $14.46B of stablecoins settled on Solana.
- **$1.49B of DEX volume in 24h** across 141 protocols, generating $9.38M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 1.382 | 0.036% +/- 0.043% (median of last 615) | Delinquent stake is 1.382%, 31.3 robust standard deviations above its recent median of 0.036% (+3738.9%). |
| 🔴 critical | Delinquent validators | 42 | 12 +/- 4.448 (median of last 615) | Delinquent validators is 42, 6.7 robust standard deviations above its recent median of 12 (+250.0%). |
| 🟠 warning | SOL price | 83.33 | $104 +/- $6 (median of last 609) | SOL price is $83, 3.5 robust standard deviations below its recent median of $104 (-19.9%). |
| 🟠 warning | DeFi TVL | 4978482301 | $5,913,984,752 +/- $285,706,606 (median of last 614) | DeFi TVL is $4,978,482,301, 3.3 robust standard deviations below its recent median of $5,913,984,752 (-15.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1083 (3.52% complete) |
| Slot | 15,198 of 432,000 in epoch |
| Absolute slot | 467,871,198 |
| Block height | 445,887,985 |
| Lifetime transactions | 566,093,711,389 |
| TPS (now / mean / peak) | 1,517 / 1,893 / 2,768 |
| True TPS, non-vote (now / mean) | 1,517 / 1,893 |
| Slot time (mean / worst) | 0.213s / 0.222s |

Epoch 1083 has **416,802 slots remaining**, about **24h 39m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 42 (6.01% delinquent) |
| Total stake | 433,423,964 SOL |
| Delinquent stake | 5,990,887 SOL (1.382%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.87% / 24.56% |
| Commission (mean / median) | 12.64% / 5% |
| Zero-commission validators | 221 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,764,485 | 3.868% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,564,685 | 3.822% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,031,625 | 3.007% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,254 | 2.334% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,644,051 | 2.225% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,571,015 | 2.208% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,999 | 2.130% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,330 | 1.803% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,248 | 1.612% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,729,845 | 1.553% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `2tucttroqFNXsrYeMBQ8LfzKNfgwT2rHBzAF6RzbbHEp` | 4,994,585 | 467,845,929 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,279 | 462,239,999 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 130,787 | 466,294,271 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 114,347 | 467,356,299 |
| `D3DfFvmLBKkX9JJNEpJRXpM1pYTVPQ5dpPQRc9F49xk4` | 103,553 | 467,423,999 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 101,016 | 467,356,334 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 99,936 | 465,663,873 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 80,223 | 467,855,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `reyYoUdFgtDLxAWW1hyn5xk2PHstA3j8zUrerQi9Ayq` | 42,479 | 467,423,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $83.33 | -3.55% 24h ↓ |
| Market cap | $49.27B | |
| Spot volume 24h | $2.99B | |
| DeFi TVL | $4.98B | -2.28% 1d / -7.87% 7d / -19.21% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.46B | |
| Stablecoin supply (all pegs) | $14.54B | |
| DEX volume 24h | $1.49B | +42.59% 1d |
| DEX volume 7d / 30d | $11.39B / $54.39B | |
| Fees + app revenue 24h | $9.38M | +12.88% 1d |
| Circulating supply | 591,204,668 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $256.08M | 17.21% |
| Orca DEX | $220.81M | 14.84% |
| BisonFi | $157.07M | 10.56% |
| Raydium AMM | $144.08M | 9.68% |
| Meteora DLMM | $122.68M | 8.25% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-10 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-06 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-09 |
| - | [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) | 2026-11-06 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-10T21:26:20Z | Change |
|---|---|---|---|
| SOL price | $107 | $83 | -22.44% |
| DeFi TVL | $5.94B | $4.98B | -16.25% |
| Stablecoin supply | $15.97B | $14.46B | -9.47% |
| DEX volume 24h | $3.63B | $1.49B | -59.04% |
| Mean TPS | 3,288 | 1,893 | -42.43% |
| Active validators | 689 | 657 | -4.64% |
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
