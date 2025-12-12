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
        try:
            fundamentals = self.clients.sec_edgar.get_company_facts(symbol)
        except ValueError:
            logger.warning(
                "SEC EDGAR fundamentals require a CIK; skipping fundamentals for %s",
                symbol,
            )
            fundamentals = {}

        return TickerSnapshot(
            symbol=symbol,
            quote=quote,
            news=news,
            fundamentals=fundamentals,
        )
