# Solana Ecosystem Report

_Generated 2026-11-12T01:41:11Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-11-12T01:41:11Z` |
| Sources healthy | 8 of 8 |
| Collection time | 12.35s |
| Snapshots in history | 624 |
| Anomalies flagged | 4 (0 critical) |

## At a glance

- The network is processing **2,138 non-vote TPS** (2,138 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.215s**.
- **661 active validators** (37 delinquent, holding 0.158% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $83.16** (-0.60% over 24h), market cap $49.17B.
- **DeFi TVL $5.05B** (-8.71% 7d, -15.30% 30d), against $13.88B of stablecoins settled on Solana.
- **$1.63B of DEX volume in 24h** across 141 protocols, generating $8.66M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🟠 warning | Delinquent validators | 37 | 13 +/- 5.93 (median of last 623) | Delinquent validators is 37, 4.0 robust standard deviations above its recent median of 13 (+184.6%). |
| 🟠 warning | SOL price | 83.16 | $104 +/- $6 (median of last 617) | SOL price is $83, 3.5 robust standard deviations below its recent median of $104 (-20.0%). |
| 🟠 warning | DeFi TVL | 5052016324 | $5,909,991,082 +/- $284,017,056 (median of last 622) | DeFi TVL is $5,052,016,324, 3.0 robust standard deviations below its recent median of $5,909,991,082 (-14.5%). |
| 🟠 warning | Stablecoin supply | 13878234964.07 | $15,899,431,760 +/- $524,220,614 (median of last 623) | Stablecoin supply is $13,878,234,964, 3.9 robust standard deviations below its recent median of $15,899,431,760 (-12.7%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.4.0 |
| Current epoch | 1084 (13.09% complete) |
| Slot | 56,560 of 432,000 in epoch |
| Absolute slot | 468,344,560 |
| Block height | 446,360,524 |
| Lifetime transactions | 566,284,114,197 |
| TPS (now / mean / peak) | 2,290 / 2,138 / 2,974 |
| True TPS, non-vote (now / mean) | 2,290 / 2,138 |
| Slot time (mean / worst) | 0.215s / 0.221s |

Epoch 1084 has **375,440 slots remaining**, about **22h 25m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 37 (5.30% delinquent) |
| Total stake | 433,416,361 SOL |
| Delinquent stake | 684,871 SOL (0.158%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.87% / 24.48% |
| Commission (mean / median) | 12.73% / 5% |
| Zero-commission validators | 223 |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,789,054 | 3.874% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,119,194 | 3.719% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,026,247 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,116,092 | 2.334% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,681,376 | 2.234% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,180 | 2.210% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,230,504 | 2.130% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,840,792 | 1.809% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,981 | 1.612% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,420 | 1.553% | 5% |

### Delinquent validators (top by stake)

| Vote account | Stake (SOL) | Last vote slot |
|---|---|---|
| `FQwewNXahV7MiZcLpY6p1xhUs2acVGQ3U5Xxc7FzV571` | 217,196 | 462,239,999 |
| `BULKEEKf9Hjy4nwCthjzheEk4joH23LLXttAHjqEZmB2` | 129,219 | 466,294,271 |
| `TKMA1fBGq4M7gF2CNnhphX6vNateFc2cm2FL2mYwq7e` | 88,437 | 467,356,299 |
| `P1TCHYwYPsNaNUK6fGkZzwXPjnYAMYRnUUv4c1TREee` | 79,757 | 467,356,334 |
| `sfo5vA1fFdPRsvqd8qdePtTnK97Qj6Jj3GupEzmNPjJ` | 78,884 | 467,855,999 |
| `NDf9Pv6TAxTDPR6ud3djsd2Ux1WS2m2YfTw4qEmSnQH` | 60,112 | 462,239,999 |
| `A11pGbZDE8fPNZgiqDjoST6v3QMdhzZ3r8W5YahCKtS5` | 25,235 | 468,287,999 |
| `DQ7D6ZRtKbBSxCcAunEkoTzQhCBKLPdzTjPRRnM6wo1f` | 2,592 | 461,807,999 |
| `CTDGxxJBrZVqUUHdHopLn4k4gtc2PCpcM9TB7ZEC4Hu2` | 1,836 | 464,160,502 |
| `J4pH3yiFrzFG1AQPRGBJXo3HP72MCZwsQamtp9ym4LwN` | 700 | 465,263,999 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $83.16 | -0.60% 24h ↓ |
| Market cap | $49.17B | |
| Spot volume 24h | $2.11B | |
| DeFi TVL | $5.05B | +0.02% 1d / -8.71% 7d / -15.30% 30d |
| TVL 90-day peak | $6.59B | |
| Stablecoin supply (USD peg) | $13.88B | |
| Stablecoin supply (all pegs) | $13.96B | |
| DEX volume 24h | $1.63B | +22.03% 1d |
| DEX volume 7d / 30d | $9.40B / $53.15B | |
| Fees + app revenue 24h | $8.66M | +3.10% 1d |
| Circulating supply | 591,457,094 SOL (92.79% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| PumpSwap | $395.67M | 24.21% |
| Orca DEX | $205.10M | 12.55% |
| BisonFi | $152.62M | 9.34% |
| Raydium AMM | $149.30M | 9.14% |
| Meteora DLMM | $129.37M | 7.92% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-676 | [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) | 2026-11-10 |
| SIMD-326 | [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) | 2026-11-10 |
| - | [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) | 2026-11-09 |
| SIMD-571 | [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) | 2026-11-09 |
| - | [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) | 2026-11-07 |
| SIMD-723 | [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) | 2026-11-06 |
| SIMD-709 | [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) | 2026-11-09 |
| - | [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) | 2026-11-06 |

### Recent Agave validator releases

| Tag | Release | Published |
|---|---|---|
| [`v4.5.0-beta.0`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | Release v4.5.0-beta.0 | 2026-11-06 |
| [`v4.4.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | Release v4.4.1 | 2026-11-05 |
| [`v4.4.0`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | Release v4.4.0 | 2026-10-28 |
| [`v4.5.0-alpha.4`](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | Release v4.5.0-alpha.4 | 2026-10-26 |
| [`v4.4.0-rc.1`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | Release v4.4.0-rc.1 | 2026-10-26 |
| [`v4.3.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | Release v4.3.2 | 2026-10-15 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-11-12T01:41:11Z | Change |
|---|---|---|---|
| SOL price | $107 | $83 | -22.60% |
| DeFi TVL | $5.94B | $5.05B | -15.02% |
| Stablecoin supply | $15.97B | $13.88B | -13.12% |
| DEX volume 24h | $3.63B | $1.63B | -55.01% |
| Mean TPS | 3,288 | 2,138 | -34.98% |
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
