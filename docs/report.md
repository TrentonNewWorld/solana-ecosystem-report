# Solana Ecosystem Report

_Generated 2026-11-15T23:31:31Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-15T23:31:31Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.32s |
| Snapshots in history | 649 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,956 non-vote TPS** (1,956 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (38 delinquent, holding 0.084% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $72.39** (+4.53% over 24h), market cap $42.83B.
- **DeFi TVL $4.69B** (-9.43% 7d, -21.32% 30d), against $13.98B of stablecoins settled on Solana.
- **$1.68B of DEX volume in 24h** across 142 protocols, generating $7.95M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 72.39 | $104 +/- $6 (median of last 641) | SOL price is $72, 5.2 robust standard deviations below its recent median of $104 (-30.3%). |
| 🟠 warning | Delinquent validators | 38 | 13 +/- 5.93 (median of last 648) | Delinquent validators is 38, 4.2 robust standard deviations above its recent median of 13 (+192.3%). |
| 🟠 warning | DeFi TVL | 4693343574 | $5,901,845,828 +/- $297,778,237 (median of last 647) | DeFi TVL is $4,693,343,574, 4.1 robust standard deviations below its recent median of $5,901,845,828 (-20.5%). |
| 🟠 warning | Stablecoin supply | 13977358003.17 | $15,870,687,722 +/- $536,603,287 (median of last 648) | Stablecoin supply is $13,977,358,003, 3.5 robust standard deviations below its recent median of $15,870,687,722 (-11.9%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1087 (76.54% complete) |
| Slot | 330,657 of 432,000 in epoch |
| Absolute slot | 469,914,657 |
| Block height | 447,929,611 |
| Lifetime transactions | 566,865,528,187 |
| TPS (now / mean / peak) | 1,969 / 1,956 / 2,864 |
| True TPS, non-vote (now / mean) | 1,969 / 1,956 |
| Slot time (mean / worst) | 0.215s / 0.225s |

Epoch 1087 has **101,343 slots remaining**, about **6h 3m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 38 (5.43% delinquent) |
| Total stake | 429,328,621 SOL |
| Delinquent stake | 360,787 SOL (0.084%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.94% / 24.77% |
| Commission (mean / median) | 12.74% / 5.0% |
| Zero-commission validators | 220 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,927,749 | 3.943% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,404,544 | 3.821% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,614,561 | 2.938% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,141,932 | 2.362% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,754,208 | 2.272% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,640,656 | 2.246% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,204,466 | 2.144% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,943,264 | 1.850% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,232 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,708,648 | 1.563% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 209,256 | 462,239,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,516 | 469,583,999 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 13,483 | 467,356,299 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 12,795 | 467,356,334 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,640 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $72.39 | +4.53% 24h ↑ |
| Market cap | $42.83B | |
| Spot volume 24h | $4.26B | |
| DeFi TVL | $4.69B | -3.29% 1d / -9.43% 7d / -21.32% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.98B | |
| Stablecoin supply (all pegs) | $14.06B | |
| DEX volume 24h | $1.68B | +7.52% 1d |
| DEX volume 7d / 30d | $10.23B / $51.16B | |
| Fees + app revenue 24h | $7.95M | -13.93% 1d |
| Circulating supply | 591,628,949 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $236.69M | 14.11% |
| Orca DEX | $233.21M | 13.90% |
| PumpSwap | $156.41M | 9.32% |
| Meteora DLMM | $154.87M | 9.23% |
| Scorch | $131.54M | 7.84% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-14 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-14 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-12 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-12 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-15T23:31:31Z | Change |
|---|---|---|---|
| SOL price | $107 | $72 | -32.62% |
| DeFi TVL | $5.94B | $4.69B | -21.05% |
| Stablecoin supply | $15.97B | $13.98B | -12.50% |
| DEX volume 24h | $3.63B | $1.68B | -53.80% |
| Mean TPS | 3,288 | 1,956 | -40.51% |
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
