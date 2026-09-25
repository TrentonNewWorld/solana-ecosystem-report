# Solana Ecosystem Report

_Generated 2026-09-25T01:56:55Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-25T01:56:55Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.63s |
| Snapshots in history | 271 |
| Anomalies flagged | 3 (1 critical) |

## At a glance

- The network is processing **1,845 non-vote TPS** (4,356 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.267s**.
- **675 active validators** (10 delinquent, holding 0.025% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $117.35** (+2.27% over 24h), market cap $68.95B.
- **DeFi TVL $6.49B** (+9.98% 7d, +15.42% 30d), against $17.33B of stablecoins settled on Solana.
- **$2.26B of DEX volume in 24h** across 125 protocols, generating $15.93M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6485662700 | $5,907,279,238 +/- $94,953,286 (median of last 270) | DeFi TVL is $6,485,662,700, 6.1 robust standard deviations above its recent median of $5,907,279,238 (+9.8%). |
| 🟠 warning | SOL price | 117.35 | $104 +/- $4 (median of last 270) | SOL price is $117, 3.3 robust standard deviations above its recent median of $104 (+13.2%). |
| 🟠 warning | Stablecoin supply | 17333627784.88 | $15,975,438,003 +/- $340,957,884 (median of last 270) | Stablecoin supply is $17,333,627,785, 4.0 robust standard deviations above its recent median of $15,975,438,003 (+8.5%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1042 (15.42% complete) |
| Slot | 66,629 of 432,000 in epoch |
| Absolute slot | 450,210,629 |
| Block height | 428,250,618 |
| Lifetime transactions | 552,314,601,666 |
| TPS (now / mean / peak) | 4,309 / 4,356 / 4,916 |
| True TPS, non-vote (now / mean) | 1,731 / 1,845 |
| Slot time (mean / worst) | 0.267s / 0.275s |

Epoch 1042 has **365,371 slots remaining**, about **27h 5m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 10 (1.46% delinquent) |
| Total stake | 440,637,196 SOL |
| Delinquent stake | 108,367 SOL (0.025%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.40% |
| Commission (mean / median) | 12.58% / 5% |
| Zero-commission validators | 235 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,819,007 | 4.044% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,817,079 | 3.590% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,387,904 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,274,982 | 2.559% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,595,499 | 2.405% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,221,893 | 2.093% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,163,088 | 2.080% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,599,959 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,091,911 | 1.609% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,887 | 1.488% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `ViKLknQuks11DLEjZ7Y2aNYAAT7Q3NTKLGxs8rdnLVi` | 84,758 | 450,166,954 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,015,156 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 45 | 450,114,566 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 449,904,508 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $117.35 | +2.27% 24h ↑ |
| Market cap | $68.95B | |
| Spot volume 24h | $4.39B | |
| DeFi TVL | $6.49B | +0.34% 1d / +9.98% 7d / +15.42% 30d |
| TVL 90-day peak | $6.53B | |
| Stablecoin supply (USD peg) | $17.33B | |
| Stablecoin supply (all pegs) | $17.39B | |
| DEX volume 24h | $2.26B | -11.37% 1d |
| DEX volume 7d / 30d | $19.63B / $77.74B | |
| Fees + app revenue 24h | $15.93M | -1.06% 1d |
| Circulating supply | 587,648,044 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Raydium AMM | $336.10M | 14.85% |
| BisonFi | $323.94M | 14.32% |
| Orca DEX | $315.11M | 13.93% |
| Meteora DLMM | $191.04M | 8.44% |
| PumpSwap | $133.76M | 5.91% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-24 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-24 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-23 |
| SIMD-174 | [SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) | 2026-09-23 |
| - | [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) | 2026-09-23 |
| SIMD-138 | [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) | 2026-09-23 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-249 | [SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) | 2026-09-23 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-25T01:56:55Z | Change |
|---|---|---|---|
| SOL price | $107 | $117 | +9.22% |
| DeFi TVL | $5.94B | $6.49B | +9.10% |
| Stablecoin supply | $15.97B | $17.33B | +8.51% |
| DEX volume 24h | $3.63B | $2.26B | -37.70% |
| Mean TPS | 3,288 | 4,356 | +32.51% |
| Active validators | 689 | 675 | -2.03% |
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
