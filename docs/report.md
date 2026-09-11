# Solana Ecosystem Report

_Generated 2026-09-11T13:32:30Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-11T13:32:30Z` |
| Sources healthy | 8 of 8 |
| Collection time | 8.08s |
| Snapshots in history | 149 |
| Anomalies flagged | 1 (1 critical) |

## At a glance

- The network is processing **2,430 non-vote TPS** (4,531 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.319s**.
- **673 active validators** (16 delinquent, holding 0.447% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $101.29** (+2.06% over 24h), market cap $59.32B.
- **DeFi TVL $5.79B** (-2.39% 7d, +18.77% 30d), against $15.97B of stablecoins settled on Solana.
- **$2.92B of DEX volume in 24h** across 122 protocols, generating $14.61M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.447 | 0.018% +/- 0.017% (median of last 148) | Delinquent stake is 0.447%, 25.2 robust standard deviations above its recent median of 0.018% (+2383.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.0-rc.0 |
| Current epoch | 1032 (79.90% complete) |
| Slot | 345,154 of 432,000 in epoch |
| Absolute slot | 446,169,154 |
| Block height | 424,212,348 |
| Lifetime transactions | 547,389,548,809 |
| TPS (now / mean / peak) | 4,901 / 4,531 / 6,534 |
| True TPS, non-vote (now / mean) | 2,839 / 2,430 |
| Slot time (mean / worst) | 0.319s / 0.339s |

Epoch 1032 has **86,846 slots remaining**, about **7h 41m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 16 (2.32% delinquent) |
| Total stake | 439,188,213 SOL |
| Delinquent stake | 1,961,345 SOL (0.447%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.21% |
| Commission (mean / median) | 12.86% / 5% |
| Zero-commission validators | 239 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.971% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.717% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.852% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.591% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.179% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,796 | 2.113% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.057% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.672% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.567% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.491% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `34kE8AGJazhgrsovREiB2Uru1CuhN4gCznNAmVUxB9AB` | 1,644,185 | 446,093,575 |
| `EtMSc3MvcDXUr6ChK5GxyFVwTxYA3zqP5XzjE9jwKvSV` | 95,156 | 446,087,868 |
| `sT34kbaqmHWbPwjhyeG1GnjoX82KpXawFsnzUkzJpYX` | 80,694 | 446,160,567 |
| `BjREhubbyR597w8tK9NUCLY74Zct2VuhvrNhyLinVc2e` | 58,591 | 445,879,082 |
| `4BVYjw1ztUzUPsxsaCheWWwThT2X4rjogZytGnuWPUGg` | 35,140 | 446,141,354 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 19,888 | 446,139,556 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,813 | 445,854,157 |
| `inQRWLtWjrZYz4z9xiPH9G8oMaGqKdeSeh7DUkGPVDL` | 8,462 | 445,699,097 |
| `xLabsqDpN9WHXEXSJXk1yhqh5H8BgcqiBP1CR6Mkjcb` | 3,361 | 443,788,373 |
| `8B2Z2R8dRvqFcXuLBwinu3Jq7HQidCaJCnDuRRqeJLC1` | 3,209 | 443,965,922 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $101.29 | +2.06% 24h ↑ |
| Market cap | $59.32B | |
| Spot volume 24h | $3.19B | |
| DeFi TVL | $5.79B | -1.15% 1d / -2.39% 7d / +18.77% 30d |
| TVL 90-day peak | $6.03B | |
| Stablecoin supply (USD peg) | $15.97B | |
| Stablecoin supply (all pegs) | $16.04B | |
| DEX volume 24h | $2.92B | -2.61% 1d |
| DEX volume 7d / 30d | $18.00B / $72.48B | |
| Fees + app revenue 24h | $14.61M | -6.98% 1d |
| Circulating supply | 586,537,421 SOL (92.54% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $468.14M | 16.02% |
| BisonFi | $395.81M | 13.55% |
| Raydium AMM | $390.47M | 13.36% |
| HumidiFi | $322.67M | 11.04% |
| Tessera V | $232.00M | 7.94% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-558 | [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) | 2026-09-11 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-09-09 |
| SIMD-376 | [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) | 2026-09-09 |
| SIMD-582 | [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) | 2026-09-09 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-09-08 |
| SIMD-177 | [SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) | 2026-09-08 |
| SIMD-630 | [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) | 2026-09-08 |
| SIMD-464 | [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) | 2026-09-03 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.4.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | Release v4.4.0-alpha.4 | 2026-09-10 |
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |
| [`v4.4.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | Release v4.4.0-alpha.2 | 2026-08-28 |
| [`v4.3.0-beta.3`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | Release v4.3.0-beta.3 | 2026-08-28 |
| [`v4.2.2`](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | Release v4.2.2 | 2026-08-28 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-11T13:32:30Z | Change |
|---|---|---|---|
| SOL price | $107 | $101 | -5.72% |
| DeFi TVL | $5.94B | $5.79B | -2.60% |
| Stablecoin supply | $15.97B | $15.97B | -0.01% |
| DEX volume 24h | $3.63B | $2.92B | -19.55% |
| Mean TPS | 3,288 | 4,531 | +37.81% |
| Active validators | 689 | 673 | -2.32% |
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
