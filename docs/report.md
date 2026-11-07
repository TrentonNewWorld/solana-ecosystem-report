# Solana Ecosystem Report

_Generated 2026-11-07T16:59:56Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-07T16:59:56Z` |
| Sources healthy | 8 of 8 |
| Collection time | 11.69s |
| Snapshots in history | 596 |
| Anomalies flagged | 1 (1 critical) |

## At a glance

- The network is processing **1,557 non-vote TPS** (1,557 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **663 active validators** (34 delinquent, holding 0.152% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $89.47** (-1.24% over 24h), market cap $52.88B.
- **DeFi TVL $5.21B** (-4.39% 7d, -18.58% 30d), against $14.58B of stablecoins settled on Solana.
- **$1.48B of DEX volume in 24h** across 141 protocols, generating $9.27M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent validators | 34 | 12 +/- 4.448 (median of last 595) | Delinquent validators is 34, 4.9 robust standard deviations above its recent median of 12 (+183.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1080 (6.57% complete) |
| Slot | 28,372 of 432,000 in epoch |
| Absolute slot | 466,588,372 |
| Block height | 444,606,965 |
| Lifetime transactions | 565,667,519,793 |
| TPS (now / mean / peak) | 1,471 / 1,557 / 2,092 |
| True TPS, non-vote (now / mean) | 1,471 / 1,557 |
| Slot time (mean / worst) | 0.214s / 0.218s |

Epoch 1080 has **403,628 slots remaining**, about **23h 59m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 34 (4.88% delinquent) |
| Total stake | 434,780,965 SOL |
| Delinquent stake | 660,479 SOL (0.152%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.92% / 24.63% |
| Commission (mean / median) | 12.98% / 5% |
| Zero-commission validators | 223 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,043,402 | 3.920% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,729,016 | 3.848% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,015,291 | 2.994% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,277,563 | 2.364% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,558,411 | 2.198% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,520,070 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,242,930 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,750,589 | 1.783% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,983,623 | 1.606% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,973,337 | 1.604% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,555 | 462,239,999 |
| `57GUg9QH2LFMV11oaduuoqVJ5qHDEp7EGJ2xgkGiqAum` | 140,397 | 465,663,873 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 134,485 | 466,294,271 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 70,733 | 465,263,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `dzufrE42PJjNNRBstdmunAdeDToDA3Cax6WDpFVj36Y` | 31,154 | 466,277,855 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,836 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 527 | 462,239,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $89.47 | -1.24% 24h ↓ |
| Market cap | $52.88B | |
| Spot volume 24h | $1.06B | |
| DeFi TVL | $5.21B | -0.92% 1d / -4.39% 7d / -18.58% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.58B | |
| Stablecoin supply (all pegs) | $14.66B | |
| DEX volume 24h | $1.48B | -32.68% 1d |
| DEX volume 7d / 30d | $11.66B / $56.85B | |
| Fees + app revenue 24h | $9.27M | -4.43% 1d |
| Circulating supply | 591,038,333 SOL (92.76% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $170.16M | 11.50% |
| Tessera V | $153.42M | 10.37% |
| Meteora DLMM | $128.65M | 8.69% |
| Orca DEX | $108.65M | 7.34% |
| pump.fun | $108.28M | 7.32% |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-07T16:59:56Z | Change |
|---|---|---|---|
| SOL price | $107 | $89 | -16.73% |
| DeFi TVL | $5.94B | $5.21B | -12.33% |
| Stablecoin supply | $15.97B | $14.58B | -8.75% |
| DEX volume 24h | $3.63B | $1.48B | -59.25% |
| Mean TPS | 3,288 | 1,557 | -52.63% |
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
