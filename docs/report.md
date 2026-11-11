# Solana Ecosystem Report

_Generated 2026-11-11T11:28:15Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-11T11:28:15Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.42s |
| Snapshots in history | 620 |
| Anomalies flagged | 4 (2 critical) |

## At a glance

- The network is processing **1,178 non-vote TPS** (1,178 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **658 active validators** (41 delinquent, holding 0.230% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $83.87** (-0.65% over 24h), market cap $49.60B.
- **DeFi TVL $5.04B** (-6.47% 7d, -18.80% 30d), against $14.37B of stablecoins settled on Solana.
- **$1.34B of DEX volume in 24h** across 141 protocols, generating $8.23M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.23 | 0.036% +/- 0.043% (median of last 619) | Delinquent stake is 0.230%, 4.5 robust standard deviations above its recent median of 0.036% (+538.9%). |
| 🔴 critical | Delinquent validators | 41 | 13 +/- 5.93 (median of last 619) | Delinquent validators is 41, 4.7 robust standard deviations above its recent median of 13 (+215.4%). |
| 🟠 warning | SOL price | 83.87 | $104 +/- $6 (median of last 613) | SOL price is $84, 3.4 robust standard deviations below its recent median of $104 (-19.3%). |
| 🟠 warning | DeFi TVL | 5038033145 | $5,911,102,303 +/- $282,329,329 (median of last 618) | DeFi TVL is $5,038,033,145, 3.1 robust standard deviations below its recent median of $5,911,102,303 (-14.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1083 (58.01% complete) |
| Slot | 250,620 of 432,000 in epoch |
| Absolute slot | 468,106,620 |
| Block height | 446,123,006 |
| Lifetime transactions | 566,174,147,719 |
| TPS (now / mean / peak) | 1,143 / 1,178 / 1,566 |
| True TPS, non-vote (now / mean) | 1,143 / 1,178 |
| Slot time (mean / worst) | 0.215s / 0.218s |

Epoch 1083 has **181,380 slots remaining**, about **10h 49m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 658 / 41 (5.87% delinquent) |
| Total stake | 433,423,964 SOL |
| Delinquent stake | 996,302 SOL (0.230%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.87% / 24.56% |
| Commission (mean / median) | 12.78% / 5.0% |
| Zero-commission validators | 220 |

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
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,279 | 462,239,999 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 130,787 | 466,294,271 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 114,347 | 467,356,299 |
| `D3DfFvmLBKkX9JJNEpJRXpM1pYTVPQ5dpPQRc9F49xk4` | 103,553 | 467,423,999 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 101,016 | 467,356,334 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 99,936 | 465,663,873 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 80,223 | 467,855,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `reyYoUdFgtDLxAWW1hyn5xk2PHstA3j8zUrerQi9Ayq` | 42,479 | 467,423,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 40,435 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $83.87 | -0.65% 24h ↓ |
| Market cap | $49.60B | |
| Spot volume 24h | $2.91B | |
| DeFi TVL | $5.04B | -0.31% 1d / -6.47% 7d / -18.80% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.37B | |
| Stablecoin supply (all pegs) | $14.45B | |
| DEX volume 24h | $1.34B | -10.03% 1d |
| DEX volume 7d / 30d | $10.44B / $54.04B | |
| Fees + app revenue 24h | $8.23M | -10.30% 1d |
| Circulating supply | 591,408,424 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $232.59M | 17.38% |
| BisonFi | $152.62M | 11.40% |
| Meteora DLMM | $129.37M | 9.67% |
| Raydium AMM | $122.06M | 9.12% |
| PumpSwap | $94.39M | 7.05% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-11T11:28:15Z | Change |
|---|---|---|---|
| SOL price | $107 | $84 | -21.94% |
| DeFi TVL | $5.94B | $5.04B | -15.25% |
| Stablecoin supply | $15.97B | $14.37B | -10.06% |
| DEX volume 24h | $3.63B | $1.34B | -63.15% |
| Mean TPS | 3,288 | 1,178 | -64.17% |
| Active validators | 689 | 658 | -4.50% |
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
