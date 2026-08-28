"""Anomaly detection over the snapshot history.

Two complementary detectors, because they fail in different ways:

* **Absolute rules** fire on values that are bad regardless of history — a
  delinquent-stake share above 5%, slot times over 0.8s, an unhealthy RPC. These
  work on the very first run, when there is no history to compare against.
* **Robust z-scores** fire on values that are unusual *for this chain lately*.
  They use the median and the median absolute deviation rather than mean/stdev,
  so a single earlier spike does not inflate the baseline and mask the next one.

Each finding carries a severity, the observed value, the expected range, and a
plain-English sentence, so the same object renders into Markdown, JSON and HTML
without re-deriving anything.
"""

import statistics

# metric -> (label, direction, warn_z, crit_z, unit, min_rel)
#   direction: "both" | "up" (only high is bad) | "down" (only low is bad)
#   min_rel:   the move must ALSO be at least this fraction of the median before
#              it is reported at all. See MATERIALITY below.
Z_RULES = [
    ("tps_mean", "Mean TPS", "both", 3.0, 4.5, "tx/s", 0.05),
    ("true_tps_mean", "True TPS (non-vote)", "both", 3.0, 4.5, "tx/s", 0.05),
    ("slot_time_mean_s", "Mean slot time", "up", 3.0, 4.5, "s", 0.05),
    ("delinquent_stake_pct", "Delinquent stake", "up", 3.0, 4.5, "%", 0.25),
    ("validators_delinquent", "Delinquent validators", "up", 3.0, 4.5, "", 0.25),
    ("nakamoto_coefficient", "Nakamoto coefficient", "down", 3.0, 4.5, "", 0.10),
    ("price_usd", "SOL price", "both", 3.0, 4.5, "USD", 0.03),
    ("tvl_usd", "DeFi TVL", "both", 3.0, 4.5, "USD", 0.03),
    ("stablecoin_usd", "Stablecoin supply", "both", 3.0, 4.5, "USD", 0.03),
    ("dex_volume_24h_usd", "DEX volume (24h)", "both", 3.0, 4.5, "USD", 0.15),
]

MIN_HISTORY = 8  # below this, z-scores are noise; absolute rules still apply

# MATERIALITY. A robust z-score divides by the spread of the baseline, so when a
# metric has been unusually flat the divisor collapses and an ordinary 1% drift
# scores 5 sigma. Statistically that is correct and editorially it is useless: a
# dashboard that shouts "critical" at normal TPS jitter trains its reader to
# ignore it. Every z-finding therefore has to clear a second, independent gate --
# the move must be a material fraction of the median in its own right. Both gates
# must fire, so a finding is always "unusual for this chain AND big enough to
# care about".


def _robust_z(value, baseline):
    """Modified z-score (Iglewicz-Hoaglin). Returns None when the baseline has
    no spread at all, which would otherwise divide by zero."""
    med = statistics.median(baseline)
    mad = statistics.median([abs(x - med) for x in baseline])
    if mad == 0:
        spread = statistics.pstdev(baseline)
        if spread == 0:
            return None, med, 0.0
        return (value - med) / spread, med, spread
    return 0.6745 * (value - med) / mad, med, mad / 0.6745


def _fmt(value, unit):
    if unit == "USD":
        return "$%s" % format(round(value), ",")
    if unit == "%":
        return "%.3f%%" % value
    if unit:
        return "%.3g %s" % (value, unit)
    return "%.4g" % value


def absolute_checks(snapshot):
    findings = []
    net = snapshot.get("network") or {}
    perf = net.get("performance") or {}
    val = snapshot.get("validators") or {}
    tvl = snapshot.get("tvl") or {}
    mkt = snapshot.get("market") or {}

    if net.get("ok") and net.get("health") not in (None, "ok"):
        findings.append(_f("critical", "rpc_health", "RPC health",
                           net.get("health"), "ok",
                           "The RPC endpoint reports itself unhealthy (%s); every on-chain "
                           "metric in this report may be stale." % net.get("health")))

    slot = perf.get("slot_time_mean_s")
    if slot is not None:
        if slot > 0.8:
            findings.append(_f("critical", "slot_time", "Mean slot time", slot, "<= 0.65 s",
                               "Slot time is %.3fs against a ~0.4s target — the network is "
                               "producing blocks materially slower than normal." % slot))
        elif slot > 0.65:
            findings.append(_f("warning", "slot_time", "Mean slot time", slot, "<= 0.65 s",
                               "Slot time is %.3fs, above the ~0.4s target." % slot))

    dpct = val.get("delinquent_stake_pct")
    if dpct is not None:
        if dpct > 5.0:
            findings.append(_f("critical", "delinquent_stake", "Delinquent stake", dpct, "< 2%",
                               "%.2f%% of stake is delinquent. Above ~33%% the chain stops "
                               "finalizing, so this is the metric to watch." % dpct))
        elif dpct > 2.0:
            findings.append(_f("warning", "delinquent_stake", "Delinquent stake", dpct, "< 2%",
                               "%.2f%% of stake is delinquent, above the usual sub-1%% band." % dpct))

    nak = val.get("nakamoto_coefficient")
    if nak is not None and nak < 15:
        findings.append(_f("warning", "nakamoto", "Nakamoto coefficient", nak, ">= 15",
                           "Only %d validators together control a third of stake — the "
                           "liveness-halting threshold." % nak))

    for key, label, sev, limit in (("change_1d_pct", "TVL 1d change", "warning", 10.0),
                                   ("change_7d_pct", "TVL 7d change", "warning", 25.0)):
        v = tvl.get(key)
        if v is not None and abs(v) >= limit:
            findings.append(_f(sev, "tvl_move", label, v, "|change| < %g%%" % limit,
                               "DeFi TVL moved %+.2f%% — a large shift worth attributing to a "
                               "specific protocol before trusting it." % v))

    chg = mkt.get("change_24h_pct")
    if chg is not None and abs(chg) >= 10.0:
        findings.append(_f("warning", "price_move", "SOL 24h change", chg, "|change| < 10%",
                           "SOL moved %+.2f%% in 24h." % chg))

    for name in ("network", "validators", "market", "tvl", "stablecoins", "dex", "fees"):
        section = snapshot.get(name) or {}
        if section.get("ok") is False:
            findings.append(_f("warning", "source_down", "Source: %s" % name,
                               "unavailable", "ok",
                               "The %s source failed this run (%s); its metrics are missing "
                               "from this snapshot." % (name, section.get("error"))))
    return findings


def historical_checks(snapshot_row, history):
    """history: prior summary rows, oldest-first, excluding the current row."""
    findings = []
    if len(history) < MIN_HISTORY:
        return findings
    for key, label, direction, warn_z, crit_z, unit, min_rel in Z_RULES:
        value = snapshot_row.get(key)
        if value is None:
            continue
        baseline = [r[key] for r in history if r.get(key) is not None]
        if len(baseline) < MIN_HISTORY:
            continue
        z, med, spread = _robust_z(value, baseline)
        if z is None or abs(z) < warn_z:
            continue
        if direction == "up" and z < 0:
            continue
        if direction == "down" and z > 0:
            continue
        if abs(value - med) < min_rel * abs(med):
            continue  # unusual for the baseline, but too small to be news
        sev = "critical" if abs(z) >= crit_z else "warning"
        findings.append(_f(
            sev, "zscore_%s" % key, label, value,
            "%s +/- %s (median of last %d)" % (_fmt(med, unit), _fmt(spread, unit), len(baseline)),
            "%s is %s, %.1f robust standard deviations %s its recent median of %s "
            "(%+.1f%%)."
            % (label, _fmt(value, unit), abs(z), "above" if z > 0 else "below",
               _fmt(med, unit), 100.0 * (value - med) / med if med else 0.0),
            z=round(z, 2),
        ))
    return findings


def _f(severity, code, metric, value, expected, message, z=None):
    finding = {
        "severity": severity,
        "code": code,
        "metric": metric,
        "value": value,
        "expected": expected,
        "message": message,
    }
    if z is not None:
        finding["z_score"] = z
    return finding


def detect(snapshot, snapshot_row, history):
    """Full pass. Returns findings sorted critical-first."""
    findings = absolute_checks(snapshot) + historical_checks(snapshot_row, history)
    order = {"critical": 0, "warning": 1, "info": 2}
    findings.sort(key=lambda f: order.get(f["severity"], 3))
    return findings
