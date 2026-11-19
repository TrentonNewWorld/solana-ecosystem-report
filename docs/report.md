# Solana Ecosystem Report

_Generated 2026-11-19T22:46:06Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-19T22:46:06Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.35s |
| Snapshots in history | 668 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **2,433 non-vote TPS** (2,433 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.216s**.
- **659 active validators** (26 delinquent, holding 0.025% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $73.15** (+0.41% over 24h), market cap $43.28B.
- **DeFi TVL $4.69B** (-6.83% 7d, -19.54% 30d), against $12.99B of stablecoins settled on Solana.
- **$1.82B of DEX volume in 24h** across 144 protocols, generating $10.95M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | SOL price | 73.15 | $104 +/- $6 (median of last 660) | SOL price is $73, 4.7 robust standard deviations below its recent median of $104 (-29.4%). |
| 🔴 critical | Stablecoin supply | 12988118840.28 | $15,838,953,181 +/- $550,446,445 (median of last 667) | Stablecoin supply is $12,988,118,840, 5.2 robust standard deviations below its recent median of $15,838,953,181 (-18.0%). |
| 🟠 warning | DeFi TVL | 4692000499 | $5,898,048,908 +/- $313,915,923 (median of last 666) | DeFi TVL is $4,692,000,499, 3.8 robust standard deviations below its recent median of $5,898,048,908 (-20.4%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1091 (45.35% complete) |
| Slot | 195,898 of 432,000 in epoch |
| Absolute slot | 471,507,898 |
| Block height | 449,522,023 |
| Lifetime transactions | 567,494,914,833 |
| TPS (now / mean / peak) | 1,873 / 2,433 / 3,163 |
| True TPS, non-vote (now / mean) | 1,873 / 2,433 |
| Slot time (mean / worst) | 0.216s / 0.221s |

Epoch 1091 has **236,102 slots remaining**, about **14h 9m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 26 (3.80% delinquent) |
| Total stake | 428,682,730 SOL |
| Delinquent stake | 108,886 SOL (0.025%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.84% |
| Commission (mean / median) | 12.63% / 5% |
| Zero-commission validators | 219 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,960 | 3.972% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,375,745 | 3.820% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,025 | 2.898% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,299,570 | 2.403% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,431 | 2.290% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,573,248 | 2.233% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,578 | 2.152% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,980,784 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,844 | 1.632% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,772,455 | 1.580% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 42,980 | 471,311,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,450 | 469,583,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,421 | 470,879,999 |
| `Bwkz1ddKoGE8hgiSV6HZLXi9RBLqfBi3HZb2QujzVGgz` | 9 | 470,879,999 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 2 | 462,239,999 |
| `25yzQawc1qeAupemd5KLPSotLejVHLcpk7DGo4ityL86` | 2 | 470,447,999 |
| `GdFaSCpPf9RqRjxkvXUCzLR62bEjmEPZMS9XRVFC3pDu` | 2 | 469,698,063 |
| `5DutFKQ8qPmbjFEmp31QH9JDYJXvwh9pma8ap5Phxk6H` | 1 | 465,304,579 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 1 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $73.15 | +0.41% 24h ↑ |
| Market cap | $43.28B | |
| Spot volume 24h | $2.14B | |
| DeFi TVL | $4.69B | -2.21% 1d / -6.83% 7d / -19.54% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.99B | |
| Stablecoin supply (all pegs) | $13.07B | |
| DEX volume 24h | $1.82B | +20.25% 1d |
| DEX volume 7d / 30d | $10.91B / $50.39B | |
| Fees + app revenue 24h | $10.95M | +33.50% 1d |
| Circulating supply | 591,851,404 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $330.65M | 18.21% |
| Orca DEX | $250.71M | 13.81% |
| Meteora DLMM | $246.17M | 13.56% |
| Raydium AMM | $233.30M | 12.85% |
| BisonFi | $153.98M | 8.48% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-19 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-19 |
| SIMD-706 | [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-11-19 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-19 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-19 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-11-19 |
| SIMD-643 | [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) _(draft)_ | 2026-11-17 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-16 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v5.0.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | Release v5.0.0-alpha.1 | 2026-11-19 |
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-19T22:46:06Z | Change |
|---|---|---|---|
| SOL price | $107 | $73 | -31.92% |
| DeFi TVL | $5.94B | $4.69B | -21.07% |
| Stablecoin supply | $15.97B | $12.99B | -18.69% |
| DEX volume 24h | $3.63B | $1.82B | -50.02% |
| Mean TPS | 3,288 | 2,433 | -26.00% |
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
