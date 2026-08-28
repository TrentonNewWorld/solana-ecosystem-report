"""Append-only snapshot history.

Every run writes one line of JSON to ``data/history.jsonl``. That file is the
dataset: the report, the charts and the anomaly detector all read from it, so a
report generated at any time is reproducible from the history alone. Storing
only a compact summary per snapshot (not the full payload) keeps the file small
enough to live in git and be committed by CI on every refresh.
"""

import json
import os

HISTORY_FILE = "history.jsonl"


def _path(data_dir):
    return os.path.join(data_dir, HISTORY_FILE)


def summarize(snapshot):
    """Reduce a full snapshot to the scalar series worth keeping forever."""
    net = snapshot.get("network") or {}
    perf = net.get("performance") or {}
    epoch = net.get("epoch") or {}
    val = snapshot.get("validators") or {}
    mkt = snapshot.get("market") or {}
    tvl = snapshot.get("tvl") or {}
    stables = snapshot.get("stablecoins") or {}
    dex = snapshot.get("dex") or {}
    fees = snapshot.get("fees") or {}
    return {
        "ts": snapshot["generated_at"],
        "epoch": epoch.get("epoch"),
        "epoch_progress_pct": epoch.get("progress_pct"),
        "block_height": epoch.get("block_height"),
        "tps_mean": perf.get("tps_mean"),
        "true_tps_mean": perf.get("true_tps_mean"),
        "slot_time_mean_s": perf.get("slot_time_mean_s"),
        "validators_active": val.get("active_count"),
        "validators_delinquent": val.get("delinquent_count"),
        "delinquent_stake_pct": val.get("delinquent_stake_pct"),
        "nakamoto_coefficient": val.get("nakamoto_coefficient"),
        "price_usd": mkt.get("price_usd"),
        "tvl_usd": tvl.get("tvl_usd"),
        "stablecoin_usd": stables.get("usd_pegged"),
        "dex_volume_24h_usd": dex.get("volume_24h_usd"),
        "fees_24h_usd": fees.get("fees_24h_usd"),
    }


def append(data_dir, snapshot):
    os.makedirs(data_dir, exist_ok=True)
    row = summarize(snapshot)
    with open(_path(data_dir), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")
    return row


def load(data_dir, limit=None):
    """Return history oldest-first. Bad lines are skipped, never fatal."""
    path = _path(data_dir)
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows[-limit:] if limit else rows


def series(rows, key):
    """Non-null values of one metric, oldest-first."""
    return [r[key] for r in rows if r.get(key) is not None]
