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

    def __init__(self, user_agent: str | None = None) -> None:
        self.user_agent = user_agent or os.getenv("SEC_EDGAR_USER_AGENT")

    def _headers(self) -> Dict[str, str]:
        if not self.user_agent:
            raise RuntimeError("SEC_EDGAR_USER_AGENT is not set")
        return {"User-Agent": self.user_agent}

    def get_company_facts(self, cik_or_symbol: str | int) -> Dict[str, Any]:
        """
        Fetch basic company facts using a numeric CIK. If a symbol string is
        passed, it is assumed to already be a CIK or pre-mapped upstream.
        """
        try:
            cik = int(cik_or_symbol)
        except ValueError:
            # In a more complete system you'd symbol->CIK map here.
            raise ValueError("get_company_facts currently expects a numeric CIK")

        url = self.COMPANY_FACTS_URL.format(cik=cik)
        return http_get(url, headers=self._headers())
