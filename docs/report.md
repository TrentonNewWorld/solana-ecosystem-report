# Solana Ecosystem Report

_Generated 2026-11-27T09:38:49Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-27T09:38:49Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.77s |
| Snapshots in history | 704 |
| Anomalies flagged | 4 (1 critical) |

## At a glance

- The network is processing **1,102 non-vote TPS** (1,102 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **654 active validators** (34 delinquent, holding 0.060% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $73.7** (+3.70% over 24h), market cap $43.65B.
- **DeFi TVL $4.68B** (-0.66% 7d, -17.80% 30d), against $12.36B of stablecoins settled on Solana.
- **$1.23B of DEX volume in 24h** across 146 protocols, generating $6.15M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Stablecoin supply | 12362461883.93 | $15,782,254,283 +/- $587,563,156 (median of last 703) | Stablecoin supply is $12,362,461,884, 5.8 robust standard deviations below its recent median of $15,782,254,283 (-21.7%). |
| 🟠 warning | Delinquent validators | 34 | 13 +/- 5.93 (median of last 703) | Delinquent validators is 34, 3.5 robust standard deviations above its recent median of 13 (+161.5%). |
| 🟠 warning | SOL price | 73.7 | $103 +/- $8 (median of last 696) | SOL price is $74, 3.7 robust standard deviations below its recent median of $103 (-28.7%). |
| 🟠 warning | DeFi TVL | 4679779249 | $5,889,570,934 +/- $377,153,298 (median of last 702) | DeFi TVL is $4,679,779,249, 3.2 robust standard deviations below its recent median of $5,889,570,934 (-20.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1098 (38.61% complete) |
| Slot | 166,808 of 432,000 in epoch |
| Absolute slot | 474,502,808 |
| Block height | 452,515,488 |
| Lifetime transactions | 568,597,805,215 |
| TPS (now / mean / peak) | 1,193 / 1,102 / 1,354 |
| True TPS, non-vote (now / mean) | 1,193 / 1,102 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1098 has **265,192 slots remaining**, about **15h 50m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 34 (4.94% delinquent) |
| Total stake | 424,207,451 SOL |
| Delinquent stake | 255,036 SOL (0.060%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.96% / 24.96% |
| Commission (mean / median) | 13.0% / 5.0% |
| Zero-commission validators | 217 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,245 | 3.964% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,826,052 | 3.731% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,437,388 | 2.932% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,238,108 | 2.413% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,920,637 | 2.339% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,617,109 | 2.267% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,296,651 | 2.192% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,037,877 | 1.895% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,972,141 | 1.644% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,741,351 | 1.589% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `DG6fVEB2Qy1jntvHVPui3R12CMqcwNNnjYPYdsbQ9ACP` | 68,776 | 473,749,295 |
| `irKsY8c3sQur1XaYuQ811hzsEQJ5Hq3Yu3AAoXYnp8W` | 60,716 | 474,335,999 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 35,467 | 474,335,999 |
| `DrKHZXtuGhuYbe5MfigvCXR7VFd3u2wxepXei8m2GsDE` | 30,405 | 473,471,999 |
| `46mwXQRqWwj8Jp4ZR2tL1Yr3Snm99xDfKUs5jz7hLmEK` | 29,437 | 474,288,935 |
| `3Z1N2Fkfha4ThNiRwN8RnU6U8dkFJ92DH2TFyLWJf8cj` | 15,163 | 474,335,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 9,529 | 471,311,999 |
| `DqbRPQXbN8GDKWZkKiHnRjiSKPqE3rQaNgTPxdLGPDMK` | 3,090 | 473,903,999 |
| `Rn3ERP5cLVcB4oWRZpoujk5VRPM7SLrM2txPVHGYwn2` | 2,238 | 326,553,475 |
| `EMVmh5hF6LT1sZM9G7dEX1bykRYEymWY2vtE7QHBBAW6` | 125 | 472,608,648 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $73.7 | +3.70% 24h ↑ |
| Market cap | $43.65B | |
| Spot volume 24h | $2.11B | |
| DeFi TVL | $4.68B | +2.15% 1d / -0.66% 7d / -17.80% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $12.36B | |
| Stablecoin supply (all pegs) | $12.45B | |
| DEX volume 24h | $1.23B | -18.51% 1d |
| DEX volume 7d / 30d | $9.41B / $46.47B | |
| Fees + app revenue 24h | $6.15M | -13.76% 1d |
| Circulating supply | 592,238,309 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $190.65M | 15.48% |
| Orca DEX | $132.93M | 10.80% |
| Meteora DLMM | $119.43M | 9.70% |
| Scorch | $104.62M | 8.50% |
| pump.fun | $102.41M | 8.32% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-11-26 |
| - | [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) _(draft)_ | 2026-11-26 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-26 |
| - | [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) | 2026-11-25 |
| SIMD-674 | [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) | 2026-11-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-11-25 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-24 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-24 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | Release v4.5.0-rc.0 | 2026-11-25 |
| [`v5.0.0-alpha.1`](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | Release v5.0.0-alpha.1 | 2026-11-19 |
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-27T09:38:49Z | Change |
|---|---|---|---|
| SOL price | $107 | $74 | -31.40% |
| DeFi TVL | $5.94B | $4.68B | -21.28% |
| Stablecoin supply | $15.97B | $12.36B | -22.61% |
| DEX volume 24h | $3.63B | $1.23B | -66.10% |
| Mean TPS | 3,288 | 1,102 | -66.49% |
| Active validators | 689 | 654 | -5.08% |
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
