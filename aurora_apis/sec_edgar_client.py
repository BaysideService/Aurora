from __future__ import annotations

import os
from typing import Any, Dict

from aurora_apis.http_client import http_get


class SECEdgarClient:
    """
    Minimal SEC EDGAR client using the official SEC API.

    You must set SEC_EDGAR_USER_AGENT to a descriptive user agent string,
    e.g., "AuroraQuant/0.1 (contact@example.com)".
    """

    SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
    COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"

    def __init__(self, user_agent: str | None = None) -> None:
        self.user_agent = user_agent or os.getenv("SEC_EDGAR_USER_AGENT")

    def _headers(self) -> Dict[str, str]:
        if not self.user_agent:
            raise RuntimeError("SEC_EDGAR_USER_AGENT is not set")
        return {"User-Agent": self.user_agent}

    def _ticker_cik_map(self) -> Dict[str, int]:
        """
        Lazily fetch and cache SEC's public ticker->CIK mapping.
        """
        if not hasattr(self, "_cached_ticker_cik_map"):
            data = http_get(self.COMPANY_TICKERS_URL, headers=self._headers())
            self._cached_ticker_cik_map = {
                entry["ticker"].upper(): int(entry["cik_str"])
                for entry in data.values()
            }
        return self._cached_ticker_cik_map

    def resolve_cik(self, cik_or_symbol: str | int) -> int:
        """
        Convert a symbol or already-numeric CIK into a numeric CIK.
        """
        try:
            return int(cik_or_symbol)
        except ValueError:
            symbol = str(cik_or_symbol).upper()
            ticker_map = self._ticker_cik_map()
            if symbol not in ticker_map:
                raise ValueError(
                    f"No CIK found for symbol '{cik_or_symbol}'"
                ) from None
            return ticker_map[symbol]

    def get_company_facts(self, cik_or_symbol: str | int) -> Dict[str, Any]:
        """
        Fetch basic company facts using a ticker symbol or numeric CIK.
        """
        cik = self.resolve_cik(cik_or_symbol)

        url = self.COMPANY_FACTS_URL.format(cik=cik)
        return http_get(url, headers=self._headers())
