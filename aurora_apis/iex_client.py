from __future__ import annotations

import os
from typing import Any, Dict

from aurora_apis.http_client import http_get


class IEXClient:
    """
    Minimal IEX Cloud client.

    Uses the `stock/{symbol}/quote` endpoint as a basic example.
    """

    BASE_URL = "https://cloud.iexapis.com/stable"

    def __init__(self, api_token: str | None = None) -> None:
        self.api_token = api_token or os.getenv("IEX_API_TOKEN")

    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_token:
            raise RuntimeError("IEX_API_TOKEN is not set")

        params = dict(params)
        params["token"] = self.api_token
        url = f"{self.BASE_URL}{path}"
        return http_get(url, params=params)

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        return self._get(f"/stock/{symbol}/quote", {})
