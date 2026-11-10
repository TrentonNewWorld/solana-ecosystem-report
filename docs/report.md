# Solana Ecosystem Report

_Generated 2026-11-10T03:31:39Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-10T03:31:39Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.75s |
| Snapshots in history | 613 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,318 non-vote TPS** (1,318 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **657 active validators** (41 delinquent, holding 0.224% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $85.65** (-2.34% over 24h), market cap $50.64B.
- **DeFi TVL $5.06B** (-6.40% 7d, -17.92% 30d), against $14.46B of stablecoins settled on Solana.
- **$1.29B of DEX volume in 24h** across 141 protocols, generating $9.49M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 41 | 12 +/- 4.448 (median of last 612) | Delinquent validators is 41, 6.5 robust standard deviations above its recent median of 12 (+241.7%). |
| 🟠 warning | Delinquent stake | 0.224 | 0.036% +/- 0.043% (median of last 612) | Delinquent stake is 0.224%, 4.4 robust standard deviations above its recent median of 0.036% (+522.2%). |
| 🟠 warning | SOL price | 85.65 | $104 +/- $6 (median of last 606) | SOL price is $86, 3.2 robust standard deviations below its recent median of $104 (-17.7%). |
| 🟠 warning | DeFi TVL | 5058181502 | $5,914,106,062 +/- $285,199,403 (median of last 611) | DeFi TVL is $5,058,181,502, 3.0 robust standard deviations below its recent median of $5,914,106,062 (-14.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1082 (33.81% complete) |
| Slot | 146,076 of 432,000 in epoch |
| Absolute slot | 467,570,076 |
| Block height | 445,587,736 |
| Lifetime transactions | 565,988,073,057 |
| TPS (now / mean / peak) | 1,128 / 1,318 / 1,729 |
| True TPS, non-vote (now / mean) | 1,128 / 1,318 |
| Slot time (mean / worst) | 0.214s / 0.22s |

Epoch 1082 has **285,924 slots remaining**, about **16h 59m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 41 (5.87% delinquent) |
| Total stake | 434,984,472 SOL |
| Delinquent stake | 976,204 SOL (0.224%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.88% / 24.57% |
| Commission (mean / median) | 12.65% / 5% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,898,208 | 3.885% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,746,254 | 3.850% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,034,244 | 2.996% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,280,950 | 2.364% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,598,549 | 2.207% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,851 | 2.196% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,233,159 | 2.123% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,813,316 | 1.796% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,971 | 1.606% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,712,231 | 1.543% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,279 | 462,239,999 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 132,270 | 466,294,271 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 114,837 | 467,356,299 |
| `D3DfFvmLBKkX9JJNEpJRXpM1pYTVPQ5dpPQRc9F49xk4` | 103,549 | 467,423,999 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 100,944 | 467,356,334 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 99,936 | 465,663,873 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 42,895 | 467,423,999 |
| `reyYoUdFgtDLxAWW1hyn5xk2PHstA3j8zUrerQi9Ayq` | 42,479 | 467,423,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 40,432 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $85.65 | -2.34% 24h ↓ |
| Market cap | $50.64B | |
| Spot volume 24h | $2.26B | |
| DeFi TVL | $5.06B | -0.61% 1d / -6.40% 7d / -17.92% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.46B | |
| Stablecoin supply (all pegs) | $14.54B | |
| DEX volume 24h | $1.29B | +24.05% 1d |
| DEX volume 7d / 30d | $10.70B / $53.70B | |
| Fees + app revenue 24h | $9.49M | +14.37% 1d |
| Circulating supply | 591,149,190 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $256.08M | 19.79% |
| Orca DEX | $220.93M | 17.07% |
| Raydium AMM | $152.71M | 11.80% |
| BisonFi | $103.44M | 7.99% |
| Meteora DLMM | $97.96M | 7.57% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-09 |
| SIMD-326 | [Amend SIMD-0326: define BLS validator ranks](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-09 |
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

| Metric | 2026-08-28T06:17:33Z | 2026-11-10T03:31:39Z | Change |
|---|---|---|---|
| SOL price | $107 | $86 | -20.28% |
| DeFi TVL | $5.94B | $5.06B | -14.91% |
| Stablecoin supply | $15.97B | $14.46B | -9.47% |
| DEX volume 24h | $3.63B | $1.29B | -64.37% |
| Mean TPS | 3,288 | 1,318 | -59.89% |
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
