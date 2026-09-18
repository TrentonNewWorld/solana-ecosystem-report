# Solana Ecosystem Report

_Generated 2026-09-18T23:16:31Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-18T23:16:31Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.68s |
| Snapshots in history | 217 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **2,229 non-vote TPS** (4,758 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.266s**.
- **677 active validators** (11 delinquent, holding 0.036% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $113.34** (+11.66% over 24h), market cap $66.57B.
- **DeFi TVL $6.29B** (+9.30% 7d, +28.07% 30d), against $15.49B of stablecoins settled on Solana.
- **$2.59B of DEX volume in 24h** across 124 protocols, generating $14.68M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6286014116 | $5,889,229,234 +/- $79,340,222 (median of last 216) | DeFi TVL is $6,286,014,116, 5.0 robust standard deviations above its recent median of $5,889,229,234 (+6.7%). |
| 🟠 warning | SOL 24h change | 11.66 | |change| < 10% | SOL moved +11.66% in 24h. |
| 🟠 warning | SOL price | 113.34 | $103 +/- $3 (median of last 216) | SOL price is $113, 3.6 robust standard deviations above its recent median of $103 (+10.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1037 (56.73% complete) |
| Slot | 245,089 of 432,000 in epoch |
| Absolute slot | 448,229,089 |
| Block height | 426,269,976 |
| Lifetime transactions | 549,974,188,508 |
| TPS (now / mean / peak) | 5,209 / 4,758 / 5,271 |
| True TPS, non-vote (now / mean) | 2,678 / 2,229 |
| Slot time (mean / worst) | 0.266s / 0.275s |

Epoch 1037 has **186,911 slots remaining**, about **13h 48m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 11 (1.60% delinquent) |
| Total stake | 439,612,408 SOL |
| Delinquent stake | 158,570 SOL (0.036%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.05% / 24.27% |
| Commission (mean / median) | 12.53% / 5% |
| Zero-commission validators | 240 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,815,472 | 4.053% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,816,148 | 3.598% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,510,308 | 2.846% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,398,202 | 2.593% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,784,908 | 2.226% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,526 | 2.105% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,077,527 | 2.065% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,397,869 | 1.683% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,085,578 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,940 | 1.492% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `3r5ZXC1yFqMmk8VwDdUJbEdPmZ8KZvEkzd5ThEYRetTk` | 128,297 | 446,560,438 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,658 | 447,595,236 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,813 | 448,061,114 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,261 | 448,011,673 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 808 | 448,146,814 |
| `Luck3DN3HhkV6oc7rPQ1hYGgU3b5AhdKW9o1ob6AyU9` | 114 | 375,618,479 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 99 | 446,995,996 |
| `AGXZemZbyZjz5NBhufcob2pf8AXnr9HaGFUGNCfooWrB` | 6 | 402,784,479 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 2 | 384,048,870 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $113.34 | +11.66% 24h ↑ |
| Market cap | $66.57B | |
| Spot volume 24h | $6.60B | |
| DeFi TVL | $6.29B | +8.72% 1d / +9.30% 7d / +28.07% 30d |
| TVL 90-day peak | $6.29B | |
| Stablecoin supply (USD peg) | $15.49B | |
| Stablecoin supply (all pegs) | $15.56B | |
| DEX volume 24h | $2.59B | -7.41% 1d |
| DEX volume 7d / 30d | $17.44B / $80.48B | |
| Fees + app revenue 24h | $14.68M | -1.45% 1d |
| Circulating supply | 587,296,736 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $420.24M | 16.21% |
| BisonFi | $378.33M | 14.60% |
| PumpSwap | $329.29M | 12.70% |
| HumidiFi | $281.64M | 10.87% |
| Orca DEX | $235.25M | 9.08% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-18 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-18 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-18 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-18 |
| SIMD-558 | [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) | 2026-09-18 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-17 |
| SIMD-643 | [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) _(draft)_ | 2026-09-17 |
| SIMD-123 | [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) | 2026-09-16 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-alpha.5`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | Release v4.4.0-alpha.5 | 2026-09-18 |
| [`v4.3.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | Release v4.3.0 | 2026-09-18 |
| [`v4.3.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | Release v4.3.0-rc.1 | 2026-09-11 |
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-18T23:16:31Z | Change |
|---|---|---|---|
| SOL price | $107 | $113 | +5.49% |
| DeFi TVL | $5.94B | $6.29B | +5.74% |
| Stablecoin supply | $15.97B | $15.49B | -3.01% |
| DEX volume 24h | $3.63B | $2.59B | -28.63% |
| Mean TPS | 3,288 | 4,758 | +44.71% |
| Active validators | 689 | 677 | -1.74% |
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
