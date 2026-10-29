# Solana Ecosystem Report

_Generated 2026-10-29T21:46:52Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-29T21:46:52Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.97s |
| Snapshots in history | 537 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **3,244 non-vote TPS** (3,244 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **666 active validators** (23 delinquent, holding 0.737% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $97.28** (-4.97% over 24h), market cap $57.38B.
- **DeFi TVL $5.63B** (-5.61% 7d, -12.16% 30d), against $15.13B of stablecoins settled on Solana.
- **$1.73B of DEX volume in 24h** across 139 protocols, generating $10.35M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.737 | 0.031% +/- 0.033% (median of last 536) | Delinquent stake is 0.737%, 21.2 robust standard deviations above its recent median of 0.031% (+2277.4%). |
| 🟠 warning | Delinquent validators | 23 | 12 +/- 2.965 (median of last 536) | Delinquent validators is 23, 3.7 robust standard deviations above its recent median of 12 (+91.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1071 (84.62% complete) |
| Slot | 365,562 of 432,000 in epoch |
| Absolute slot | 463,037,562 |
| Block height | 441,060,784 |
| Lifetime transactions | 564,363,989,915 |
| TPS (now / mean / peak) | 2,282 / 3,244 / 4,804 |
| True TPS, non-vote (now / mean) | 2,282 / 3,244 |
| Slot time (mean / worst) | 0.214s / 0.218s |

Epoch 1071 has **66,438 slots remaining**, about **3h 56m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 23 (3.34% delinquent) |
| Total stake | 436,776,187 SOL |
| Delinquent stake | 3,220,997 SOL (0.737%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.90% / 24.53% |
| Commission (mean / median) | 13.04% / 5.0% |
| Zero-commission validators | 228 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,028,574 | 3.899% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,665,444 | 3.816% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,878,826 | 2.949% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,762,073 | 2.464% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,705,356 | 2.222% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,646 | 2.167% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,110 | 2.110% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,761,555 | 1.777% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,998,037 | 1.602% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,646,428 | 1.522% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,526,587 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,312 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 792,800 | 462,239,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 83,867 | 462,239,999 |
| `48Za4qpPrYz7v7aDhPhjHZwh7ahtWkye8vjqDYEUy9iV` | 20,448 | 0 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,613 | 461,807,999 |
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 290 | 0 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |
| `37BPVW1Ne1XHrzK15xguAS2BTdobVfThDzTE2mv8SsnJ` | 2 | 408,332,659 |
| `F3Bv6jaD8dAK8UwTshyKbji58fUDWUP36oee8hu53pRP` | 2 | 0 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $97.28 | -4.97% 24h ↓ |
| Market cap | $57.38B | |
| Spot volume 24h | $3.86B | |
| DeFi TVL | $5.63B | -1.15% 1d / -5.61% 7d / -12.16% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.13B | |
| Stablecoin supply (all pegs) | $15.19B | |
| DEX volume 24h | $1.73B | +9.50% 1d |
| DEX volume 7d / 30d | $12.30B / $60.78B | |
| Fees + app revenue 24h | $10.35M | -7.89% 1d |
| Circulating supply | 589,983,594 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $245.70M | 14.17% |
| BisonFi | $205.55M | 11.86% |
| Raydium AMM | $171.26M | 9.88% |
| Manifest Trade | $154.95M | 8.94% |
| Tessera V | $148.18M | 8.55% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-10-29 |
| SIMD-685 | [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) | 2026-10-29 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-29 |
| SIMD-568 | [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) | 2026-10-29 |
| SIMD-706 | [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-10-28 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-10-27 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-10-27 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-10-27 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-10-29T21:46:52Z | Change |
|---|---|---|---|
| SOL price | $107 | $97 | -9.46% |
| DeFi TVL | $5.94B | $5.63B | -5.33% |
| Stablecoin supply | $15.97B | $15.13B | -5.31% |
| DEX volume 24h | $3.63B | $1.73B | -52.28% |
| Mean TPS | 3,288 | 3,244 | -1.31% |
| Active validators | 689 | 666 | -3.34% |
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
