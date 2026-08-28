"""Data collectors. Every source here is public and keyless.

Each collector returns a plain dict and never raises: a source that is down
yields ``{"ok": False, "error": ...}`` so the report still renders with the
metrics that did resolve. Partial data is far more useful than no report.
"""

import datetime
import re
import statistics

from .http import FetchError, RpcClient, get_json

LAMPORTS_PER_SOL = 1_000_000_000

DEFAULT_RPC = "https://api.mainnet-beta.solana.com"
COINGECKO = "https://api.coingecko.com/api/v3"
LLAMA = "https://api.llama.fi"
LLAMA_STABLES = "https://stablecoins.llama.fi"
GITHUB = "https://api.github.com"


def _utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def _ok(**kw):
    d = {"ok": True}
    d.update(kw)
    return d


def _fail(exc):
    return {"ok": False, "error": str(exc)}


# --------------------------------------------------------------------------
# On-chain: Solana RPC
# --------------------------------------------------------------------------

def collect_network(rpc_endpoint=DEFAULT_RPC, perf_samples=60):
    """Network performance + epoch progress + supply, in one batched RPC call.

    ``getRecentPerformanceSamples`` returns one entry per ~60s slot window, so
    60 samples is roughly the last hour of throughput.
    """
    rpc = RpcClient(rpc_endpoint)
    try:
        health, epoch, perf, supply, version, blockhash = rpc.batch([
            ("getHealth", None),
            ("getEpochInfo", None),
            ("getRecentPerformanceSamples", [perf_samples]),
            ("getSupply", [{"commitment": "finalized",
                            "excludeNonCirculatingAccountsList": True}]),
            ("getVersion", None),
            ("getLatestBlockhash", None),
        ])
    except FetchError as exc:
        return _fail(exc)

    out = {"ok": True, "endpoint": rpc_endpoint, "health": health}

    if epoch:
        slots_in_epoch = epoch.get("slotsInEpoch") or 0
        slot_index = epoch.get("slotIndex") or 0
        out["epoch"] = {
            "epoch": epoch.get("epoch"),
            "absolute_slot": epoch.get("absoluteSlot"),
            "block_height": epoch.get("blockHeight"),
            "slot_index": slot_index,
            "slots_in_epoch": slots_in_epoch,
            "progress_pct": round(100.0 * slot_index / slots_in_epoch, 2) if slots_in_epoch else None,
            "transaction_count": epoch.get("transactionCount"),
        }
        # Skipped slots: the network schedules absoluteSlot slots but only
        # blockHeight of them produced a block. The gap is leader slots missed.
        abs_slot = epoch.get("absoluteSlot")
        height = epoch.get("blockHeight")
        if abs_slot and height:
            out["epoch"]["skipped_slots_lifetime"] = abs_slot - height

    if perf:
        tps, non_vote_tps, slot_times = [], [], []
        for s in perf:
            period = s.get("samplePeriodSecs") or 0
            if period <= 0:
                continue
            tps.append(s.get("numTransactions", 0) / period)
            if s.get("numNonVoteTransactions") is not None:
                non_vote_tps.append(s["numNonVoteTransactions"] / period)
            num_slots = s.get("numSlots") or 0
            if num_slots:
                slot_times.append(period / num_slots)
        if tps:
            out["performance"] = {
                "samples": len(tps),
                "window_minutes": round(len(tps) * (perf[0].get("samplePeriodSecs") or 60) / 60.0, 1),
                "tps_current": round(tps[0], 1),
                "tps_mean": round(statistics.fmean(tps), 1),
                "tps_max": round(max(tps), 1),
                "tps_min": round(min(tps), 1),
                "true_tps_current": round(non_vote_tps[0], 1) if non_vote_tps else None,
                "true_tps_mean": round(statistics.fmean(non_vote_tps), 1) if non_vote_tps else None,
                "slot_time_mean_s": round(statistics.fmean(slot_times), 3) if slot_times else None,
                "slot_time_max_s": round(max(slot_times), 3) if slot_times else None,
                # newest-first from the RPC; store oldest-first for charting
                "tps_series": [round(v, 1) for v in reversed(tps)],
                "slot_time_series": [round(v, 3) for v in reversed(slot_times)],
            }

    if supply and supply.get("value"):
        v = supply["value"]
        total = v.get("total", 0) / LAMPORTS_PER_SOL
        circulating = v.get("circulating", 0) / LAMPORTS_PER_SOL
        out["supply"] = {
            "total_sol": round(total, 2),
            "circulating_sol": round(circulating, 2),
            "non_circulating_sol": round(v.get("nonCirculating", 0) / LAMPORTS_PER_SOL, 2),
            "circulating_pct": round(100.0 * circulating / total, 2) if total else None,
        }

    if version:
        out["version"] = version.get("solana-core")
    if blockhash and blockhash.get("value"):
        out["latest_blockhash_slot"] = blockhash.get("context", {}).get("slot")
    return out


def collect_validators(rpc_endpoint=DEFAULT_RPC, top_n=10):
    """Validator set health: active vs delinquent, stake concentration, commission.

    Stake concentration is the number the ecosystem actually argues about, so we
    compute the Nakamoto coefficient (validators needed for 33.3% of stake, the
    liveness-halting threshold) rather than only listing the top validators.
    """
    rpc = RpcClient(rpc_endpoint, timeout=45)
    try:
        va = rpc.call("getVoteAccounts")
    except FetchError as exc:
        return _fail(exc)

    current = va.get("current") or []
    delinquent = va.get("delinquent") or []

    def stake(v):
        return (v.get("activatedStake") or 0) / LAMPORTS_PER_SOL

    active_stake = sum(stake(v) for v in current)
    delinquent_stake = sum(stake(v) for v in delinquent)
    total_stake = active_stake + delinquent_stake

    ranked = sorted(current, key=stake, reverse=True)

    nakamoto, running = 0, 0.0
    for v in ranked:
        running += stake(v)
        nakamoto += 1
        if total_stake and running >= total_stake / 3.0:
            break

    commissions = [v.get("commission") for v in current if v.get("commission") is not None]
    zero_commission = sum(1 for c in commissions if c == 0)

    return _ok(
        active_count=len(current),
        delinquent_count=len(delinquent),
        total_count=len(current) + len(delinquent),
        delinquent_pct=round(100.0 * len(delinquent) / (len(current) + len(delinquent)), 2)
        if (current or delinquent) else None,
        active_stake_sol=round(active_stake, 2),
        delinquent_stake_sol=round(delinquent_stake, 2),
        delinquent_stake_pct=round(100.0 * delinquent_stake / total_stake, 3) if total_stake else None,
        total_stake_sol=round(total_stake, 2),
        nakamoto_coefficient=nakamoto,
        top1_stake_pct=round(100.0 * stake(ranked[0]) / total_stake, 2) if ranked and total_stake else None,
        top10_stake_pct=round(100.0 * sum(stake(v) for v in ranked[:10]) / total_stake, 2)
        if ranked and total_stake else None,
        commission_mean=round(statistics.fmean(commissions), 2) if commissions else None,
        commission_median=statistics.median(commissions) if commissions else None,
        zero_commission_count=zero_commission,
        top_validators=[
            {
                "vote_pubkey": v.get("votePubkey"),
                "node_pubkey": v.get("nodePubkey"),
                "stake_sol": round(stake(v), 2),
                "stake_pct": round(100.0 * stake(v) / total_stake, 3) if total_stake else None,
                "commission": v.get("commission"),
                "last_vote": v.get("lastVote"),
            }
            for v in ranked[:top_n]
        ],
        delinquent_validators=[
            {
                "vote_pubkey": v.get("votePubkey"),
                "stake_sol": round(stake(v), 2),
                "last_vote": v.get("lastVote"),
            }
            for v in sorted(delinquent, key=stake, reverse=True)[:top_n]
        ],
    )


# --------------------------------------------------------------------------
# Off-chain: price, TVL, stablecoins, DEX volume
# --------------------------------------------------------------------------

def collect_market():
    """SOL price / market cap / volume from CoinGecko's keyless simple-price API."""
    url = (COINGECKO + "/simple/price?ids=solana&vs_currencies=usd"
           "&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true")
    try:
        data = get_json(url).get("solana", {})
    except FetchError as exc:
        return _fail(exc)
    return _ok(
        price_usd=data.get("usd"),
        market_cap_usd=data.get("usd_market_cap"),
        volume_24h_usd=data.get("usd_24h_vol"),
        change_24h_pct=round(data["usd_24h_change"], 2) if data.get("usd_24h_change") is not None else None,
    )


def collect_tvl(history_days=90):
    """Solana DeFi TVL now, plus the daily series for trend and anomaly checks."""
    try:
        series = get_json(LLAMA + "/v2/historicalChainTvl/Solana")
    except FetchError as exc:
        return _fail(exc)
    if not series:
        return _fail("empty TVL series")

    tail = series[-history_days:]
    current = tail[-1]["tvl"]

    def change(days):
        if len(tail) > days and tail[-1 - days]["tvl"]:
            return round(100.0 * (current - tail[-1 - days]["tvl"]) / tail[-1 - days]["tvl"], 2)
        return None

    return _ok(
        tvl_usd=round(current, 2),
        change_1d_pct=change(1),
        change_7d_pct=change(7),
        change_30d_pct=change(30),
        peak_90d_usd=round(max(p["tvl"] for p in tail), 2),
        series=[{"date": p["date"], "tvl": round(p["tvl"], 2)} for p in tail],
    )


def collect_stablecoins():
    """Stablecoin supply settled on Solana, by peg. The USD peg is the headline."""
    try:
        chains = get_json(LLAMA_STABLES + "/stablecoinchains")
    except FetchError as exc:
        return _fail(exc)
    row = next((c for c in chains if c.get("name") == "Solana"), None)
    if not row:
        return _fail("Solana not present in stablecoinchains")
    circ = row.get("totalCirculatingUSD") or {}
    return _ok(
        usd_pegged=round(circ.get("peggedUSD", 0), 2),
        all_pegs_usd=round(sum(v for v in circ.values() if isinstance(v, (int, float))), 2),
        by_peg={k: round(v, 2) for k, v in circ.items() if isinstance(v, (int, float)) and v > 1},
    )


def collect_dex_volume():
    """DEX volume on Solana — the cleanest public proxy for Real Economic Value."""
    url = (LLAMA + "/overview/dexs/solana?excludeTotalDataChart=true"
           "&excludeTotalDataChartBreakdown=true")
    try:
        data = get_json(url)
    except FetchError as exc:
        return _fail(exc)
    return _ok(
        volume_24h_usd=data.get("total24h"),
        volume_7d_usd=data.get("total7d"),
        volume_30d_usd=data.get("total30d"),
        change_1d_pct=data.get("change_1d"),
        change_7d_pct=data.get("change_7d"),
        protocol_count=len(data.get("protocols") or []),
        top_protocols=[
            {"name": p.get("name"), "volume_24h_usd": p.get("total24h")}
            for p in sorted(
                (data.get("protocols") or []),
                key=lambda p: p.get("total24h") or 0,
                reverse=True,
            )[:5]
        ],
    )


def collect_fees():
    """Chain fees and app revenue — the other half of the REV picture."""
    url = LLAMA + "/overview/fees/solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
    try:
        data = get_json(url)
    except FetchError as exc:
        return _fail(exc)
    return _ok(
        fees_24h_usd=data.get("total24h"),
        fees_7d_usd=data.get("total7d"),
        fees_30d_usd=data.get("total30d"),
        change_1d_pct=data.get("change_1d"),
    )


# --------------------------------------------------------------------------
# Protocol roadmap: SIMDs and validator client releases
# --------------------------------------------------------------------------

def collect_upgrades(simd_count=8, release_count=6):
    """What the protocol is about to change.

    The listing asks for upgrade tracking by name (Alpenglow, SIMD-525). There
    is no vendor "roadmap API", but the roadmap is not a secret either: every
    protocol change lands as a pull request against the Solana Improvement
    Documents repo, and every shipped change lands as a tagged release of the
    Agave validator client. Both are readable through the public GitHub API
    with no key, so this stays inside the no-API-keys constraint.

    Open SIMD PRs are what is *proposed*; recent Agave releases are what
    validators are actually being asked to run. Together they are the honest
    machine-readable answer to "what is coming", derived rather than
    hand-maintained -- so it keeps working after this report is handed over.
    """
    out = {}
    try:
        prs = get_json(
            GITHUB + "/repos/solana-foundation/solana-improvement-documents/pulls"
            "?state=open&sort=updated&direction=desc&per_page=%d" % simd_count)
        simds = []
        for pr in prs:
            title = (pr.get("title") or "").strip()
            simds.append({
                "number": pr.get("number"),
                "title": title,
                "simd": _simd_number(title, pr.get("head") or {}),
                "url": pr.get("html_url"),
                "updated_at": pr.get("updated_at"),
                "draft": bool(pr.get("draft")),
            })
        out["simds"] = simds
    except FetchError as exc:
        return _fail(exc)

    try:
        rels = get_json(GITHUB + "/repos/anza-xyz/agave/releases?per_page=%d" % release_count)
        out["releases"] = [{
            "tag": r.get("tag_name"),
            "name": (r.get("name") or "").strip(),
            "published_at": r.get("published_at"),
            "prerelease": bool(r.get("prerelease")),
            "url": r.get("html_url"),
        } for r in rels]
    except FetchError as exc:
        out["releases"] = []
        out["releases_error"] = str(exc)

    return _ok(**out)


def _simd_number(title, head):
    """Pull the SIMD number out of a PR title or branch name when it has one.
    Titles are not standardised, so this is best-effort and returns None rather
    than guessing."""
    for text in (title, head.get("ref") or ""):
        m = re.search(r"(?:simd[-_ ]?|^)(\d{3,4})\b", text, re.I)
        if m:
            return int(m.group(1))
    return None
