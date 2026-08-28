"""Snapshot orchestration: run every collector, assemble one versioned object."""

import datetime

from . import sources

SCHEMA_VERSION = 1


def build_snapshot(rpc_endpoint=sources.DEFAULT_RPC, perf_samples=60, skip=()):
    """Collect every source into one snapshot dict.

    ``skip`` names sections to leave out (used by the test/offline path). No
    collector raises, so a snapshot is always produced; sections that failed
    carry ``ok: False`` and an error string.
    """
    started = datetime.datetime.now(datetime.timezone.utc)

    collectors = {
        "network": lambda: sources.collect_network(rpc_endpoint, perf_samples),
        "validators": lambda: sources.collect_validators(rpc_endpoint),
        "market": sources.collect_market,
        "tvl": sources.collect_tvl,
        "stablecoins": sources.collect_stablecoins,
        "dex": sources.collect_dex_volume,
        "fees": sources.collect_fees,
        "upgrades": sources.collect_upgrades,
    }

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources": {
            "solana_rpc": rpc_endpoint,
            "coingecko": sources.COINGECKO,
            "defillama": sources.LLAMA,
            "defillama_stablecoins": sources.LLAMA_STABLES,
            "github": sources.GITHUB,
        },
    }

    for name, fn in collectors.items():
        if name in skip:
            continue
        try:
            snapshot[name] = fn()
        except Exception as exc:  # a collector bug must not lose the whole run
            snapshot[name] = {"ok": False, "error": "collector raised: %r" % (exc,)}

    finished = datetime.datetime.now(datetime.timezone.utc)
    snapshot["collection_seconds"] = round((finished - started).total_seconds(), 2)
    snapshot["sources_ok"] = sum(
        1 for k in collectors if isinstance(snapshot.get(k), dict) and snapshot[k].get("ok")
    )
    snapshot["sources_total"] = len([k for k in collectors if k not in skip])
    return snapshot
