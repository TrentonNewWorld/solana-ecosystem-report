# Solana Ecosystem Report

_Generated 2026-09-22T22:25:36Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-22T22:25:36Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.01s |
| Snapshots in history | 252 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **1,969 non-vote TPS** (4,498 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.266s**.
- **677 active validators** (12 delinquent, holding 0.045% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $118.12** (-1.13% over 24h), market cap $69.38B.
- **DeFi TVL $6.49B** (+9.73% 7d, +16.60% 30d), against $15.96B of stablecoins settled on Solana.
- **$3.43B of DEX volume in 24h** across 125 protocols, generating $18.64M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6494694566 | $5,898,936,760 +/- $78,143,103 (median of last 251) | DeFi TVL is $6,494,694,566, 7.6 robust standard deviations above its recent median of $5,898,936,760 (+10.1%). |
| 🟠 warning | SOL price | 118.12 | $103 +/- $4 (median of last 251) | SOL price is $118, 4.1 robust standard deviations above its recent median of $103 (+14.2%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1040 (53.86% complete) |
| Slot | 232,688 of 432,000 in epoch |
| Absolute slot | 449,512,688 |
| Block height | 427,553,011 |
| Lifetime transactions | 551,485,825,409 |
| TPS (now / mean / peak) | 4,264 / 4,498 / 4,902 |
| True TPS, non-vote (now / mean) | 1,738 / 1,969 |
| Slot time (mean / worst) | 0.266s / 0.274s |

Epoch 1040 has **199,312 slots remaining**, about **14h 43m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 12 (1.74% delinquent) |
| Total stake | 439,861,749 SOL |
| Delinquent stake | 199,751 SOL (0.045%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.05% / 24.32% |
| Commission (mean / median) | 12.57% / 5% |
| Zero-commission validators | 236 |

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
| SOL price | $118.12 | -1.13% 24h ↓ |
| Market cap | $69.38B | |
| Spot volume 24h | $4.66B | |
| DeFi TVL | $6.49B | +4.66% 1d / +9.73% 7d / +16.60% 30d |
| TVL 90-day peak | $6.49B | |
| Stablecoin supply (USD peg) | $15.96B | |
| Stablecoin supply (all pegs) | $16.02B | |
| DEX volume 24h | $3.43B | +22.67% 1d |
| DEX volume 7d / 30d | $20.73B / $79.76B | |
| Fees + app revenue 24h | $18.64M | +26.21% 1d |
| Circulating supply | 587,507,337 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $493.51M | 14.39% |
| BisonFi | $446.78M | 13.03% |
| PumpSwap | $390.12M | 11.38% |
| Orca DEX | $377.05M | 11.00% |
| Meteora DLMM | $259.61M | 7.57% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-558 | [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) | 2026-09-22 |
| - | [Fix broken markdown, stale references and typos across several SIMDs](https://github.com/solana-foundation/solana-improvement-documents/pull/668) | 2026-09-22 |
| SIMD-385 | [SIMD-0385 / 0388 / 0204: fix inconsistent field and constant names](https://github.com/solana-foundation/solana-improvement-documents/pull/666) | 2026-09-22 |
| SIMD-118 | [Fix dead links in SIMD-0118, 0153, 0183, 0204, 0266, 0553](https://github.com/solana-foundation/solana-improvement-documents/pull/665) | 2026-09-22 |
| - | [ci: move checkout/setup-node off the deprecated Node 20 runtime, lint on Node 24](https://github.com/solana-foundation/solana-improvement-documents/pull/664) | 2026-09-22 |
| - | [Linter: match type exactly; template: add status; README: document Advisory](https://github.com/solana-foundation/solana-improvement-documents/pull/663) | 2026-09-22 |
| - | [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) | 2026-09-22 |
| - | [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) | 2026-09-22 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-22T22:25:36Z | Change |
|---|---|---|---|
| SOL price | $107 | $118 | +9.94% |
| DeFi TVL | $5.94B | $6.49B | +9.25% |
| Stablecoin supply | $15.97B | $15.96B | -0.07% |
| DEX volume 24h | $3.63B | $3.43B | -5.59% |
| Mean TPS | 3,288 | 4,498 | +36.82% |
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
