"""`python -m solreport` — collect, detect, render, in one command."""

import argparse
import json
import os
import sys

from . import anomaly, collect, render_html, render_md, sources, store


def build_parser():
    p = argparse.ArgumentParser(
        prog="solreport",
        description="Generate an auto-updating Solana ecosystem report "
                    "(HTML dashboard + Markdown + JSON) from keyless public sources.")
    p.add_argument("--out", default="output", help="output directory (default: output)")
    p.add_argument("--data", default="data", help="snapshot history directory (default: data)")
    p.add_argument("--rpc", default=sources.DEFAULT_RPC,
                   help="Solana JSON-RPC endpoint (default: public mainnet-beta)")
    p.add_argument("--perf-samples", type=int, default=60,
                   help="performance samples to fetch, ~1 minute each (default: 60)")
    p.add_argument("--no-history", action="store_true",
                   help="do not append this snapshot to the history file")
    p.add_argument("--quiet", action="store_true", help="suppress the console summary")
    p.add_argument("--fail-on-critical", action="store_true",
                   help="exit 2 if any critical anomaly is detected (for alerting in CI)")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    os.makedirs(args.out, exist_ok=True)

    snapshot = collect.build_snapshot(rpc_endpoint=args.rpc, perf_samples=args.perf_samples)
    row = store.summarize(snapshot)

    history_before = store.load(args.data)
    findings = anomaly.detect(snapshot, row, history_before)
    snapshot["anomalies"] = findings

    if not args.no_history:
        store.append(args.data, snapshot)
    history = history_before + [row]

    paths = {
        "json": os.path.join(args.out, "report.json"),
        "markdown": os.path.join(args.out, "report.md"),
        "html": os.path.join(args.out, "index.html"),
    }
    with open(paths["json"], "w", encoding="utf-8") as fh:
        json.dump(snapshot, fh, indent=2)
    with open(paths["markdown"], "w", encoding="utf-8") as fh:
        fh.write(render_md.render(snapshot, findings, history))
    with open(paths["html"], "w", encoding="utf-8") as fh:
        fh.write(render_html.render(snapshot, findings, history))

    if not args.quiet:
        crit = sum(1 for f in findings if f["severity"] == "critical")
        print("solreport %s" % snapshot["generated_at"])
        print("  sources    %s/%s healthy in %ss"
              % (snapshot.get("sources_ok"), snapshot.get("sources_total"),
                 snapshot.get("collection_seconds")))
        print("  history    %d snapshots" % len(history))
        print("  anomalies  %d (%d critical)" % (len(findings), crit))
        for f in findings:
            print("    [%s] %s" % (f["severity"], f["message"]))
        for label, path in paths.items():
            print("  %-10s %s" % (label, path))

    if args.fail_on_critical and any(f["severity"] == "critical" for f in findings):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
