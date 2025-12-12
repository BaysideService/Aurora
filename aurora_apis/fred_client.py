from __future__ import annotations

import os
from typing import Any, Dict

from aurora_apis.http_client import http_get


class FREDClient:
    """
    Minimal FRED client for macroeconomic series.
    """

    BASE_URL = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("FRED_API_KEY")

    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("FRED_API_KEY is not set")

        params = dict(params)
        params["api_key"] = self.api_key
        params["file_type"] = "json"
        url = f"{self.BASE_URL}{path}"
        return http_get(url, params=params)

    def get_series(self, series_id: str) -> Dict[str, Any]:
        return self._get("/series/observations", {"series_id": series_id})
