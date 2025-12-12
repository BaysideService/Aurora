from __future__ import annotations

import os
from typing import Any, Dict

from aurora_apis.http_client import http_get


class StockTwitsClient:
    """
    Minimal StockTwits client for symbol streams.

    If STOCKTWITS_ACCESS_TOKEN is set, it will be appended as an `access_token`
    parameter, but public endpoints can function without it.
    """

    BASE_URL = "https://api.stocktwits.com/api/2"

    def __init__(self, access_token: str | None = None) -> None:
        self.access_token = access_token or os.getenv("STOCKTWITS_ACCESS_TOKEN")

    def get_symbol_stream(self, symbol: str) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if self.access_token:
            params["access_token"] = self.access_token

        url = f"{self.BASE_URL}/streams/symbol/{symbol}.json"
        return http_get(url, params=params)
