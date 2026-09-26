# Solana Ecosystem Report

_Generated 2026-09-26T06:08:16Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-26T06:08:16Z` |
| Sources healthy | 8 of 8 |
| Collection time | 6.59s |
| Snapshots in history | 280 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,179 non-vote TPS** (4,683 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.269s**.
- **675 active validators** (12 delinquent, holding 0.008% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $120.43** (+3.49% over 24h), market cap $70.78B.
- **DeFi TVL $6.61B** (+4.86% 7d, +14.27% 30d), against $16.66B of stablecoins settled on Solana.
- **$2.80B of DEX volume in 24h** across 125 protocols, generating $14.94M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | DeFi TVL | 6612074872 | $5,910,417,113 +/- $99,855,597 (median of last 279) | DeFi TVL is $6,612,074,872, 7.0 robust standard deviations above its recent median of $5,910,417,113 (+11.9%). |
| 🟠 warning | SOL price | 120.43 | $104 +/- $4 (median of last 279) | SOL price is $120, 3.7 robust standard deviations above its recent median of $104 (+16.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0 |
| Current epoch | 1043 (3.08% complete) |
| Slot | 13,327 of 432,000 in epoch |
| Absolute slot | 450,589,327 |
| Block height | 428,629,118 |
| Lifetime transactions | 552,775,134,634 |
| TPS (now / mean / peak) | 4,666 / 4,683 / 5,270 |
| True TPS, non-vote (now / mean) | 2,200 / 2,179 |
| Slot time (mean / worst) | 0.269s / 0.279s |

Epoch 1043 has **418,673 slots remaining**, about **31h 17m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 12 (1.75% delinquent) |
| Total stake | 437,542,654 SOL |
| Delinquent stake | 36,336 SOL (0.008%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 4.08% / 24.61% |
| Commission (mean / median) | 12.61% / 5% |
| Zero-commission validators | 232 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,860,284 | 4.082% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,799,204 | 3.611% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,343,056 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,222,561 | 2.565% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,836,562 | 2.477% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,102 | 2.111% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,182,742 | 2.099% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,606,181 | 1.738% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,093,311 | 1.621% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,506,505 | 1.487% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `8jxSHbS4qAnh5yueFp4D9ABXubKqMwXqF3HtdzQGuphp` | 12,737 | 450,345,071 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,703 | 450,466,404 |
| `H3GhqPMwvGLdxWg3QJGjXDSkFSJCsFk3Wx9XBTdYZykc` | 9,758 | 448,798,710 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 2,207 | 448,597,405 |
| `DHoZJqvvMGvAXw85Lmsob7YwQzFVisYg8HY4rt5BAj6M` | 790 | 448,492,871 |
| `6ANziPu9boXJ6PZzSQoBVEUz8qowKMK3XWaxmG4EYVMJ` | 64 | 450,022,154 |
| `6XPxXV2VZMNqSquPUF3bjnGt5u8R884A9UVYS6jv8g5f` | 46 | 450,473,191 |
| `MajorF3gAYEmUhqkoRXoL546Zim8nMa82tuUTz9LkmE` | 24 | 448,762,375 |
| `R1vAoSPFQdCc6wsAEMtxWXjqptSeN1YUiq2Zni1of21` | 3 | 384,048,870 |
| `9HgX6hTfHSW2KcmopricBPVsS1pTGTEoFZji65D2yDUX` | 2 | 450,230,119 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $120.43 | +3.49% 24h ↑ |
| Market cap | $70.78B | |
| Spot volume 24h | $6.11B | |
| DeFi TVL | $6.61B | +1.95% 1d / +4.86% 7d / +14.27% 30d |
| TVL 90-day peak | $6.61B | |
| Stablecoin supply (USD peg) | $16.66B | |
| Stablecoin supply (all pegs) | $16.72B | |
| DEX volume 24h | $2.80B | +14.26% 1d |
| DEX volume 7d / 30d | $18.90B / $78.12B | |
| Fees + app revenue 24h | $14.94M | -6.49% 1d |
| Circulating supply | 587,713,208 SOL (92.59% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $425.99M | 15.21% |
| BisonFi | $395.08M | 14.11% |
| Orca DEX | $386.44M | 13.80% |
| Raydium AMM | $289.35M | 10.33% |
| Meteora DLMM | $204.57M | 7.31% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-670 | [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) | 2026-09-26 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-25 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-09-25 |
| SIMD-646 | [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) _(draft)_ | 2026-09-25 |
| SIMD-648 | [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) | 2026-09-23 |
| SIMD-645 | [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) | 2026-09-23 |
| SIMD-499 | [SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) | 2026-09-19 |
| SIMD-602 | [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) | 2026-09-18 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-09-26T06:08:16Z | Change |
|---|---|---|---|
| SOL price | $107 | $120 | +12.09% |
| DeFi TVL | $5.94B | $6.61B | +11.23% |
| Stablecoin supply | $15.97B | $16.66B | +4.30% |
| DEX volume 24h | $3.63B | $2.80B | -22.90% |
| Mean TPS | 3,288 | 4,683 | +42.44% |
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
