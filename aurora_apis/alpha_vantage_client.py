from __future__ import annotations

import os
from typing import Any, Dict

import requests


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
        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("Global Quote", data)
