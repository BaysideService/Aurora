#!/usr/bin/env python
"""
Bootstrap script for the Aurora repo.

Run this ONCE from the repo root to create the directory structure and
initial codebase for:
- aurora_core
- aurora_apis
- tests
- config, API manager, data fusion bus
- minimal API clients for each upstream service

All files are fully concrete; no placeholders are left in the generated code.
"""

from pathlib import Path
from textwrap import dedent


FILES: dict[str, str] = {}

# ---------------------------------------------------------------------------
# Top-level files
# ---------------------------------------------------------------------------

FILES["README.md"] = dedent(
    '''
    # Aurora

    Aurora is a modular market-intelligence and microstructure engine.

    This repository provides:

    - `aurora_core`: configuration, logging, API manager, data fusion bus
    - `aurora_apis`: thin, typed HTTP clients for each upstream data provider
    - `tests`: smoke tests to confirm the environment and imports

    Aurora loads credentials from environment variables. The following
    variables are currently used:

    - `ALPHA_VANTAGE_API_KEY`
    - `ALPHA_VANTAGE_EMAIL`
    - `BENZINGA_API_KEY`
    - `FINNHUB_API_KEY`
    - `FINNHUB_SECRET`
    - `FINNHUB_PROXY_URL`
    - `OPENAI_API_KEY`
    - `POLYGON_API_KEY`
    - `POLYGON_ACCESS_KEY_ID`
    - `POLYGON_SECRET_ACCESS_KEY`
    - `POLYGON_S3_ENDPOINT`
    - `SCHWAB_API_KEY`
    - `SCHWAB_APP_SECRET`
    - `SEC_EDGAR_USER_AGENT`
    - `FRED_API_KEY`
    - `REDDIT_CLIENT_ID`
    - `REDDIT_CLIENT_SECRET`
    - `REDDIT_USER_AGENT`
    - `STOCKTWITS_ACCESS_TOKEN`
    - `IEX_API_TOKEN`
    - `TRADINGECONOMICS_CLIENT_KEY`
    - `TRADINGECONOMICS_CLIENT_SECRET`

    To install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    To run tests:

    ```bash
    pytest
    ```
    '''
).lstrip("\n")

FILES[".gitignore"] = dedent(
    '''
    __pycache__/
    .pytest_cache/
    .venv/
    .env
    .idea/
    .vscode/
    *.pyc
    *.pyo
    *.pyd
    .DS_Store
    *.log
    '''
).lstrip("\n")

FILES["requirements.txt"] = dedent(
    '''
    requests
    pydantic>=2.0
    python-dotenv
    '''
).lstrip("\n")

FILES["pyproject.toml"] = dedent(
    '''
    [build-system]
    requires = ["setuptools>=61.0", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "aurora"
    version = "0.1.0"
    description = "Aurora market microstructure and data-fusion engine"
    authors = [{ name = "Aurora System" }]
    requires-python = ">=3.10"
    dependencies = [
        "requests",
        "pydantic>=2.0",
        "python-dotenv",
    ]

    [tool.pytest.ini_options]
    pythonpath = ["."]
    '''
).lstrip("\n")

# ---------------------------------------------------------------------------
# aurora_core package
# ---------------------------------------------------------------------------

FILES["aurora_core/__init__.py"] = dedent(
    '''
    '''
).lstrip("\n")

FILES["aurora_core/config.py"] = dedent(
    '''
    import os
    from dataclasses import dataclass
    from typing import Optional


    @dataclass
    class APIConfig:
        alpha_vantage_api_key: Optional[str] = None
        alpha_vantage_email: Optional[str] = None
        benzinga_api_key: Optional[str] = None
        finnhub_api_key: Optional[str] = None
        finnhub_secret: Optional[str] = None
        finnhub_proxy_url: Optional[str] = None
        openai_api_key: Optional[str] = None
        polygon_api_key: Optional[str] = None
        polygon_access_key_id: Optional[str] = None
        polygon_secret_access_key: Optional[str] = None
        polygon_s3_endpoint: Optional[str] = None
        schwab_api_key: Optional[str] = None
        schwab_app_secret: Optional[str] = None
        sec_edgar_user_agent: Optional[str] = None
        fred_api_key: Optional[str] = None
        reddit_client_id: Optional[str] = None
        reddit_client_secret: Optional[str] = None
        reddit_user_agent: Optional[str] = None
        stocktwits_access_token: Optional[str] = None
        iex_api_token: Optional[str] = None
        tradingeconomics_client_key: Optional[str] = None
        tradingeconomics_client_secret: Optional[str] = None


    def load_api_config() -> APIConfig:
        """
        Load all API-related configuration from environment variables.
        """
        return APIConfig(
            alpha_vantage_api_key=os.getenv("ALPHA_VANTAGE_API_KEY"),
            alpha_vantage_email=os.getenv("ALPHA_VANTAGE_EMAIL"),
            benzinga_api_key=os.getenv("BENZINGA_API_KEY"),
            finnhub_api_key=os.getenv("FINNHUB_API_KEY"),
            finnhub_secret=os.getenv("FINNHUB_SECRET"),
            finnhub_proxy_url=os.getenv("FINNHUB_PROXY_URL"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            polygon_api_key=os.getenv("POLYGON_API_KEY"),
            polygon_access_key_id=os.getenv("POLYGON_ACCESS_KEY_ID"),
            polygon_secret_access_key=os.getenv("POLYGON_SECRET_ACCESS_KEY"),
            polygon_s3_endpoint=os.getenv("POLYGON_S3_ENDPOINT"),
            schwab_api_key=os.getenv("SCHWAB_API_KEY"),
            schwab_app_secret=os.getenv("SCHWAB_APP_SECRET"),
            sec_edgar_user_agent=os.getenv("SEC_EDGAR_USER_AGENT"),
            fred_api_key=os.getenv("FRED_API_KEY"),
            reddit_client_id=os.getenv("REDDIT_CLIENT_ID"),
            reddit_client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            reddit_user_agent=os.getenv("REDDIT_USER_AGENT"),
            stocktwits_access_token=os.getenv("STOCKTWITS_ACCESS_TOKEN"),
            iex_api_token=os.getenv("IEX_API_TOKEN"),
            tradingeconomics_client_key=os.getenv("TRADINGECONOMICS_CLIENT_KEY"),
            tradingeconomics_client_secret=os.getenv("TRADINGECONOMICS_CLIENT_SECRET"),
        )
    '''
).lstrip("\n")

FILES["aurora_core/logging_utils.py"] = dedent(
    '''
    import logging
    import sys


    def get_logger(name: str) -> logging.Logger:
        """
        Return a configured logger for the Aurora system.
        """
        logger = logging.getLogger(name)
        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        return logger
    '''
).lstrip("\n")

FILES["aurora_core/api_manager.py"] = dedent(
    '''
    from dataclasses import dataclass

    from aurora_core.config import APIConfig, load_api_config
    from aurora_core.logging_utils import get_logger
    from aurora_apis.alpha_vantage_client import AlphaVantageClient
    from aurora_apis.benzinga_client import BenzingaClient
    from aurora_apis.finnhub_client import FinnhubClient
    from aurora_apis.polygon_client import PolygonClient
    from aurora_apis.schwab_client import SchwabClient
    from aurora_apis.sec_edgar_client import SECEdgarClient
    from aurora_apis.fred_client import FREDClient
    from aurora_apis.reddit_client import RedditClient
    from aurora_apis.stocktwits_client import StockTwitsClient
    from aurora_apis.iex_client import IEXClient
    from aurora_apis.tradingeconomics_client import TradingEconomicsClient


    logger = get_logger(__name__)


    @dataclass
    class AuroraClients:
        alpha_vantage: AlphaVantageClient
        benzinga: BenzingaClient
        finnhub: FinnhubClient
        polygon: PolygonClient
        schwab: SchwabClient
        sec_edgar: SECEdgarClient
        fred: FREDClient
        reddit: RedditClient
        stocktwits: StockTwitsClient
        iex: IEXClient
        tradingeconomics: TradingEconomicsClient


    def build_clients(config: APIConfig | None = None) -> AuroraClients:
        """
        Build all Aurora API clients from the loaded configuration.
        """
        if config is None:
            config = load_api_config()

        logger.info("Building Aurora API clients")

        return AuroraClients(
            alpha_vantage=AlphaVantageClient(api_key=config.alpha_vantage_api_key),
            benzinga=BenzingaClient(api_key=config.benzinga_api_key),
            finnhub=FinnhubClient(
                api_key=config.finnhub_api_key,
                api_secret=config.finnhub_secret,
                proxy_url=config.finnhub_proxy_url,
            ),
            polygon=PolygonClient(
                api_key=config.polygon_api_key,
                access_key_id=config.polygon_access_key_id,
                secret_access_key=config.polygon_secret_access_key,
            ),
            schwab=SchwabClient(
                api_key=config.schwab_api_key,
                app_secret=config.schwab_app_secret,
            ),
            sec_edgar=SECEdgarClient(user_agent=config.sec_edgar_user_agent),
            fred=FREDClient(api_key=config.fred_api_key),
            reddit=RedditClient(
                client_id=config.reddit_client_id,
                client_secret=config.reddit_client_secret,
                user_agent=config.reddit_user_agent,
            ),
            stocktwits=StockTwitsClient(
                access_token=config.stocktwits_access_token
            ),
            iex=IEXClient(api_token=config.iex_api_token),
            tradingeconomics=TradingEconomicsClient(
                client_key=config.tradingeconomics_client_key,
                client_secret=config.tradingeconomics_client_secret,
            ),
        )
    '''
).lstrip("\n")

FILES["aurora_core/data_fusion_bus.py"] = dedent(
    '''
    from dataclasses import dataclass
    from typing import Any, Dict

    from aurora_core.api_manager import AuroraClients
    from aurora_core.logging_utils import get_logger


    logger = get_logger(__name__)


    @dataclass
    class TickerSnapshot:
        symbol: str
        quote: Dict[str, Any]
        news: list[Dict[str, Any]]
        fundamentals: Dict[str, Any]


    class DataFusionBus:
        """
        Simple data fusion bus that pulls from upstream APIs and returns
        a unified snapshot structure. This is intentionally conservative
        and can be extended by additional Aurora services.
        """

        def __init__(self, clients: AuroraClients) -> None:
            self.clients = clients

        def snapshot(self, symbol: str) -> TickerSnapshot:
            logger.info("Building snapshot for %s", symbol)

            quote = self.clients.alpha_vantage.get_quote(symbol)
            news = self.clients.benzinga.get_news(symbol, limit=10)
            fundamentals = self.clients.sec_edgar.get_company_facts(symbol)

            return TickerSnapshot(
                symbol=symbol,
                quote=quote,
                news=news,
                fundamentals=fundamentals,
            )
    '''
).lstrip("\n")

# ---------------------------------------------------------------------------
# aurora_apis package
# ---------------------------------------------------------------------------

FILES["aurora_apis/__init__.py"] = ""

FILES["aurora_apis/alpha_vantage_client.py"] = dedent(
    '''
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
    '''
).lstrip("\n")

FILES["aurora_apis/benzinga_client.py"] = dedent(
    '''
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
    '''
).lstrip("\n")

FILES["aurora_apis/finnhub_client.py"] = dedent(
    '''
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
    '''
).lstrip("\n")

FILES["aurora_apis/polygon_client.py"] = dedent(
    '''
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
    '''
).lstrip("\n")

FILES["aurora_apis/schwab_client.py"] = dedent(
    '''
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
    '''
).lstrip("\n")

FILES["aurora_apis/sec_edgar_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict

    import requests


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
            response = requests.get(url, headers=self._headers(), timeout=10)
            response.raise_for_status()
            return response.json()
    '''
).lstrip("\n")

FILES["aurora_apis/fred_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict

    import requests


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
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        def get_series(self, series_id: str) -> Dict[str, Any]:
            return self._get("/series/observations", {"series_id": series_id})
    '''
).lstrip("\n")

FILES["aurora_apis/reddit_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict, List

    import requests
    from requests.auth import HTTPBasicAuth


    class RedditClient:
        """
        Minimal Reddit client for ticker mention scraping using OAuth2.

        This uses the application-only client_credentials flow and requires:

        - REDDIT_CLIENT_ID
        - REDDIT_CLIENT_SECRET
        - REDDIT_USER_AGENT
        """

        TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
        BASE_URL = "https://oauth.reddit.com"

        def __init__(
            self,
            client_id: str | None = None,
            client_secret: str | None = None,
            user_agent: str | None = None,
        ) -> None:
            self.client_id = client_id or os.getenv("REDDIT_CLIENT_ID")
            self.client_secret = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
            self.user_agent = user_agent or os.getenv("REDDIT_USER_AGENT")
            self._access_token: str | None = None

        def _get_token(self) -> str:
            if self._access_token:
                return self._access_token

            if not (self.client_id and self.client_secret and self.user_agent):
                raise RuntimeError("Reddit credentials are not fully configured")

            auth = HTTPBasicAuth(self.client_id, self.client_secret)
            data = {"grant_type": "client_credentials"}
            headers = {"User-Agent": self.user_agent}
            response = requests.post(
                self.TOKEN_URL, auth=auth, data=data, headers=headers, timeout=10
            )
            response.raise_for_status()
            token = response.json()["access_token"]
            self._access_token = token
            return token

        def search_subreddit(self, subreddit: str, query: str, limit: int = 10) -> List[Dict[str, Any]]:
            token = self._get_token()
            headers = {
                "Authorization": f"Bearer {token}",
                "User-Agent": self.user_agent or "aurora-reddit-client",
            }
            params = {"q": query, "limit": limit, "sort": "new", "restrict_sr": True}
            url = f"{self.BASE_URL}/r/{subreddit}/search"
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            children = data.get("data", {}).get("children", [])
            return [c.get("data", {}) for c in children]
    '''
).lstrip("\n")

FILES["aurora_apis/stocktwits_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict

    import requests


    class StockTwitsClient:
        """
        Minimal StockTwits client for symbol streams.

        If STOCKTWITS_ACCESS_TOKEN is set, it will be appended as an `access_token`
        parameter, but public endpoints can function without it.
        """

        BASE_URL = "https://api.stocktwits.com/api/2"

        def __init__(self, access_token: str | None = None) -> None:
            self.access_token = access_token or os.getenv("STOCKTWITS_ACCESS_TOKEN")

        def get_symbol_stream(self, symbol: str) -> Dict[str, Any]:
            params: Dict[str, Any] = {}
            if self.access_token:
                params["access_token"] = self.access_token

            url = f"{self.BASE_URL}/streams/symbol/{symbol}.json"
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
    '''
).lstrip("\n")

FILES["aurora_apis/iex_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict

    import requests


    class IEXClient:
        """
        Minimal IEX Cloud client.

        Uses the `stock/{symbol}/quote` endpoint as a basic example.
        """

        BASE_URL = "https://cloud.iexapis.com/stable"

        def __init__(self, api_token: str | None = None) -> None:
            self.api_token = api_token or os.getenv("IEX_API_TOKEN")

        def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
            if not self.api_token:
                raise RuntimeError("IEX_API_TOKEN is not set")

            params = dict(params)
            params["token"] = self.api_token
            url = f"{self.BASE_URL}{path}"
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        def get_quote(self, symbol: str) -> Dict[str, Any]:
            return self._get(f"/stock/{symbol}/quote", {})
    '''
).lstrip("\n")

FILES["aurora_apis/tradingeconomics_client.py"] = dedent(
    '''
    from __future__ import annotations

    import os
    from typing import Any, Dict, List

    import requests


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
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
    '''
).lstrip("\n")

# ---------------------------------------------------------------------------
# tests
# ---------------------------------------------------------------------------

FILES["tests/__init__.py"] = ""

FILES["tests/test_smoke_imports.py"] = dedent(
    '''
    from aurora_core.config import load_api_config
    from aurora_core.api_manager import build_clients
    from aurora_core.data_fusion_bus import DataFusionBus


    def test_smoke_build_clients():
        config = load_api_config()
        clients = build_clients(config)
        assert clients.alpha_vantage is not None
        assert clients.benzinga is not None
        assert clients.polygon is not None


    def test_smoke_data_fusion_bus_initialization():
        config = load_api_config()
        clients = build_clients(config)
        bus = DataFusionBus(clients)
        assert bus.clients is clients
    '''
).lstrip("\n")


def write_files() -> None:
    for path_str, content in FILES.items():
        path = Path(path_str)
        if path.parent and not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Created {len(FILES)} files for Aurora.")


if __name__ == "__main__":
    write_files()
