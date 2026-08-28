"""Interactive dark-theme HTML dashboard.

Single self-contained file: the snapshot is embedded as JSON and all charts are
SVG drawn by ~200 lines of vanilla JS. No CDN, no build step, no network calls at
view time — so the dashboard opens from `file://`, from GitHub Pages, or from an
air-gapped machine, and it still works in five years when today's chart library
has had four breaking releases.
"""

import json

CSS = """
:root{
  --bg:#0b0f14; --panel:#121820; --panel-2:#171f29; --line:#1f2a37;
  --text:#e6edf3; --muted:#8b9aad; --dim:#5d6b7d;
  --accent:#14f195;   /* Solana green */
  --accent-2:#9945ff; /* Solana purple */
  --warn:#f0a92b; --crit:#ff5c5c; --ok:#14f195;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);
  font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
.wrap{max-width:1180px;margin:0 auto;padding:32px 20px 72px}
header{display:flex;flex-wrap:wrap;gap:16px;align-items:baseline;justify-content:space-between;
  border-bottom:1px solid var(--line);padding-bottom:20px;margin-bottom:28px}
h1{font-size:26px;margin:0;letter-spacing:-.02em}
h1 .dot{color:var(--accent)}
h2{font-size:14px;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);
  margin:38px 0 14px;font-weight:600}
.meta{font-family:var(--mono);font-size:12px;color:var(--dim);text-align:right}
.meta b{color:var(--muted);font-weight:500}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(224px,1fr))}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tile .k{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted)}
.tile .v{font-size:25px;font-family:var(--mono);margin:6px 0 2px;letter-spacing:-.02em;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tile .v .u{font-size:14px;color:var(--muted);margin-left:4px;letter-spacing:0}
.tile .s{font-size:12px;color:var(--dim);font-family:var(--mono)}
.up{color:var(--ok)} .down{color:var(--crit)} .flat{color:var(--muted)}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px}
.panel h3{margin:0 0 4px;font-size:15px}
.panel .sub{color:var(--dim);font-size:12px;margin-bottom:14px}
.two{display:grid;gap:12px;grid-template-columns:1fr 1fr}
@media(max-width:820px){.two{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;font-weight:600;color:var(--muted);font-size:11px;text-transform:uppercase;
  letter-spacing:.06em;padding:8px 10px;border-bottom:1px solid var(--line);cursor:pointer;
  user-select:none;white-space:nowrap}
th:hover{color:var(--text)}
th.sorted::after{content:" ▾";color:var(--accent)}
th.sorted.asc::after{content:" ▴"}
td{padding:8px 10px;border-bottom:1px solid #151d27;font-family:var(--mono);font-size:12.5px}
tbody tr:hover{background:var(--panel-2)}
td.num{text-align:right}
.k-mono{color:var(--muted)}
.scroll{overflow-x:auto}
.finding{display:flex;gap:12px;padding:12px 14px;border-radius:8px;margin-bottom:8px;
  border:1px solid var(--line);background:var(--panel-2)}
.finding.critical{border-left:3px solid var(--crit)}
.finding.warning{border-left:3px solid var(--warn)}
.finding .sev{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.08em;
  padding-top:3px;min-width:62px}
.finding.critical .sev{color:var(--crit)} .finding.warning .sev{color:var(--warn)}
.finding .msg{font-size:13.5px}
.finding .det{color:var(--dim);font-size:11.5px;font-family:var(--mono);margin-top:3px}
.clear{display:flex;gap:10px;align-items:center;color:var(--muted);font-size:13.5px;
  border:1px solid var(--line);border-left:3px solid var(--ok);border-radius:8px;
  padding:12px 14px;background:var(--panel-2)}
.controls{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.controls button{background:var(--panel-2);color:var(--muted);border:1px solid var(--line);
  border-radius:6px;padding:4px 11px;font-size:12px;font-family:var(--mono);cursor:pointer}
.controls button:hover{color:var(--text);border-color:var(--dim)}
.controls button[aria-pressed=true]{background:rgba(20,241,149,.12);color:var(--accent);
  border-color:rgba(20,241,149,.45)}
.bar{height:7px;background:var(--panel-2);border-radius:4px;overflow:hidden;margin-top:7px}
.bar > i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent))}
svg{display:block;width:100%;height:auto;overflow:visible}
.src{font-family:var(--mono);font-size:11.5px;color:var(--dim)}
footer{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);
  color:var(--dim);font-size:12px}
.badge{font-family:var(--mono);font-size:11px;padding:2px 7px;border-radius:20px;
  border:1px solid var(--line);color:var(--muted)}
.badge.ok{color:var(--ok);border-color:rgba(20,241,149,.35)}
.badge.bad{color:var(--crit);border-color:rgba(255,92,92,.35)}
"""

JS = r"""
const D = window.__SNAPSHOT__;

const fmtUsd = (v, d) => {
  if (v == null) return 'n/a';
  const a = Math.abs(v);
  if (a >= 1e9) return '$' + (v/1e9).toFixed(2) + 'B';
  if (a >= 1e6) return '$' + (v/1e6).toFixed(2) + 'M';
  if (a >= 1e3) return '$' + (v/1e3).toFixed(1) + 'K';
  return '$' + v.toFixed(d == null ? 2 : d);
};
const fmtNum = (v, d=0) => v == null ? 'n/a'
  : v.toLocaleString('en-US', {minimumFractionDigits:d, maximumFractionDigits:d});
const fmtPct = (v, d=2) => v == null ? 'n/a' : (v>=0?'+':'') + v.toFixed(d) + '%';
const cls = v => v == null ? 'flat' : (v > 0 ? 'up' : (v < 0 ? 'down' : 'flat'));

/* ---------- charts: hand-rolled SVG, no dependencies ---------- */
function lineChart(el, pts, opts={}) {
  if (!pts || pts.length < 2) { el.innerHTML = '<p class="src">not enough data yet</p>'; return; }
  const W = 720, H = opts.height || 190, P = {t:14, r:56, b:22, l:6};
  const ys = pts.map(p => p.y);
  let min = Math.min(...ys), max = Math.max(...ys);
  if (opts.zero) min = Math.min(0, min);
  const pad = (max - min) * 0.12 || Math.abs(max) * 0.1 || 1;
  min -= pad; max += pad;
  const x = i => P.l + (i / (pts.length - 1)) * (W - P.l - P.r);
  const y = v => P.t + (1 - (v - min) / (max - min)) * (H - P.t - P.b);
  const line = pts.map((p,i) => (i?'L':'M') + x(i).toFixed(1) + ' ' + y(p.y).toFixed(1)).join(' ');
  const area = line + ` L${x(pts.length-1).toFixed(1)} ${H-P.b} L${x(0).toFixed(1)} ${H-P.b} Z`;
  const gid = 'g' + Math.abs(el.id.split('').reduce((a,c)=>a+c.charCodeAt(0),0));
  const ticks = [max - pad*0.9, (max+min)/2, min + pad*0.9];
  const fmt = opts.fmt || (v => fmtNum(v, opts.decimals || 0));
  const last = pts[pts.length-1];
  el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img"
      aria-label="${opts.label || 'time series'}: ${fmt(last.y)} latest">
    <defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${opts.color || '#14f195'}" stop-opacity=".28"/>
      <stop offset="100%" stop-color="${opts.color || '#14f195'}" stop-opacity="0"/>
    </linearGradient></defs>
    ${ticks.map(t => `<g><line x1="${P.l}" x2="${W-P.r}" y1="${y(t).toFixed(1)}" y2="${y(t).toFixed(1)}"
        stroke="#1f2a37" stroke-dasharray="2 4"/>
      <text x="${W-P.r+8}" y="${(y(t)+4).toFixed(1)}" fill="#5d6b7d" font-size="11"
        font-family="ui-monospace,monospace">${fmt(t)}</text></g>`).join('')}
    <path d="${area}" fill="url(#${gid})"/>
    <path d="${line}" fill="none" stroke="${opts.color || '#14f195'}" stroke-width="1.8"
      stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${x(pts.length-1).toFixed(1)}" cy="${y(last.y).toFixed(1)}" r="3.2"
      fill="${opts.color || '#14f195'}"/>
    <text x="${P.l}" y="${H-6}" fill="#5d6b7d" font-size="11"
      font-family="ui-monospace,monospace">${pts[0].label || ''}</text>
    <text x="${W-P.r}" y="${H-6}" fill="#5d6b7d" font-size="11" text-anchor="end"
      font-family="ui-monospace,monospace">${last.label || ''}</text>
  </svg>`;
}

function barChart(el, rows, opts={}) {
  if (!rows || !rows.length) { el.innerHTML = '<p class="src">no data</p>'; return; }
  const max = Math.max(...rows.map(r => r.value));
  const fmt = opts.fmt || fmtUsd;
  el.innerHTML = rows.map(r => `
    <div style="margin-bottom:11px">
      <div style="display:flex;justify-content:space-between;font-size:12.5px;
        font-family:ui-monospace,monospace">
        <span>${r.label}</span><span class="k-mono">${fmt(r.value)}</span></div>
      <div class="bar"><i style="width:${(100*r.value/max).toFixed(1)}%"></i></div>
    </div>`).join('');
}

/* ---------- interactive range filter on the TVL series ---------- */
const tvlSeries = ((D.tvl && D.tvl.series) || []).map(p => ({
  y: p.tvl,
  label: new Date(p.date * 1000).toISOString().slice(0, 10)
}));
function drawTvl(days) {
  const pts = tvlSeries.slice(-days);
  lineChart(document.getElementById('chart-tvl'), pts,
    {color:'#9945ff', fmt:fmtUsd, label:'Solana DeFi TVL'});
  document.querySelectorAll('#tvl-range button').forEach(b =>
    b.setAttribute('aria-pressed', String(+b.dataset.days === days)));
}

/* ---------- sortable tables ---------- */
function sortable(table) {
  const tbody = table.querySelector('tbody');
  table.querySelectorAll('th').forEach((th, i) => {
    th.addEventListener('click', () => {
      const asc = !(th.classList.contains('sorted') && !th.classList.contains('asc'));
      table.querySelectorAll('th').forEach(o => o.classList.remove('sorted','asc'));
      th.classList.add('sorted'); if (asc) th.classList.add('asc');
      const rows = [...tbody.rows].sort((a, b) => {
        const av = a.cells[i].dataset.v ?? a.cells[i].textContent;
        const bv = b.cells[i].dataset.v ?? b.cells[i].textContent;
        const an = parseFloat(av), bn = parseFloat(bv);
        const cmp = (!isNaN(an) && !isNaN(bn)) ? an - bn : String(av).localeCompare(String(bv));
        return asc ? cmp : -cmp;
      });
      rows.forEach(r => tbody.appendChild(r));
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const perf = (D.network && D.network.performance) || {};
  const tps = (perf.tps_series || []).map((v, i) => ({y: v, label: i === 0 ? 'older' : 'now'}));
  lineChart(document.getElementById('chart-tps'), tps,
    {color:'#14f195', label:'Transactions per second', zero:true});
  const slots = (perf.slot_time_series || []).map((v, i) => ({y: v, label: i === 0 ? 'older' : 'now'}));
  lineChart(document.getElementById('chart-slot'), slots,
    {color:'#f0a92b', decimals:3, fmt:v => v.toFixed(3)+'s', label:'Slot time', height:150});

  barChart(document.getElementById('chart-dex'),
    ((D.dex && D.dex.top_protocols) || []).map(p => ({label:p.name, value:p.volume_24h_usd || 0})));
  barChart(document.getElementById('chart-validators'),
    ((D.validators && D.validators.top_validators) || []).slice(0, 8).map(v =>
      ({label: v.vote_pubkey.slice(0, 12) + '…', value: v.stake_sol})),
    {fmt: v => fmtNum(v) + ' SOL'});

  if (tvlSeries.length) {
    drawTvl(90);
    document.querySelectorAll('#tvl-range button').forEach(b =>
      b.addEventListener('click', () => drawTvl(+b.dataset.days)));
  }

  const hist = (D.history || []);
  if (hist.length >= 2) {
    const pts = hist.filter(h => h.price_usd != null)
      .map(h => ({y: h.price_usd, label: h.ts.slice(5, 16).replace('T',' ')}));
    lineChart(document.getElementById('chart-history'), pts,
      {color:'#14f195', fmt:v=>fmtUsd(v,2), label:'SOL price across snapshots'});
  }

  document.querySelectorAll('table').forEach(sortable);
});
"""


def _esc(t):
    """PR titles and release names are third-party text. Escape them rather than
    trusting whatever someone typed into a GitHub title field."""
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _usd(v):
    if v is None:
        return "n/a"
    for unit, scale in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(v) >= scale:
            return "$%.2f%s" % (v / scale, unit)
    return "$%.2f" % v


def _num(v, d=0):
    if v is None:
        return "n/a"
    if d:  # fixed precision: "$107.30", never "$107.3"
        return format(v, ",.%df" % d)
    return format(round(v), ",")


def _compact(v, d=2):
    """Hero-number form of a large count. The exact figure belongs on the sub-line."""
    if v is None:
        return "n/a"
    for unit, scale in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(v) >= scale:
            return "%.*f%s" % (d, v / scale, unit)
    return format(round(v), ",")


def _pct(v, d=2, sign=False):
    if v is None:
        return "n/a"
    return ("%+.*f%%" if sign else "%.*f%%") % (d, v)


def _cls(v):
    if v is None:
        return "flat"
    return "up" if v > 0 else ("down" if v < 0 else "flat")


def _tile(k, v, s="", scls="flat"):
    return ('<div class="tile"><div class="k">%s</div><div class="v">%s</div>'
            '<div class="s %s">%s</div></div>' % (k, v, scls, s))


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

    payload = dict(snapshot)
    payload["history"] = history[-200:]
    data_json = json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")

    crit = sum(1 for f in findings if f["severity"] == "critical")
    health_ok = net.get("health") == "ok"

    tiles = "".join([
        _tile("True TPS (non-vote)", _num(perf.get("true_tps_current")),
              "mean %s over %s min" % (_num(perf.get("true_tps_mean")), perf.get("window_minutes"))),
        _tile("Slot time", "%ss" % (perf.get("slot_time_mean_s") or "n/a"),
              "worst %ss · target ~0.4s" % (perf.get("slot_time_max_s") or "n/a")),
        _tile("Epoch", str(epoch.get("epoch") or "n/a"),
              "%s complete" % _pct(epoch.get("progress_pct"))),
        _tile("Active validators", _num(val.get("active_count")),
              "%s delinquent · %s of stake"
              % (_num(val.get("delinquent_count")), _pct(val.get("delinquent_stake_pct"), 3))),
        _tile("Nakamoto coefficient", str(val.get("nakamoto_coefficient") or "n/a"),
              "validators to halt liveness"),
        _tile("SOL price", "$%s" % _num(mkt.get("price_usd"), 2),
              "%s 24h" % _pct(mkt.get("change_24h_pct"), 2, True), _cls(mkt.get("change_24h_pct"))),
        _tile("DeFi TVL", _usd(tvl.get("tvl_usd")),
              "%s 7d" % _pct(tvl.get("change_7d_pct"), 2, True), _cls(tvl.get("change_7d_pct"))),
        _tile("Stablecoins on Solana", _usd(stables.get("usd_pegged")), "USD peg, circulating"),
        _tile("DEX volume 24h", _usd(dex.get("volume_24h_usd")),
              "%s 1d · %s protocols" % (_pct(dex.get("change_1d_pct"), 2, True), dex.get("protocol_count")),
              _cls(dex.get("change_1d_pct"))),
        _tile("Fees + app revenue 24h", _usd(fees.get("fees_24h_usd")),
              "%s 1d" % _pct(fees.get("change_1d_pct"), 2, True), _cls(fees.get("change_1d_pct"))),
        _tile("Circulating supply",
              '%s<span class="u">SOL</span>' % _compact(supply.get("circulating_sol")),
              "%s of total supply" % _pct(supply.get("circulating_pct"))),
        _tile("Lifetime transactions", _compact(epoch.get("transaction_count")),
              "block height %s" % _num(epoch.get("block_height"))),
    ])

    if findings:
        anomalies = "".join(
            '<div class="finding %s"><div class="sev">%s</div><div><div class="msg">%s</div>'
            '<div class="det">%s &middot; observed %s &middot; expected %s</div></div></div>'
            % (f["severity"], f["severity"], f["message"], f["metric"], f["value"], f["expected"])
            for f in findings)
    else:
        extra = ("and within normal variance of its recent median"
                 if len(history) >= 8 else
                 "; z-score checks activate at 8 snapshots (currently %d)" % len(history))
        anomalies = ('<div class="clear"><span>&#10003;</span><span>No anomalies. '
                     'Every monitored metric is inside its absolute safety band %s.</span></div>' % extra)

    val_rows = "".join(
        '<tr><td class="num">%d</td><td class="k-mono">%s</td>'
        '<td class="num" data-v="%s">%s</td><td class="num" data-v="%s">%s</td>'
        '<td class="num" data-v="%s">%s%%</td></tr>'
        % (i, v["vote_pubkey"], v["stake_sol"], _num(v["stake_sol"]),
           v["stake_pct"], _pct(v["stake_pct"], 3), v["commission"], v["commission"])
        for i, v in enumerate(val.get("top_validators") or [], 1))

    delinq = val.get("delinquent_validators") or []
    delinq_rows = "".join(
        '<tr><td class="k-mono">%s</td><td class="num" data-v="%s">%s</td>'
        '<td class="num" data-v="%s">%s</td></tr>'
        % (v["vote_pubkey"], v["stake_sol"], _num(v["stake_sol"]), v["last_vote"], _num(v["last_vote"]))
        for v in delinq)
    delinq_block = ("""
    <div class="panel" style="margin-top:12px">
      <h3>Delinquent validators</h3>
      <div class="sub">Not voting. Their stake still counts against liveness until it is deactivated.</div>
      <div class="scroll"><table><thead><tr><th>Vote account</th><th>Stake (SOL)</th>
        <th>Last vote slot</th></tr></thead><tbody>%s</tbody></table></div>
    </div>""" % delinq_rows) if delinq_rows else ""

    upg = snapshot.get("upgrades") or {}
    simd_rows = "".join(
        '<tr><td class="k-mono">%s</td><td><a href="%s">%s</a>%s</td><td class="num">%s</td></tr>'
        % ("SIMD-%s" % d["simd"] if d.get("simd") else "&mdash;",
           _esc(d.get("url") or "#"), _esc(d.get("title") or ""),
           ' <span class="badge">draft</span>' if d.get("draft") else "",
           (d.get("updated_at") or "")[:10])
        for d in (upg.get("simds") or []))
    rel_rows = "".join(
        '<tr><td class="k-mono"><a href="%s">%s</a></td><td>%s</td><td class="num">%s</td></tr>'
        % (_esc(r.get("url") or "#"), _esc(r.get("tag") or ""),
           _esc(r.get("name") or ""), (r.get("published_at") or "")[:10])
        for r in (upg.get("releases") or []))
    upgrades_block = ("""
    <h2>Protocol roadmap</h2>
    <div class="two">
      <div class="panel">
        <h3>Proposed changes &middot; open SIMDs</h3>
        <div class="sub">Most recently updated open pull requests against the Solana
          Improvement Documents repo &mdash; what the protocol is being asked to change,
          read straight from the source of record rather than a hand-kept list.</div>
        <div class="scroll"><table><thead><tr><th>SIMD</th><th>Proposal</th><th>Updated</th>
          </tr></thead><tbody>%s</tbody></table></div>
      </div>
      <div class="panel">
        <h3>Shipped &middot; Agave validator releases</h3>
        <div class="sub">What validators are actually being asked to run. A proposal only
          matters once it lands in a client release.</div>
        <div class="scroll"><table><thead><tr><th>Tag</th><th>Release</th><th>Published</th>
          </tr></thead><tbody>%s</tbody></table></div>
      </div>
    </div>""" % (simd_rows, rel_rows)) if simd_rows else ""

    history_block = ("""
    <h2>Across snapshots</h2>
    <div class="panel">
      <h3>SOL price, every snapshot in history</h3>
      <div class="sub">%d snapshots collected. This chart is drawn from
        <code>data/history.jsonl</code>, the same file the anomaly detector uses as its baseline.</div>
      <div id="chart-history"></div>
    </div>""" % len(history)) if len(history) >= 2 else ""

    return """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solana Ecosystem Report &middot; %(ts)s</title>
<meta name="description" content="Auto-updating report on the state of the Solana ecosystem: network performance, validator health, and economics, from keyless public sources.">
<style>%(css)s</style>
</head><body>
<div class="wrap">
<header>
  <div>
    <h1>Solana Ecosystem Report<span class="dot">.</span></h1>
    <div class="src">Network performance, validator health and economics &mdash;
      regenerated from live public sources on every refresh.</div>
  </div>
  <div class="meta">
    <div><b>snapshot</b> %(ts)s</div>
    <div><b>sources</b> %(ok)s/%(total)s healthy in %(secs)ss</div>
    <div><b>rpc</b> <span class="badge %(hcls)s">%(health)s</span>
         <span class="badge">%(version)s</span></div>
    <div><b>anomalies</b> %(nfind)s (%(ncrit)s critical)</div>
  </div>
</header>

<h2>Key metrics</h2>
<div class="grid">%(tiles)s</div>

<h2>Anomaly detection</h2>
%(anomalies)s

<h2>Network performance</h2>
<div class="two">
  <div class="panel">
    <h3>Transactions per second</h3>
    <div class="sub">Last %(window)s minutes, one point per RPC performance sample.
      Includes consensus votes; the non-vote figure is in the tiles above.</div>
    <div id="chart-tps"></div>
  </div>
  <div class="panel">
    <h3>Slot time</h3>
    <div class="sub">Seconds per slot. Solana targets ~0.4s; sustained rises above
      0.65s are the earliest sign of network stress.</div>
    <div id="chart-slot"></div>
  </div>
</div>

<h2>Value and activity</h2>
<div class="two">
  <div class="panel">
    <h3>DeFi TVL</h3>
    <div class="sub">Total value locked across Solana DeFi. Click a range to refilter.</div>
    <div class="controls" id="tvl-range">
      <button data-days="7">7d</button><button data-days="30">30d</button>
      <button data-days="90" aria-pressed="true">90d</button>
    </div>
    <div id="chart-tvl"></div>
  </div>
  <div class="panel">
    <h3>DEX volume by protocol &middot; 24h</h3>
    <div class="sub">Where the %(dexvol)s of 24-hour swap volume actually traded.</div>
    <div id="chart-dex"></div>
  </div>
</div>

<h2>Validator set</h2>
<div class="two">
  <div class="panel">
    <h3>Stake concentration</h3>
    <div class="sub">Top validators by activated stake. Top 10 hold %(top10)s of all stake;
      %(nak)s validators together reach the 33%% liveness threshold.</div>
    <div id="chart-validators"></div>
  </div>
  <div class="panel">
    <h3>Top validators</h3>
    <div class="sub">Click any column header to sort.</div>
    <div class="scroll"><table><thead><tr><th>#</th><th>Vote account</th>
      <th>Stake (SOL)</th><th>Share</th><th>Commission</th></tr></thead>
      <tbody>%(valrows)s</tbody></table></div>
  </div>
</div>
%(delinq)s
%(upgrades)s
%(history)s

<h2>Data sources</h2>
<div class="panel">
  <div class="scroll"><table><thead><tr><th>Source</th><th>Used for</th><th>API key</th>
    </tr></thead><tbody>
    <tr><td class="k-mono">%(rpc)s</td><td>epoch, slots, TPS, slot time, supply, validators</td>
      <td>none</td></tr>
    <tr><td class="k-mono">api.coingecko.com</td><td>SOL price, market cap, spot volume</td>
      <td>none</td></tr>
    <tr><td class="k-mono">api.llama.fi</td><td>DeFi TVL (90d), DEX volume, chain fees</td>
      <td>none</td></tr>
    <tr><td class="k-mono">stablecoins.llama.fi</td><td>stablecoin supply on Solana, by peg</td>
      <td>none</td></tr>
    <tr><td class="k-mono">api.github.com</td><td>open SIMD proposals, Agave client releases</td>
      <td>none</td></tr>
  </tbody></table></div>
</div>

<footer>
  Generated by <code>solreport</code> &mdash; Python standard library only, no API keys,
  no third-party packages, no build step. Machine-readable output:
  <code>report.json</code>. Snapshot history: <code>data/history.jsonl</code>.
</footer>
</div>
<script>window.__SNAPSHOT__ = %(data)s;</script>
<script>%(js)s</script>
</body></html>
""" % {
        "css": CSS,
        "js": JS,
        "data": data_json,
        "ts": snapshot["generated_at"],
        "ok": snapshot.get("sources_ok"),
        "total": snapshot.get("sources_total"),
        "secs": snapshot.get("collection_seconds"),
        "health": net.get("health") or "unknown",
        "hcls": "ok" if health_ok else "bad",
        "version": net.get("version") or "unknown",
        "nfind": len(findings),
        "ncrit": crit,
        "tiles": tiles,
        "anomalies": anomalies,
        "window": perf.get("window_minutes") or "?",
        "dexvol": _usd(dex.get("volume_24h_usd")),
        "top10": _pct(val.get("top10_stake_pct")),
        "nak": val.get("nakamoto_coefficient"),
        "valrows": val_rows,
        "delinq": delinq_block,
        "upgrades": upgrades_block,
        "history": history_block,
        "rpc": (snapshot["sources"]["solana_rpc"] or "").replace("https://", ""),
    }
