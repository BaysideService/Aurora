from __future__ import annotations

import os
from typing import Any, Dict, List

import requests


class BenzingaClient:
    """
    Minimal Benzinga news client.

    Expects BENZINGA_API_KEY to be present in the environment.
    """

    BASE_URL = "https://api.benzinga.com/api/v2"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("BENZINGA_API_KEY")

    def get_news(self, symbol: str, limit: int = 10) -> List[Dict[str, Any]]:
        if not self.api_key:
            raise RuntimeError("BENZINGA_API_KEY is not set")

        params = {
            "token": self.api_key,
            "tickers": symbol,
            "channels": "stocks",
            "pageSize": limit,
        }
        url = f"{self.BASE_URL}/news"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
