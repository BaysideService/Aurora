from __future__ import annotations

import os
from typing import Any, Dict

import requests


class FinnhubClient:
    """
    Minimal Finnhub client for quote + sentiment.
    """

    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        proxy_url: str | None = None,
    ) -> None:
        self.api_key = api_key or os.getenv("FINNHUB_API_KEY")
        self.api_secret = api_secret or os.getenv("FINNHUB_SECRET")
        self.proxy_url = proxy_url or os.getenv("FINNHUB_PROXY_URL")

    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("FINNHUB_API_KEY is not set")

        params = dict(params)
        params["token"] = self.api_key
        url = f"{self.BASE_URL}{path}"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        return self._get("/quote", {"symbol": symbol})
