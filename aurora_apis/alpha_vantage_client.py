from __future__ import annotations

import os
from typing import Any, Dict

from aurora_apis.http_client import http_get


class AlphaVantageClient:
    """
    Minimal Alpha Vantage client.

    Uses the GLOBAL_QUOTE endpoint for live pricing.
    """

    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY")

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("ALPHA_VANTAGE_API_KEY is not set")

        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key,
        }
        data = http_get(self.BASE_URL, params=params)
        return data.get("Global Quote", data)
