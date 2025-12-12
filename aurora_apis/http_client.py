from __future__ import annotations

import base64
import json
from typing import Any, Dict, Mapping, MutableMapping, Tuple
from urllib import parse, request


def _build_url(url: str, params: Mapping[str, Any] | None) -> str:
    if not params:
        return url
    query = parse.urlencode({k: v for k, v in params.items() if v is not None})
    return f"{url}?{query}" if query else url


def http_get(
    url: str,
    params: Mapping[str, Any] | None = None,
    headers: Mapping[str, str] | None = None,
    timeout: float = 10,
) -> Dict[str, Any]:
    full_url = _build_url(url, params)
    req = request.Request(full_url, headers=dict(headers or {}))
    with request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.load(resp)


def http_post(
    url: str,
    data: Mapping[str, Any] | None = None,
    headers: MutableMapping[str, str] | None = None,
    auth_basic: Tuple[str, str] | None = None,
    timeout: float = 10,
) -> Dict[str, Any]:
    body = parse.urlencode(data or {}).encode()
    req_headers: Dict[str, str] = dict(headers or {})

    if auth_basic:
        user, password = auth_basic
        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        req_headers["Authorization"] = f"Basic {token}"

    req = request.Request(url, data=body, headers=req_headers)
    with request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.load(resp)
