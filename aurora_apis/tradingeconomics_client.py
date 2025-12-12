from __future__ import annotations

import os
from typing import Any, Dict, List

from aurora_apis.http_client import http_get


class TradingEconomicsClient:
    """
    Minimal TradingEconomics client using the free tier.

    Requires:
    - TRADINGECONOMICS_CLIENT_KEY
    - TRADINGECONOMICS_CLIENT_SECRET
    """

    BASE_URL = "https://api.tradingeconomics.com"

    def __init__(
        self,
        client_key: str | None = None,
        client_secret: str | None = None,
    ) -> None:
        self.client_key = client_key or os.getenv("TRADINGECONOMICS_CLIENT_KEY")
        self.client_secret = (
            client_secret or os.getenv("TRADINGECONOMICS_CLIENT_SECRET")
        )

    def _auth_params(self) -> Dict[str, str]:
        if not (self.client_key and self.client_secret):
            raise RuntimeError("TradingEconomics credentials are not set")
        return {"client": f"{self.client_key}:{self.client_secret}"}

    def get_calendar(self, country: str | None = None) -> List[Dict[str, Any]]:
        params: Dict[str, Any] = self._auth_params()
        if country:
            params["country"] = country
        url = f"{self.BASE_URL}/calendar"
        return http_get(url, params=params)
