"""Markdown report generator.

The narrative is derived from the snapshot, not hand-written: every sentence
below is a function of the numbers, so the report regenerates itself correctly
on every refresh instead of drifting out of date.
"""

import datetime


def _usd(v, digits=0):
    if v is None:
        return "n/a"
    for unit, scale in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(v) >= scale:
            return "$%.2f%s" % (v / scale, unit)
    return "$%.*f" % (digits, v)


def _num(v, digits=0):
    if v is None:
        return "n/a"
    return format(round(v, digits) if digits else round(v), ",")


def _pct(v, digits=2, sign=False):
    if v is None:
        return "n/a"
    return "%+.*f%%" % (digits, v) if sign else "%.*f%%" % (digits, v)


def _arrow(v):
    if v is None:
        return ""
    return " ↑" if v > 0 else (" ↓" if v < 0 else " →")


def render(snapshot, findings, history):
    net = snapshot.get("network") or {}
    perf = net.get("performance") or {}
    epoch = net.get("epoch") or {}
    supply = net.get("supply") or {}
    val = snapshot.get("validators") or {}
    mkt = snapshot.get("market") or {}
    tvl = snapshot.get("tvl") or {}
    stables = snapshot.get("stablecoins") or {}
    dex = snapshot.get("dex") or {}
    fees = snapshot.get("fees") or {}

    L = []
    a = L.append

    a("# Solana Ecosystem Report")
    a("")
    a("_Generated %s from live public sources. No API keys, no third-party packages._"
      % snapshot["generated_at"])
    a("")
    a("| | |")
    a("|---|---|")
    a("| Snapshot | `%s` |" % snapshot["generated_at"])
    a("| Sources healthy | %s of %s |" % (snapshot.get("sources_ok"), snapshot.get("sources_total")))
    a("| Collection time | %ss |" % snapshot.get("collection_seconds"))
    a("| Snapshots in history | %d |" % len(history))
    a("| Anomalies flagged | %d (%d critical) |"
      % (len(findings), sum(1 for f in findings if f["severity"] == "critical")))
    a("")

    # ---------------- executive summary (fully derived) -------------------
    a("## At a glance")
    a("")
    bullets = []
    if perf.get("true_tps_mean") is not None:
        bullets.append(
            "The network is processing **%s non-vote TPS** (%s TPS including consensus votes) "
            "over the last %s minutes, at a mean slot time of **%.3fs**."
            % (_num(perf["true_tps_mean"]), _num(perf.get("tps_mean")),
               perf.get("window_minutes"), perf.get("slot_time_mean_s") or 0))
    if val.get("active_count") is not None:
        bullets.append(
            "**%s active validators** (%s delinquent, holding %s of stake). It takes "
            "**%s validators** to control a third of stake — the liveness-halting threshold."
            % (_num(val["active_count"]), _num(val.get("delinquent_count")),
               _pct(val.get("delinquent_stake_pct"), 3), val.get("nakamoto_coefficient")))
    if mkt.get("price_usd") is not None:
        bullets.append("**SOL at $%s** (%s over 24h), market cap %s."
                       % (_num(mkt["price_usd"], 2), _pct(mkt.get("change_24h_pct"), 2, True),
                          _usd(mkt.get("market_cap_usd"))))
    if tvl.get("tvl_usd") is not None:
        bullets.append("**DeFi TVL %s** (%s 7d, %s 30d), against %s of stablecoins settled on Solana."
                       % (_usd(tvl["tvl_usd"]), _pct(tvl.get("change_7d_pct"), 2, True),
                          _pct(tvl.get("change_30d_pct"), 2, True), _usd(stables.get("usd_pegged"))))
    if dex.get("volume_24h_usd") is not None:
        bullets.append("**%s of DEX volume in 24h** across %s protocols, generating %s in fees."
                       % (_usd(dex["volume_24h_usd"]), dex.get("protocol_count"),
                          _usd(fees.get("fees_24h_usd"))))
    for b in bullets:
        a("- " + b)
    a("")

    # ---------------- anomalies -------------------------------------------
    a("## Anomalies")
    a("")
    if not findings:
        a("No anomalies detected. Every monitored metric is inside its absolute safety band"
          + (" and within normal variance of its recent median." if len(history) >= 8
             else "; historical z-score checks activate once 8 snapshots exist (currently %d)." % len(history)))
    else:
        a("| Severity | Metric | Observed | Expected | What it means |")
        a("|---|---|---|---|---|")
        for f in findings:
            icon = {"critical": "🔴 critical", "warning": "🟠 warning"}.get(f["severity"], f["severity"])
            a("| %s | %s | %s | %s | %s |"
              % (icon, f["metric"], f["value"], f["expected"], f["message"]))
    a("")

    # ---------------- network ---------------------------------------------
    a("## Network performance")
    a("")
    a("| Metric | Value |")
    a("|---|---|")
    a("| RPC health | %s |" % (net.get("health") or "n/a"))
    a("| Validator client version | %s |" % (net.get("version") or "n/a"))
    a("| Current epoch | %s (%s complete) |" % (epoch.get("epoch"), _pct(epoch.get("progress_pct"))))
    a("| Slot | %s of %s in epoch |" % (_num(epoch.get("slot_index")), _num(epoch.get("slots_in_epoch"))))
    a("| Absolute slot | %s |" % _num(epoch.get("absolute_slot")))
    a("| Block height | %s |" % _num(epoch.get("block_height")))
    a("| Lifetime transactions | %s |" % _num(epoch.get("transaction_count")))
    a("| TPS (now / mean / peak) | %s / %s / %s |"
      % (_num(perf.get("tps_current")), _num(perf.get("tps_mean")), _num(perf.get("tps_max"))))
    a("| True TPS, non-vote (now / mean) | %s / %s |"
      % (_num(perf.get("true_tps_current")), _num(perf.get("true_tps_mean"))))
    a("| Slot time (mean / worst) | %ss / %ss |"
      % (perf.get("slot_time_mean_s"), perf.get("slot_time_max_s")))
    a("")
    if epoch.get("slots_in_epoch"):
        remaining = (epoch.get("slots_in_epoch") or 0) - (epoch.get("slot_index") or 0)
        slot_s = perf.get("slot_time_mean_s") or 0.4
        eta = datetime.timedelta(seconds=int(remaining * slot_s))
        a("Epoch %s has **%s slots remaining**, about **%s** at the current slot time."
          % (epoch.get("epoch"), _num(remaining), _fmt_delta(eta)))
        a("")

    # ---------------- validators ------------------------------------------
    a("## Validator set")
    a("")
    a("| Metric | Value |")
    a("|---|---|")
    a("| Active / delinquent | %s / %s (%s delinquent) |"
      % (_num(val.get("active_count")), _num(val.get("delinquent_count")), _pct(val.get("delinquent_pct"))))
    a("| Total stake | %s SOL |" % _num(val.get("total_stake_sol")))
    a("| Delinquent stake | %s SOL (%s) |"
      % (_num(val.get("delinquent_stake_sol")), _pct(val.get("delinquent_stake_pct"), 3)))
    a("| Nakamoto coefficient | %s |" % val.get("nakamoto_coefficient"))
    a("| Top 1 / top 10 stake share | %s / %s |"
      % (_pct(val.get("top1_stake_pct")), _pct(val.get("top10_stake_pct"))))
    a("| Commission (mean / median) | %s%% / %s%% |"
      % (val.get("commission_mean"), val.get("commission_median")))
    a("| Zero-commission validators | %s |" % _num(val.get("zero_commission_count")))
    a("")
    if val.get("top_validators"):
        a("### Top validators by stake")
        a("")
        a("| # | Vote account | Stake (SOL) | Share | Commission |")
        a("|---|---|---|---|---|")
        for i, v in enumerate(val["top_validators"], 1):
            a("| %d | `%s` | %s | %s | %s%% |"
              % (i, v["vote_pubkey"], _num(v["stake_sol"]), _pct(v["stake_pct"], 3), v["commission"]))
        a("")
    if val.get("delinquent_validators"):
        a("### Delinquent validators (top by stake)")
        a("")
        a("| Vote account | Stake (SOL) | Last vote slot |")
        a("|---|---|---|")
        for v in val["delinquent_validators"]:
            a("| `%s` | %s | %s |" % (v["vote_pubkey"], _num(v["stake_sol"]), _num(v["last_vote"])))
        a("")

    # ---------------- economics -------------------------------------------
    a("## Economics")
    a("")
    a("| Metric | Value | Change |")
    a("|---|---|---|")
    a("| SOL price | $%s | %s 24h%s |"
      % (_num(mkt.get("price_usd"), 2), _pct(mkt.get("change_24h_pct"), 2, True),
         _arrow(mkt.get("change_24h_pct"))))
    a("| Market cap | %s | |" % _usd(mkt.get("market_cap_usd")))
    a("| Spot volume 24h | %s | |" % _usd(mkt.get("volume_24h_usd")))
    a("| DeFi TVL | %s | %s 1d / %s 7d / %s 30d |"
      % (_usd(tvl.get("tvl_usd")), _pct(tvl.get("change_1d_pct"), 2, True),
         _pct(tvl.get("change_7d_pct"), 2, True), _pct(tvl.get("change_30d_pct"), 2, True)))
    a("| TVL 90-day peak | %s | |" % _usd(tvl.get("peak_90d_usd")))
    a("| Stablecoin supply (USD peg) | %s | |" % _usd(stables.get("usd_pegged")))
    a("| Stablecoin supply (all pegs) | %s | |" % _usd(stables.get("all_pegs_usd")))
    a("| DEX volume 24h | %s | %s 1d |"
      % (_usd(dex.get("volume_24h_usd")), _pct(dex.get("change_1d_pct"), 2, True)))
    a("| DEX volume 7d / 30d | %s / %s | |"
      % (_usd(dex.get("volume_7d_usd")), _usd(dex.get("volume_30d_usd"))))
    a("| Fees + app revenue 24h | %s | %s 1d |"
      % (_usd(fees.get("fees_24h_usd")), _pct(fees.get("change_1d_pct"), 2, True)))
    a("| Circulating supply | %s SOL (%s of total) |"
      % (_num(supply.get("circulating_sol")), _pct(supply.get("circulating_pct"))))
    a("")
    if dex.get("top_protocols"):
        a("### DEX volume by protocol (24h)")
        a("")
        a("| Protocol | Volume 24h | Share of chain |")
        a("|---|---|---|")
        total = dex.get("volume_24h_usd") or 0
        for p in dex["top_protocols"]:
            share = _pct(100.0 * p["volume_24h_usd"] / total) if total and p.get("volume_24h_usd") else "n/a"
            a("| %s | %s | %s |" % (p["name"], _usd(p.get("volume_24h_usd")), share))
        a("")

    # ---------------- trend ------------------------------------------------
    if len(history) >= 2:
        a("## Trend since first snapshot")
        a("")
        first, last = history[0], history[-1]
        a("| Metric | %s | %s | Change |" % (first["ts"], last["ts"]))
        a("|---|---|---|---|")
        for key, label, fmt in (("price_usd", "SOL price", _usd),
                                ("tvl_usd", "DeFi TVL", _usd),
                                ("stablecoin_usd", "Stablecoin supply", _usd),
                                ("dex_volume_24h_usd", "DEX volume 24h", _usd),
                                ("tps_mean", "Mean TPS", _num),
                                ("validators_active", "Active validators", _num),
                                ("nakamoto_coefficient", "Nakamoto coefficient", _num)):
            if first.get(key) is None or last.get(key) is None:
                continue
            delta = (100.0 * (last[key] - first[key]) / first[key]) if first[key] else None
            a("| %s | %s | %s | %s |" % (label, fmt(first[key]), fmt(last[key]),
                                         _pct(delta, 2, True)))
        a("")

    # ---------------- methodology -----------------------------------------
    a("## Data sources")
    a("")
    a("| Source | Used for | Key required |")
    a("|---|---|---|")
    a("| `%s` (Solana JSON-RPC) | epoch, slots, TPS, slot time, supply, validator set | no |"
      % snapshot["sources"]["solana_rpc"])
    a("| CoinGecko public API | SOL price, market cap, spot volume | no |")
    a("| DeFiLlama | DeFi TVL (90d series), DEX volume, chain fees | no |")
    a("| DeFiLlama stablecoins | stablecoin supply settled on Solana, by peg | no |")
    a("")
    a("Every request is a plain HTTPS GET/POST from `urllib` in the Python standard "
      "library. There are no API keys, no accounts and no third-party packages, so the "
      "pipeline runs on a bare `python:3-slim` image or a GitHub Actions runner with no setup step.")
    a("")
    a("---")
    a("")
    a("Report and dashboard regenerated automatically by "
      "[`solreport`](README.md). Snapshot history: `data/history.jsonl`.")
    return "\n".join(L) + "\n"


def _fmt_delta(td):
    hours, rem = divmod(int(td.total_seconds()), 3600)
    minutes = rem // 60
    if hours:
        return "%dh %dm" % (hours, minutes)
    return "%dm" % minutes
