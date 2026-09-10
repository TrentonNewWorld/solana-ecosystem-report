# Solana Ecosystem Report

_Generated 2026-09-10T15:11:56Z from live public sources. No API keys, no third-party packages._

| | |
|---|---|
| Snapshot | `2026-09-10T15:11:56Z` |
| Sources healthy | 8 of 8 |
| Collection time | 12.31s |
| Snapshots in history | 141 |
| Anomalies flagged | 1 (1 critical) |

## At a glance

- The network is processing **2,215 non-vote TPS** (4,335 TPS including consensus votes) over the last 60.0 minutes, at a mean slot time of **0.317s**.
- **675 active validators** (14 delinquent, holding 0.104% of stake). It takes **18 validators** to control a third of stake — the liveness-halting threshold.
- **SOL at $100.06** (-2.78% over 24h), market cap $58.67B.
- **DeFi TVL $5.77B** (+1.06% 7d, +19.02% 30d), against $16.16B of stablecoins settled on Solana.
- **$3.00B of DEX volume in 24h** across 122 protocols, generating $15.44M in fees.

## Anomalies

| Severity | Metric | Observed | Expected | What it means |
|---|---|---|---|---|
| 🔴 critical | Delinquent stake | 0.104 | 0.018% +/- 0.016% (median of last 140) | Delinquent stake is 0.104%, 5.3 robust standard deviations above its recent median of 0.018% (+477.8%). |

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| Validator client version | 4.2.2 |
| Current epoch | 1032 (21.07% complete) |
| Slot | 91,014 of 432,000 in epoch |
| Absolute slot | 445,915,014 |
| Block height | 423,958,369 |
| Lifetime transactions | 547,077,399,891 |
| TPS (now / mean / peak) | 4,155 / 4,335 / 5,198 |
| True TPS, non-vote (now / mean) | 2,016 / 2,215 |
| Slot time (mean / worst) | 0.317s / 0.328s |

Epoch 1032 has **340,986 slots remaining**, about **30h 1m** at the current slot time.

## Validator set

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 14 (2.03% delinquent) |
| Total stake | 439,188,213 SOL |
| Delinquent stake | 455,545 SOL (0.104%) |
| Nakamoto coefficient | 18 |
| Top 1 / top 10 stake share | 3.97% / 24.21% |
| Commission (mean / median) | 12.53% / 5% |
| Zero-commission validators | 242 |

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
| `Mxv1Ubm71XoUvxrN3qjN8ii6Bh5b43NuuKywsWx6ox2` | 220,403 | 445,914,690 |
| `3jkJVgfz1zrHSy6YLK6g96eTj49kCnDj2i8AbbKLZhkk` | 128,972 | 445,913,824 |
| `BjREhubbyR597w8tK9NUCLY74Zct2VuhvrNhyLinVc2e` | 58,591 | 445,879,082 |
| `mrgn4t2JabSgvGnrCaHXMvz8ocr4F52scsxJnkQMQsQ` | 19,888 | 445,708,539 |
| `AfyTzhTXBRBCxGdTEMc9LNEkVGVGfGA9wHf1VikaNb37` | 10,813 | 445,854,157 |
| `inQRWLtWjrZYz4z9xiPH9G8oMaGqKdeSeh7DUkGPVDL` | 8,462 | 445,699,097 |
| `xLabsqDpN9WHXEXSJXk1yhqh5H8BgcqiBP1CR6Mkjcb` | 3,361 | 443,788,373 |
| `8B2Z2R8dRvqFcXuLBwinu3Jq7HQidCaJCnDuRRqeJLC1` | 3,209 | 443,965,922 |
| `BU5CXmHhXwZfSYwFjCjqAqdbu7MTUsiKLUj45RSXiPsE` | 1,512 | 445,795,162 |
| `4GEEKSwzc242QKF1uzzodpFaxb4GShQEZhkZfeXd27Vi` | 326 | 445,809,612 |

## Economics

| Metric | Value | Change |
|---|---|---|
| SOL price | $100.06 | -2.78% 24h ↓ |
| Market cap | $58.67B | |
| Spot volume 24h | $3.55B | |
| DeFi TVL | $5.77B | -3.03% 1d / +1.06% 7d / +19.02% 30d |
| TVL 90-day peak | $6.02B | |
| Stablecoin supply (USD peg) | $16.16B | |
| Stablecoin supply (all pegs) | $16.23B | |
| DEX volume 24h | $3.00B | +10.69% 1d |
| DEX volume 7d / 30d | $17.54B / $71.20B | |
| Fees + app revenue 24h | $15.44M | -7.59% 1d |
| Circulating supply | 586,335,537 SOL (92.51% of total) |

### DEX volume by protocol (24h)

| Protocol | Volume 24h | Share of chain |
|---|---|---|
| BisonFi | $402.77M | 13.42% |
| Raydium AMM | $348.41M | 11.61% |
| PumpSwap | $340.96M | 11.36% |
| Meteora DLMM | $322.25M | 10.74% |
| HumidiFi | $285.64M | 9.52% |

## Protocol roadmap

Read from the source of record rather than a hand-kept list, so it stays correct without anyone maintaining it: open pull requests against the Solana Improvement Documents repo are what the protocol is being *asked* to change, and Agave releases are what validators are actually being asked to *run*.

### Open SIMDs (most recently updated)

| SIMD | Proposal | Updated |
|---|---|---|
| SIMD-558 | [SIMD-0558 Amendment: Specify use of sol_get_sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/634) | 2026-09-10 |
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
| [`v4.3.0-rc.0`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | Release v4.3.0-rc.0 | 2026-09-04 |
| [`v4.4.0-alpha.3`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | Release v4.4.0-alpha.3 | 2026-09-03 |
| [`v4.4.0-alpha.2`](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | Release v4.4.0-alpha.2 | 2026-08-28 |
| [`v4.3.0-beta.3`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | Release v4.3.0-beta.3 | 2026-08-28 |
| [`v4.2.2`](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | Release v4.2.2 | 2026-08-28 |
| [`v4.3.0-beta.2`](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | Release v4.3.0-beta.2 | 2026-08-21 |

## Trend since first snapshot

| Metric | 2026-08-28T06:17:33Z | 2026-09-10T15:11:56Z | Change |
|---|---|---|---|
| SOL price | $107 | $100 | -6.87% |
| DeFi TVL | $5.94B | $5.77B | -2.94% |
| Stablecoin supply | $15.97B | $16.16B | +1.19% |
| DEX volume 24h | $3.63B | $3.00B | -17.39% |
| Mean TPS | 3,288 | 4,335 | +31.85% |
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
