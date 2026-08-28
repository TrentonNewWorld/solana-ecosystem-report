"""Minimal HTTP/JSON-RPC layer built on the standard library only.

Deliberately no `requests`: the bounty prefers a solution that runs on a bare
Python install with no API keys and no third-party packages. Everything here is
`urllib.request` plus retry/backoff so a flaky public endpoint degrades to a
missing metric instead of a crashed report.
"""

import gzip
import json
import time
import urllib.error
import urllib.request

USER_AGENT = "solreport/1.0 (+https://github.com/) stdlib-only"
DEFAULT_TIMEOUT = 25


class FetchError(Exception):
    """Raised when a source could not be reached after all retries."""


def _open(req, timeout):
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        return raw.decode("utf-8", errors="replace")


def get_json(url, timeout=DEFAULT_TIMEOUT, retries=3, backoff=1.5):
    """GET a URL and parse JSON. Retries transient failures, then raises."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    last = None
    for attempt in range(retries):
        try:
            return json.loads(_open(req, timeout))
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError) as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(backoff ** attempt)
    raise FetchError("GET %s failed: %s" % (url, last))


def post_json(url, payload, timeout=DEFAULT_TIMEOUT, retries=3, backoff=1.5):
    """POST a JSON body and parse the JSON response."""
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    last = None
    for attempt in range(retries):
        try:
            return json.loads(_open(req, timeout))
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError) as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(backoff ** attempt)
    raise FetchError("POST %s failed: %s" % (url, last))


class RpcClient:
    """Solana JSON-RPC client. Supports batching so one round trip covers many
    cheap methods, which matters on a rate-limited public endpoint."""

    def __init__(self, endpoint, timeout=DEFAULT_TIMEOUT):
        self.endpoint = endpoint
        self.timeout = timeout

    def call(self, method, params=None):
        payload = {"jsonrpc": "2.0", "id": 1, "method": method}
        if params is not None:
            payload["params"] = params
        res = post_json(self.endpoint, payload, timeout=self.timeout)
        if "error" in res:
            raise FetchError("rpc %s: %s" % (method, res["error"]))
        return res.get("result")

    def batch(self, calls):
        """calls: list of (method, params_or_None). Returns list aligned to input,
        with None where that single call errored."""
        payload = []
        for idx, (method, params) in enumerate(calls):
            item = {"jsonrpc": "2.0", "id": idx, "method": method}
            if params is not None:
                item["params"] = params
            payload.append(item)
        res = post_json(self.endpoint, payload, timeout=self.timeout)
        out = [None] * len(calls)
        if not isinstance(res, list):
            return out
        for item in res:
            idx = item.get("id")
            if isinstance(idx, int) and 0 <= idx < len(out) and "result" in item:
                out[idx] = item["result"]
        return out
