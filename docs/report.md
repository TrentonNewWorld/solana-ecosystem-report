# Solana Ecosystem Report

_Generated 2026-09-25T15:55:51Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-25T15:55:51Z` |
| Sources healthy | 8 of 8 |
| Collection time | 6.8s |
| Snapshots in history | 275 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,454 non-vote TPS** (4,962 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.268s**.
- **675 active validators** (10 delinquent, holding 0.008% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $119.27** (+2.55% over 24h), market cap $70.08B.
- **DeFi TVL $6.54B** (+10.97% 7d, +16.46% 30d), against $16.57B of stablecoins settled on Solana.
- **$2.45B of DEX volume in 24h** across 125 protocols, generating $15.98M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6543754304 | $5,907,744,800 +/- $96,536,547 (median of last 274) | DeFi TVL is $6,543,754,304, 6.6 robust standard deviations above its recent median of $5,907,744,800 (+10.8%). |
| 🟠 warning | SOL price | 119.27 | $104 +/- $4 (median of last 274) | SOL price is $119, 3.6 robust standard deviations above its recent median of $104 (+15.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1042 (59.06% complete) |
| Slot | 255,121 of 432,000 in epoch |
| Absolute slot | 450,399,121 |
| Block height | 428,439,005 |
| Lifetime transactions | 552,530,343,551 |
| TPS (now / mean / peak) | 4,948 / 4,962 / 5,472 |
| True TPS, non-vote (now / mean) | 2,437 / 2,454 |
| Slot time (mean / worst) | 0.268s / 0.28s |

Epoch 1042 has **176,879 slots remaining**, about **13h 10m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 10 (1.46% delinquent) |
| Total stake | 440,637,196 SOL |
| Delinquent stake | 36,346 SOL (0.008%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.04% / 24.40% |
| Commission (mean / median) | 12.91% / 5% |
| Zero-commission validators | 230 |

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
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,736 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,287,917 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,765 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 797 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 45 | 450,114,566 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `sTach38ebT8jnGH8i2D1g8NDAS6An19whVMnSSWPXt4` | 3 | 429,535,683 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 450,230,119 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $119.27 | +2.55% 24h ↑ |
| Market cap | $70.08B | |
| Spot volume 24h | $6.06B | |
| DeFi TVL | $6.54B | +2.34% 1d / +10.97% 7d / +16.46% 30d |
| TVL 90-day peak | $6.54B | |
| Stablecoin supply (USD peg) | $16.57B | |
| Stablecoin supply (all pegs) | $16.63B | |
| DEX volume 24h | $2.45B | -4.00% 1d |
| DEX volume 7d / 30d | $20.84B / $78.94B | |
| Fees + app revenue 24h | $15.98M | -1.37% 1d |
| Circulating supply | 587,647,478 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $395.08M | 16.12% |
| Orca DEX | $344.60M | 14.06% |
| Raydium AMM | $283.37M | 11.56% |
| Meteora DLMM | $191.04M | 7.80% |
| HumidiFi | $190.33M | 7.77% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-25 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-25 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-23 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-24 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-09-19 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-18 |
| SIMD-607 | [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) _(draft)_ | 2026-09-18 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-25T15:55:51Z | Change |
|---|---|---|---|
| SOL price | $107 | $119 | +11.01% |
| DeFi TVL | $5.94B | $6.54B | +10.08% |
| Stablecoin supply | $15.97B | $16.57B | +3.74% |
| DEX volume 24h | $3.63B | $2.45B | -32.53% |
| Mean TPS | 3,288 | 4,962 | +50.92% |
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
