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
