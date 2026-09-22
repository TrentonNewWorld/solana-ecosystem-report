# Solana Ecosystem Report

_Generated 2026-09-22T20:10:44Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-22T20:10:44Z` |
| Sources healthy | 8 of 8 |
| Collection time | 10.58s |
| Snapshots in history | 251 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,348 non-vote TPS** (4,868 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **677 active validators** (12 delinquent, holding 0.045% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $118.1** (-0.33% over 24h), market cap $69.37B.
- **DeFi TVL $6.49B** (+9.70% 7d, +16.56% 30d), against $15.98B of stablecoins settled on Solana.
- **$3.43B of DEX volume in 24h** across 125 protocols, generating $18.64M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6492724520 | $5,898,602,886 +/- $77,456,489 (median of last 250) | DeFi TVL is $6,492,724,520, 7.7 robust standard deviations above its recent median of $5,898,602,886 (+10.1%). |
| 🟠 warning | SOL price | 118.1 | $103 +/- $4 (median of last 250) | SOL price is $118, 4.0 robust standard deviations above its recent median of $103 (+14.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1040 (46.85% complete) |
| Slot | 202,404 of 432,000 in epoch |
| Absolute slot | 449,482,404 |
| Block height | 427,522,737 |
| Lifetime transactions | 551,448,771,180 |
| TPS (now / mean / peak) | 4,487 / 4,868 / 5,284 |
| True TPS, non-vote (now / mean) | 1,995 / 2,348 |
| Slot time (mean / worst) | 0.267s / 0.275s |

Epoch 1040 has **229,596 slots remaining**, about **17h 1m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 12 (1.74% delinquent) |
| Total stake | 439,861,749 SOL |
| Delinquent stake | 199,751 SOL (0.045%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.05% / 24.32% |
| Commission (mean / median) | 12.27% / 5% |
| Zero-commission validators | 239 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,826,722 | 4.053% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,698 | 3.601% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,354,353 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,265,429 | 2.561% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,210,832 | 2.321% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,211,356 | 2.094% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,144,102 | 2.079% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,458,789 | 1.696% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,089,342 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,555,722 | 1.490% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `drXsaoxWGkvjEUveMpbS1RVQmtZ7y1kb9E4YERJxCFt` | 89,154 | 0 |
| `54DYhq7YnjHgVw8fKTEtYbc7qAtctWo8bjj84BrK1199` | 71,154 | 0 |
| `6XiVWAyRpG7wGUQPVRd2XrYdgQVQyoQamd2J8XAmate` | 14,371 | 447,595,236 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,706 | 449,084,940 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,261 | 448,597,405 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 447,874,752 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $118.1 | -0.33% 24h ↓ |
| Market cap | $69.37B | |
| Spot volume 24h | $4.89B | |
| DeFi TVL | $6.49B | +4.62% 1d / +9.70% 7d / +16.56% 30d |
| TVL 90-day peak | $6.49B | |
| Stablecoin supply (USD peg) | $15.98B | |
| Stablecoin supply (all pegs) | $16.04B | |
| DEX volume 24h | $3.43B | +22.67% 1d |
| DEX volume 7d / 30d | $20.73B / $79.76B | |
| Fees + app revenue 24h | $18.64M | +26.21% 1d |
| Circulating supply | 587,507,434 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $497.57M | 14.51% |
| BisonFi | $446.78M | 13.03% |
| Orca DEX | $398.84M | 11.63% |
| PumpSwap | $390.12M | 11.38% |
| Meteora DLMM | $259.61M | 7.57% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-302 | [Fix rendering in SIMD-0302/0306/0266/0307, rename 0505 file to 0506](https://github.com/solana-foundation/solana-improvement-documents/pull/655) | 2026-09-22 |
| SIMD-47 | [SIMD-0047 / SIMD-0186: fix syscall hash and signature, union of loaded accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/654) | 2026-09-22 |
| SIMD-317 | [SIMD-0317 / SIMD-0313: fix FEC set payload size, gate name and shred layout](https://github.com/solana-foundation/solana-improvement-documents/pull/653) | 2026-09-22 |
| SIMD-174 | [SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) | 2026-09-22 |
| - | [Sync SIMD statuses and feature keys with mainnet activations (56 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) | 2026-09-22 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-22 |
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-22 |
| SIMD-558 | [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) | 2026-09-22 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-22T20:10:44Z | Change |
|---|---|---|---|
| SOL price | $107 | $118 | +9.92% |
| DeFi TVL | $5.94B | $6.49B | +9.22% |
| Stablecoin supply | $15.97B | $15.98B | +0.01% |
| DEX volume 24h | $3.63B | $3.43B | -5.59% |
| Mean TPS | 3,288 | 4,868 | +48.07% |
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
