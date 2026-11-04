# Solana Ecosystem Report

_Generated 2026-11-04T20:24:21Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-04T20:24:21Z` |
| Sources healthy | 8 of 8 |
| Collection time | 7.44s |
| Snapshots in history | 578 |
| Anomalies flagged | 2 (1 critical) |

## At a glance

- The network is processing **2,394 non-vote TPS** (2,394 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **662 active validators** (31 delinquent, holding 0.457% of stake). It takes **17 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $94.8** (+1.74% over 24h), market cap $55.97B.
- **DeFi TVL $5.52B** (-3.04% 7d, -16.03% 30d), against $14.54B of stablecoins settled on Solana.
- **$1.88B of DEX volume in 24h** across 141 protocols, generating $11.47M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.457 | 0.035% +/- 0.040% (median of last 577) | Delinquent stake is 0.457%, 10.5 robust standard deviations above its recent median of 0.035% (+1205.7%). |
| 🟠 warning | Delinquent validators | 31 | 12 +/- 4.448 (median of last 577) | Delinquent validators is 31, 4.3 robust standard deviations above its recent median of 12 (+158.3%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1077 (39.53% complete) |
| Slot | 170,767 of 432,000 in epoch |
| Absolute slot | 465,434,767 |
| Block height | 443,455,163 |
| Lifetime transactions | 565,239,749,319 |
| TPS (now / mean / peak) | 1,864 / 2,394 / 3,293 |
| True TPS, non-vote (now / mean) | 1,864 / 2,394 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1077 has **261,233 slots remaining**, about **15h 36m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 31 (4.47% delinquent) |
| Total stake | 433,017,789 SOL |
| Delinquent stake | 1,977,809 SOL (0.457%) |
| Nakamoto coefficient | 17 |
| Top 1 / top 10 stake share | 3.93% / 24.75% |
| Commission (mean / median) | 12.55% / 5.0% |
| Zero-commission validators | 225 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,036,631 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,689 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,012,272 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,433,406 | 2.409% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,524,736 | 2.200% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,439,186 | 2.180% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,217,930 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,826,697 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,981,457 | 1.612% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,980,105 | 1.612% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `EXhYxF25PJEHb3v5G1HY8Jn8Jm7bRjJtaxEghGrUuhQw` | 1,265,362 | 462,239,999 |
| `Dkj8XzgvjDuZzvAwiWYExt3rwLPqtVEQTpgK49tRirb5` | 300,002 | 465,263,999 |
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 237,143 | 462,239,999 |
| `so1arJJbp9sis5XpovLyjTZPk8bDjfs37Meghi5wXbu` | 76,346 | 465,263,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `D4Em5FzPmCNTyawCYfk3zLeDTmefk7ZPfdhyJfdjLdcZ` | 17,541 | 463,967,999 |
| `2czzKTUoAtscCfEQN6LAjUX9GwzqqGqyemttYcYgYWkr` | 13,445 | 0 |
| `J21SMPFJEY9ExCDPiSJQXN23PVSeoQe3LnKD7QcP3bgP` | 2,605 | 462,239,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,596 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,850 | 464,160,502 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $94.8 | +1.74% 24h ↑ |
| Market cap | $55.97B | |
| Spot volume 24h | $3.77B | |
| DeFi TVL | $5.52B | +2.23% 1d / -3.04% 7d / -16.03% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $14.54B | |
| Stablecoin supply (all pegs) | $14.63B | |
| DEX volume 24h | $1.88B | +1.54% 1d |
| DEX volume 7d / 30d | $11.74B / $57.10B | |
| Fees + app revenue 24h | $11.47M | +2.29% 1d |
| Circulating supply | 590,262,234 SOL (92.66% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $321.84M | 17.11% |
| Orca DEX | $309.68M | 16.46% |
| BisonFi | $257.10M | 13.67% |
| Raydium AMM | $225.67M | 12.00% |
| Tessera V | $154.41M | 8.21% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-714 | [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) | 2026-11-04 |
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-04 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-04 |
| SIMD-401 | [SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) | 2026-11-04 |
| SIMD-706 | [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) | 2026-11-04 |
| SIMD-701 | [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) | 2026-11-03 |
| - | [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) | 2026-11-03 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-03 |

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

| Metric | 2026-08-28T06:17:33Z | 2026-11-04T20:24:21Z | Change |
|---|---|---|---|
| SOL price | $107 | $95 | -11.76% |
| DeFi TVL | $5.94B | $5.52B | -7.14% |
| Stablecoin supply | $15.97B | $14.54B | -8.96% |
| DEX volume 24h | $3.63B | $1.88B | -48.21% |
| Mean TPS | 3,288 | 2,394 | -27.18% |
| Active validators | 689 | 662 | -3.92% |
| Nakamoto coefficient | 18 | 17 | -5.56% |

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
