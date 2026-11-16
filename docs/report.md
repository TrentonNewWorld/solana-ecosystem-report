# Solana Ecosystem Report

_Generated 2026-11-16T07:56:41Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-16T07:56:41Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.35s |
| Snapshots in history | 651 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,282 non-vote TPS** (1,282 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (37 delinquent, holding 0.035% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $71.36** (+2.22% over 24h), market cap $42.22B.
- **DeFi TVL $4.67B** (-8.40% 7d, -21.02% 30d), against $13.96B of stablecoins settled on Solana.
- **$1.54B of DEX volume in 24h** across 142 protocols, generating $7.30M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 71.36 | $104 +/- $6 (median of last 643) | SOL price is $71, 5.3 robust standard deviations below its recent median of $104 (-31.2%). |
| 🟠 warning | Delinquent validators | 37 | 13 +/- 5.93 (median of last 650) | Delinquent validators is 37, 4.0 robust standard deviations above its recent median of 13 (+184.6%). |
| 🟠 warning | DeFi TVL | 4666598585 | $5,901,435,967 +/- $299,545,234 (median of last 649) | DeFi TVL is $4,666,598,585, 4.1 robust standard deviations below its recent median of $5,901,435,967 (-20.9%). |
| 🟠 warning | Stablecoin supply | 13955443358.21 | $15,869,312,106 +/- $537,793,790 (median of last 650) | Stablecoin supply is $13,955,443,358, 3.6 robust standard deviations below its recent median of $15,869,312,106 (-12.1%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1088 (9.18% complete) |
| Slot | 39,647 of 432,000 in epoch |
| Absolute slot | 470,055,647 |
| Block height | 448,070,585 |
| Lifetime transactions | 566,914,834,854 |
| TPS (now / mean / peak) | 1,579 / 1,282 / 2,247 |
| True TPS, non-vote (now / mean) | 1,579 / 1,282 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1088 has **392,353 slots remaining**, about **23h 25m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 (5.29% delinquent) |
| Total stake | 429,145,034 SOL |
| Delinquent stake | 152,189 SOL (0.035%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.95% / 24.77% |
| Commission (mean / median) | 12.59% / 5.0% |
| Zero-commission validators | 221 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,936,855 | 3.947% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,432,361 | 3.829% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,687 | 2.910% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,142,842 | 2.363% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,787,748 | 2.281% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,620,150 | 2.242% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,212,350 | 2.147% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,959,108 | 1.855% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,992,227 | 1.629% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,709,566 | 1.563% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `fuyugZxM5S4NyV3ZYoc6ebs3fmRTrZ3X27MKCFvHpVD` | 68,080 | 470,015,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,516 | 469,583,999 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 23,779 | 467,855,999 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 13,483 | 467,356,299 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 5,493 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,640 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |
| `PEBBLETUXFPdrwm5heff4x1VsrypGS1fNSRPEF6LiZL` | 162 | 466,127,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $71.36 | +2.22% 24h ↑ |
| Market cap | $42.22B | |
| Spot volume 24h | $2.99B | |
| DeFi TVL | $4.67B | +0.86% 1d / -8.40% 7d / -21.02% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.96B | |
| Stablecoin supply (all pegs) | $14.04B | |
| DEX volume 24h | $1.54B | -8.79% 1d |
| DEX volume 7d / 30d | $9.89B / $49.70B | |
| Fees + app revenue 24h | $7.30M | -7.09% 1d |
| Circulating supply | 591,684,547 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $236.69M | 15.33% |
| Orca DEX | $172.21M | 11.16% |
| Meteora DLMM | $154.87M | 10.03% |
| PumpSwap | $142.79M | 9.25% |
| Scorch | $131.54M | 8.52% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-16T07:56:41Z | Change |
|---|---|---|---|
| SOL price | $107 | $71 | -33.58% |
| DeFi TVL | $5.94B | $4.67B | -21.50% |
| Stablecoin supply | $15.97B | $13.96B | -12.64% |
| DEX volume 24h | $3.63B | $1.54B | -57.50% |
| Mean TPS | 3,288 | 1,282 | -60.99% |
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
