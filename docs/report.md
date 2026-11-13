# Solana Ecosystem Report

_Generated 2026-11-13T11:36:59Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-13T11:36:59Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.29s |
| Snapshots in history | 631 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,206 non-vote TPS** (1,206 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **659 active validators** (40 delinquent, holding 0.157% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $80.37** (-2.55% over 24h), market cap $47.54B.
- **DeFi TVL $4.95B** (-5.91% 7d, -17.50% 30d), against $13.90B of stablecoins settled on Solana.
- **$1.50B of DEX volume in 24h** across 141 protocols, generating $8.33M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 40 | 13 +/- 5.93 (median of last 630) | Delinquent validators is 40, 4.6 robust standard deviations above its recent median of 13 (+207.7%). |
| 🟠 warning | SOL price | 80.37 | $104 +/- $6 (median of last 624) | SOL price is $80, 3.9 robust standard deviations below its recent median of $104 (-22.6%). |
| 🟠 warning | DeFi TVL | 4949266972 | $5,907,625,094 +/- $289,268,099 (median of last 629) | DeFi TVL is $4,949,266,972, 3.3 robust standard deviations below its recent median of $5,907,625,094 (-16.2%). |
| 🟠 warning | Stablecoin supply | 13899212536.14 | $15,895,572,069 +/- $529,507,096 (median of last 630) | Stablecoin supply is $13,899,212,536, 3.8 robust standard deviations below its recent median of $15,895,572,069 (-12.6%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1085 (44.48% complete) |
| Slot | 192,163 of 432,000 in epoch |
| Absolute slot | 468,912,163 |
| Block height | 446,927,373 |
| Lifetime transactions | 566,496,808,939 |
| TPS (now / mean / peak) | 1,151 / 1,206 / 1,594 |
| True TPS, non-vote (now / mean) | 1,151 / 1,206 |
| Slot time (mean / worst) | 0.215s / 0.222s |

Epoch 1085 has **239,837 slots remaining**, about **14h 19m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 40 (5.72% delinquent) |
| Total stake | 432,410,499 SOL |
| Delinquent stake | 678,732 SOL (0.157%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.89% / 24.54% |
| Commission (mean / median) | 12.46% / 5% |
| Zero-commission validators | 224 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,755 | 3.889% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,140,175 | 3.733% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,976,229 | 3.001% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,722 | 2.340% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,699,456 | 2.243% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,578,398 | 2.215% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,076 | 2.137% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,863,387 | 1.819% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,989,060 | 1.616% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,712,617 | 1.552% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 214,586 | 462,239,999 |
| `EtMSc3MvcDXUr6ChK5GxyFVwTxYA3zqP5XzjE9jwKvSV` | 108,633 | 468,833,014 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 80,386 | 467,356,299 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 79,941 | 467,356,334 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 52,342 | 468,719,999 |
| `reyYoUdFgtDLxAWW1hyn5xk2PHstA3j8zUrerQi9Ayq` | 42,479 | 468,719,999 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `6M6vB2thgACsfHHuk5KZPdWqSJivm9mArVLxKXynBGbS` | 10,634 | 0 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $80.37 | -2.55% 24h ↓ |
| Market cap | $47.54B | |
| Spot volume 24h | $3.47B | |
| DeFi TVL | $4.95B | -1.72% 1d / -5.91% 7d / -17.50% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.90B | |
| Stablecoin supply (all pegs) | $13.98B | |
| DEX volume 24h | $1.50B | -7.43% 1d |
| DEX volume 7d / 30d | $9.38B / $52.83B | |
| Fees + app revenue 24h | $8.33M | -18.17% 1d |
| Circulating supply | 591,511,041 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $290.16M | 19.38% |
| Orca DEX | $242.91M | 16.22% |
| BisonFi | $147.27M | 9.83% |
| Meteora DLMM | $144.66M | 9.66% |
| Raydium AMM | $138.98M | 9.28% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-12 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-12 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-09 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-13T11:36:59Z | Change |
|---|---|---|---|
| SOL price | $107 | $80 | -25.20% |
| DeFi TVL | $5.94B | $4.95B | -16.74% |
| Stablecoin supply | $15.97B | $13.90B | -12.99% |
| DEX volume 24h | $3.63B | $1.50B | -58.77% |
| Mean TPS | 3,288 | 1,206 | -63.32% |
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
