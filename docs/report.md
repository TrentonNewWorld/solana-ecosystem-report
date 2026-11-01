# Solana Ecosystem Report

_Generated 2026-11-01T07:29:12Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-01T07:29:12Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.09s |
| Snapshots in history | 555 |
| Anomalies flagged | 3 (2 critical) |

## At a glance

- The network is processing **957 non-vote TPS** (957 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **663 active validators** (33 delinquent, holding 1.049% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $95.37** (-0.50% over 24h), market cap $56.28B.
- **DeFi TVL $5.41B** (-6.00% 7d, -16.09% 30d), against $15.15B of stablecoins settled on Solana.
- **$1.44B of DEX volume in 24h** across 139 protocols, generating $8.58M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 1.049 | 0.032% +/- 0.035% (median of last 554) | Delinquent stake is 1.049%, 29.2 robust standard deviations above its recent median of 0.032% (+3178.1%). |
| 🔴 critical | Delinquent validators | 33 | 12 +/- 4.448 (median of last 554) | Delinquent validators is 33, 4.7 robust standard deviations above its recent median of 12 (+175.0%). |
| 🟠 warning | Mean TPS | 957.0 | 4.24e+03 tx/s +/- 847 tx/s (median of last 554) | Mean TPS is 957 tx/s, 3.9 robust standard deviations below its recent median of 4.24e+03 tx/s (-77.4%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1074 (9.30% complete) |
| Slot | 40,167 of 432,000 in epoch |
| Absolute slot | 464,008,167 |
| Block height | 442,029,699 |
| Lifetime transactions | 564,688,771,463 |
| TPS (now / mean / peak) | 908 / 957 / 1,182 |
| True TPS, non-vote (now / mean) | 908 / 957 |
| Slot time (mean / worst) | 0.214s / 0.221s |

Epoch 1074 has **391,833 slots remaining**, about **23h 17m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 33 (4.74% delinquent) |
| Total stake | 433,943,288 SOL |
| Delinquent stake | 4,553,167 SOL (1.049%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.69% |
| Commission (mean / median) | 12.81% / 5% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,029,196 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,695,127 | 3.847% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,943,199 | 2.983% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,426,987 | 2.403% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,583,157 | 2.208% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,451,197 | 2.178% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,053 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,791,639 | 1.796% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,293 | 1.613% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,977,108 | 1.608% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `JEJzKYzyYJJjtn6Yb1P7r6YV75TdSNmmJT49sgDoHvmk` | 1,838,200 | 463,967,999 |
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,346,016 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,225 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 250,453 | 462,239,999 |
| `7K8DVxtNJGnMtUY1CQJT5jcs8sFGSZTDiG7kowvFpECh` | 145,759 | 463,535,999 |
| `5K8qgC9nHzKHSSyo9fKLsMfYmavYdMgEaYx86cMmVKVv` | 96,624 | 463,967,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 62,325 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 16,589 | 463,967,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 289 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $95.37 | -0.50% 24h ↓ |
| Market cap | $56.28B | |
| Spot volume 24h | $1.38B | |
| DeFi TVL | $5.41B | -0.66% 1d / -6.00% 7d / -16.09% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.15B | |
| Stablecoin supply (all pegs) | $15.23B | |
| DEX volume 24h | $1.44B | -31.85% 1d |
| DEX volume 7d / 30d | $11.80B / $58.08B | |
| Fees + app revenue 24h | $8.58M | -23.60% 1d |
| Circulating supply | 590,150,501 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $182.87M | 12.67% |
| Tessera V | $181.44M | 12.57% |
| PumpSwap | $130.68M | 9.06% |
| pump.fun | $113.64M | 7.88% |
| GoonFi | $108.02M | 7.49% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-567 | [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) | 2026-10-31 |
| SIMD-529 | [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) | 2026-10-31 |
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-10-30 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-10-30 |
| SIMD-685 | [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) | 2026-10-30 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-29 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-10-29 |
| SIMD-706 | [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-10-28 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |
| [`v4.4.0-beta.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | Release v4.4.0-beta.1 | 2026-10-13 |
| [`v4.5.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | Release v4.5.0-alpha.2 | 2026-10-08 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-01T07:29:12Z | Change |
|---|---|---|---|
| SOL price | $107 | $95 | -11.23% |
| DeFi TVL | $5.94B | $5.41B | -8.92% |
| Stablecoin supply | $15.97B | $15.15B | -5.18% |
| DEX volume 24h | $3.63B | $1.44B | -60.27% |
| Mean TPS | 3,288 | 957 | -70.89% |
| Active validators | 689 | 663 | -3.77% |
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
