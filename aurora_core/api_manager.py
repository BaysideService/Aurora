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
