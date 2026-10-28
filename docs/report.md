# Solana Ecosystem Report

_Generated 2026-10-28T21:38:09Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-10-28T21:38:09Z` |
| Sources healthy | 8 of 8 |
| Collection time | 9.21s |
| Snapshots in history | 530 |
| Anomalies flagged | 2 (2 critical) |

## At a glance

- The network is processing **2,328 non-vote TPS** (2,328 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.214s**.
- **661 active validators** (30 delinquent, holding 0.886% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $102.21** (+0.63% over 24h), market cap $60.28B.
- **DeFi TVL $5.72B** (-3.83% 7d, -13.14% 30d), against $15.46B of stablecoins settled on Solana.
- **$1.58B of DEX volume in 24h** across 139 protocols, generating $10.91M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.886 | 0.028% +/- 0.031% (median of last 529) | Delinquent stake is 0.886%, 27.6 robust standard deviations above its recent median of 0.028% (+3064.3%). |
| 🔴 critical | Delinquent validators | 30 | 12 +/- 2.965 (median of last 529) | Delinquent validators is 30, 6.1 robust standard deviations above its recent median of 12 (+150.0%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.3.2 |
| Current epoch | 1070 (90.52% complete) |
| Slot | 391,031 of 432,000 in epoch |
| Absolute slot | 462,631,031 |
| Block height | 440,655,434 |
| Lifetime transactions | 564,207,234,657 |
| TPS (now / mean / peak) | 2,088 / 2,328 / 3,599 |
| True TPS, non-vote (now / mean) | 2,088 / 2,328 |
| Slot time (mean / worst) | 0.214s / 0.219s |

Epoch 1070 has **40,969 slots remaining**, about **2h 26m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 30 (4.34% delinquent) |
| Total stake | 437,290,026 SOL |
| Delinquent stake | 3,874,357 SOL (0.886%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.89% / 24.57% |
| Commission (mean / median) | 12.97% / 5% |
| Zero-commission validators | 227 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,006,422 | 3.889% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,661,096 | 3.810% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,791,931 | 2.925% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,815,143 | 2.473% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,548 | 2.222% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,464,443 | 2.164% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,208,877 | 2.106% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,757,994 | 1.774% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,041,146 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,044 | 1.600% | 0% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,559,012 | 462,239,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 1,188,775 | 462,239,999 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 794,312 | 462,239,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 292,980 | 462,239,999 |
| `sShosKd6uA5c1ZpVMxdsE6do13TLRWSMYsXbSMmNC77` | 35,704 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,613 | 461,807,999 |
| `4KfAqBj3Jvi9GGngFK1MbZkjHTcSFyvhFnVwc2QrNiEh` | 398 | 460,079,999 |
| `9pKpg51D8DNrrDYzNCpsdEtWVyzRAmV4W7Zqkkw2HfU8` | 290 | 0 |
| `SANDhe6azby4EMLJd8N77QTk5K92n2tCi4NXba7iwuc` | 181 | 460,079,999 |
| `ADoJoWDcMS7HVW8cMu5GRvy3FBm3RG5bEWQi74YRnwKt` | 63 | 462,464,506 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $102.21 | +0.63% 24h ↑ |
| Market cap | $60.28B | |
| Spot volume 24h | $2.67B | |
| DeFi TVL | $5.72B | +1.28% 1d / -3.83% 7d / -13.14% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $15.46B | |
| Stablecoin supply (all pegs) | $15.53B | |
| DEX volume 24h | $1.58B | -23.57% 1d |
| DEX volume 7d / 30d | $12.83B / $61.74B | |
| Fees + app revenue 24h | $10.91M | -6.54% 1d |
| Circulating supply | 589,928,208 SOL (92.67% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| Orca DEX | $209.43M | 13.23% |
| PumpSwap | $193.28M | 12.21% |
| BisonFi | $191.20M | 12.08% |
| Manifest Trade | $181.87M | 11.49% |
| Tessera V | $142.35M | 8.99% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-10-28 |
| SIMD-550 | [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) | 2026-10-28 |
| SIMD-706 | [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-10-28 |
| SIMD-579 | [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) | 2026-10-27 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-10-27 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-10-27 |
| SIMD-650 | [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) | 2026-10-27 |
| SIMD-567 | [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) | 2026-10-27 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-10-28T21:38:09Z | Change |
|---|---|---|---|
| SOL price | $107 | $102 | -4.87% |
| DeFi TVL | $5.94B | $5.72B | -3.75% |
| Stablecoin supply | $15.97B | $15.46B | -3.19% |
| DEX volume 24h | $3.63B | $1.58B | -56.42% |
| Mean TPS | 3,288 | 2,328 | -29.20% |
| Active validators | 689 | 661 | -4.06% |
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
