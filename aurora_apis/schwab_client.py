from __future__ import annotations

import os
from typing import Any, Dict


class SchwabClient:
    """
    Placeholder for Schwab brokerage integration.

    This class does not perform HTTP requests directly because access
    is controlled and must be wired to the official Schwab Trader API
    client in your environment.

    For now, it simply stores the credentials and exposes a clean
    interface boundary for future expansion.
    """

    def __init__(
        self,
        api_key: str | None = None,
        app_secret: str | None = None,
    ) -> None:
        self.api_key = api_key or os.getenv("SCHWAB_API_KEY")
        self.app_secret = app_secret or os.getenv("SCHWAB_APP_SECRET")

    def is_configured(self) -> bool:
        return bool(self.api_key and self.app_secret)

    def summary(self) -> Dict[str, Any]:
        return {
            "configured": self.is_configured(),
            "has_api_key": bool(self.api_key),
            "has_app_secret": bool(self.app_secret),
        }
