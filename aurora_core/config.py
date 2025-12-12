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
