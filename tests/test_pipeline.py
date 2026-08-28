"""Offline tests. No network: every case runs against a fixture snapshot, so CI
is deterministic and a Solana RPC outage cannot turn the build red.
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solreport import anomaly, render_html, render_md, store  # noqa: E402


def fixture(**overrides):
    snap = {
        "schema_version": 1,
        "generated_at": "2026-01-01T00:00:00Z",
        "sources": {"solana_rpc": "https://api.mainnet-beta.solana.com"},
        "collection_seconds": 5.0,
        "sources_ok": 7,
        "sources_total": 7,
        "network": {
            "ok": True, "health": "ok", "version": "2.1.0",
            "epoch": {"epoch": 700, "absolute_slot": 300000000, "block_height": 280000000,
                      "slot_index": 216000, "slots_in_epoch": 432000, "progress_pct": 50.0,
                      "transaction_count": 400000000000},
            "performance": {"samples": 60, "window_minutes": 60.0, "tps_current": 3000.0,
                            "tps_mean": 3000.0, "tps_max": 3200.0, "tps_min": 2800.0,
                            "true_tps_current": 1200.0, "true_tps_mean": 1200.0,
                            "slot_time_mean_s": 0.4, "slot_time_max_s": 0.45,
                            "tps_series": [2900.0, 3000.0, 3100.0],
                            "slot_time_series": [0.39, 0.40, 0.41]},
            "supply": {"total_sol": 600000000.0, "circulating_sol": 550000000.0,
                       "non_circulating_sol": 50000000.0, "circulating_pct": 91.67},
        },
        "validators": {
            "ok": True, "active_count": 1000, "delinquent_count": 5, "total_count": 1005,
            "delinquent_pct": 0.5, "active_stake_sol": 400000000.0,
            "delinquent_stake_sol": 40000.0, "delinquent_stake_pct": 0.01,
            "total_stake_sol": 400040000.0, "nakamoto_coefficient": 20,
            "top1_stake_pct": 3.0, "top10_stake_pct": 22.0, "commission_mean": 8.0,
            "commission_median": 5, "zero_commission_count": 200,
            "top_validators": [{"vote_pubkey": "Vote111", "node_pubkey": "Node111",
                                "stake_sol": 12000000.0, "stake_pct": 3.0,
                                "commission": 5, "last_vote": 299999999}],
            "delinquent_validators": [{"vote_pubkey": "Bad111", "stake_sol": 40000.0,
                                       "last_vote": 299000000}],
        },
        "market": {"ok": True, "price_usd": 150.0, "market_cap_usd": 8.0e10,
                   "volume_24h_usd": 3.0e9, "change_24h_pct": 1.5},
        "tvl": {"ok": True, "tvl_usd": 8.0e9, "change_1d_pct": 0.5, "change_7d_pct": 2.0,
                "change_30d_pct": -3.0, "peak_90d_usd": 9.0e9,
                "series": [{"date": 1735689600 + i * 86400, "tvl": 8.0e9} for i in range(90)]},
        "stablecoins": {"ok": True, "usd_pegged": 1.2e10, "all_pegs_usd": 1.21e10,
                        "by_peg": {"peggedUSD": 1.2e10}},
        "dex": {"ok": True, "volume_24h_usd": 3.0e9, "volume_7d_usd": 2.0e10,
                "volume_30d_usd": 8.0e10, "change_1d_pct": 1.0, "change_7d_pct": 2.0,
                "protocol_count": 100,
                "top_protocols": [{"name": "Orca", "volume_24h_usd": 1.0e9}]},
        "fees": {"ok": True, "fees_24h_usd": 1.5e7, "fees_7d_usd": 1.0e8,
                 "fees_30d_usd": 4.0e8, "change_1d_pct": 2.0},
    }
    # Overrides replace a section wholesale rather than merging into it, so a
    # test can simulate a source that returned nothing but an error.
    snap.update(overrides)
    return snap


class TestStore(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_append_and_load_roundtrip(self):
        snap = fixture()
        store.append(self.dir, snap)
        store.append(self.dir, fixture(generated_at="2026-01-01T01:00:00Z"))
        rows = store.load(self.dir)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["ts"], "2026-01-01T00:00:00Z")
        self.assertEqual(rows[1]["ts"], "2026-01-01T01:00:00Z")
        self.assertEqual(rows[0]["price_usd"], 150.0)
        self.assertEqual(rows[0]["nakamoto_coefficient"], 20)

    def test_load_skips_corrupt_lines(self):
        store.append(self.dir, fixture())
        with open(os.path.join(self.dir, store.HISTORY_FILE), "a", encoding="utf-8") as fh:
            fh.write("{not json at all\n\n")
        self.assertEqual(len(store.load(self.dir)), 1)

    def test_load_missing_file_is_empty(self):
        self.assertEqual(store.load(os.path.join(self.dir, "nope")), [])

    def test_summary_survives_a_failed_source(self):
        row = store.summarize(fixture(market={"ok": False, "error": "boom"}))
        self.assertIsNone(row["price_usd"])
        self.assertEqual(row["tps_mean"], 3000.0)


class TestAnomaly(unittest.TestCase):
    def test_healthy_snapshot_is_quiet(self):
        snap = fixture()
        self.assertEqual(anomaly.detect(snap, store.summarize(snap), []), [])

    def test_slow_slots_are_critical(self):
        snap = fixture()
        snap["network"]["performance"]["slot_time_mean_s"] = 1.2
        codes = [f["code"] for f in anomaly.detect(snap, store.summarize(snap), [])]
        self.assertIn("slot_time", codes)
        self.assertEqual(
            [f["severity"] for f in anomaly.detect(snap, store.summarize(snap), [])
             if f["code"] == "slot_time"], ["critical"])

    def test_delinquent_stake_escalates(self):
        snap = fixture()
        snap["validators"]["delinquent_stake_pct"] = 7.5
        findings = anomaly.detect(snap, store.summarize(snap), [])
        self.assertTrue(any(f["code"] == "delinquent_stake" and f["severity"] == "critical"
                            for f in findings))

    def test_unhealthy_rpc_is_flagged(self):
        snap = fixture()
        snap["network"]["health"] = "behind"
        self.assertTrue(any(f["code"] == "rpc_health" for f in anomaly.detect(
            snap, store.summarize(snap), [])))

    def test_failed_source_is_reported_not_hidden(self):
        snap = fixture(tvl={"ok": False, "error": "timeout"})
        self.assertTrue(any(f["code"] == "source_down"
                            for f in anomaly.detect(snap, store.summarize(snap), [])))

    def test_zscore_needs_history_then_fires(self):
        snap = fixture()
        snap["market"]["price_usd"] = 400.0
        row = store.summarize(snap)
        # Too little history: no z-score finding.
        short = [dict(store.summarize(fixture()), ts="t%d" % i) for i in range(3)]
        self.assertFalse(any(f["code"].startswith("zscore")
                             for f in anomaly.detect(snap, row, short)))
        # Enough history at a stable baseline: the 400 outlier must fire.
        long = [dict(store.summarize(fixture()), ts="t%d" % i) for i in range(20)]
        for i, r in enumerate(long):
            r["price_usd"] = 150.0 + (i % 3)  # small real spread
        codes = [f["code"] for f in anomaly.detect(snap, row, long)]
        self.assertIn("zscore_price_usd", codes)

    def test_tiny_move_on_a_flat_baseline_is_not_reported(self):
        """A baseline with almost no spread makes ordinary drift score many
        sigma. The materiality gate must swallow it, or every quiet period
        produces a fake 'critical'."""
        snap = fixture()
        snap["market"]["price_usd"] = 151.5  # +1% on a 150 median: not news
        row = store.summarize(snap)
        history = [dict(store.summarize(fixture()), ts="t%d" % i) for i in range(20)]
        for i, r in enumerate(history):
            r["price_usd"] = 150.0 + (i % 2) * 0.01  # spread of one cent
        codes = [f["code"] for f in anomaly.detect(snap, row, history)]
        self.assertNotIn("zscore_price_usd", codes)
        # ...but a move that clears the gate on that same baseline still fires.
        snap["market"]["price_usd"] = 180.0
        codes = [f["code"] for f in anomaly.detect(snap, store.summarize(snap), history)]
        self.assertIn("zscore_price_usd", codes)

    def test_zero_variance_baseline_does_not_divide_by_zero(self):
        snap = fixture()
        snap["market"]["price_usd"] = 150.0
        history = [store.summarize(fixture()) for _ in range(20)]
        anomaly.detect(snap, store.summarize(snap), history)  # must not raise

    def test_findings_sorted_critical_first(self):
        snap = fixture()
        snap["network"]["performance"]["slot_time_mean_s"] = 1.2   # critical
        snap["validators"]["nakamoto_coefficient"] = 9             # warning
        findings = anomaly.detect(snap, store.summarize(snap), [])
        self.assertEqual(findings[0]["severity"], "critical")


class TestRenderers(unittest.TestCase):
    def test_markdown_contains_every_section(self):
        snap = fixture()
        md = render_md.render(snap, [], [store.summarize(snap)])
        for heading in ("# Solana Ecosystem Report", "## At a glance", "## Anomalies",
                        "## Network performance", "## Validator set", "## Economics",
                        "## Data sources"):
            self.assertIn(heading, md)
        self.assertIn("Vote111", md)

    def test_markdown_renders_findings(self):
        snap = fixture()
        snap["network"]["performance"]["slot_time_mean_s"] = 1.2
        findings = anomaly.detect(snap, store.summarize(snap), [])
        md = render_md.render(snap, findings, [])
        self.assertIn("critical", md)
        self.assertNotIn("No anomalies detected", md)

    def test_markdown_survives_missing_sections(self):
        snap = fixture(market={"ok": False, "error": "down"},
                       tvl={"ok": False, "error": "down"})
        md = render_md.render(snap, [], [])
        self.assertIn("n/a", md)

    def test_html_is_self_contained(self):
        snap = fixture()
        html = render_html.render(snap, [], [store.summarize(snap)])
        self.assertIn("<!doctype html>", html)
        self.assertIn("__SNAPSHOT__", html)
        # No external resources: the dashboard must open offline.
        for bad in ("src=\"http", "href=\"http", "cdn.", "googleapis"):
            self.assertNotIn(bad, html)

    def test_html_embeds_parseable_json(self):
        snap = fixture()
        html = render_html.render(snap, [], [])
        blob = html.split("window.__SNAPSHOT__ = ", 1)[1].split(";</script>", 1)[0]
        parsed = json.loads(blob.replace("<\\/", "</"))
        self.assertEqual(parsed["network"]["epoch"]["epoch"], 700)

    def test_html_escapes_closing_script_tags(self):
        snap = fixture()
        snap["network"]["version"] = "</script><script>alert(1)</script>"
        html = render_html.render(snap, [], [])
        blob = html.split("window.__SNAPSHOT__ = ", 1)[1].split(";</script>", 1)[0]
        self.assertNotIn("</script>", blob)


if __name__ == "__main__":
    unittest.main()
