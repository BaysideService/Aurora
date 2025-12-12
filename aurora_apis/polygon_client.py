from __future__ import annotations

import os
from typing import Any, Dict

import requests


class PolygonClient:
    """
    Minimal Polygon client for last trade / quote.
    """

    BASE_URL = "https://api.polygon.io"

    def __init__(
        self,
        api_key: str | None = None,
        access_key_id: str | None = None,
        secret_access_key: str | None = None,
    ) -> None:
        self.api_key = api_key or os.getenv("POLYGON_API_KEY")
        self.access_key_id = access_key_id or os.getenv("POLYGON_ACCESS_KEY_ID")
        self.secret_access_key = (
            secret_access_key or os.getenv("POLYGON_SECRET_ACCESS_KEY")
        )

    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("POLYGON_API_KEY is not set")

        params = dict(params)
        params["apiKey"] = self.api_key
        url = f"{self.BASE_URL}{path}"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_last_trade(self, symbol: str) -> Dict[str, Any]:
        return self._get(f"/v2/last/trade/{symbol}", {})
