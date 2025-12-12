import pytest

# The test environment may not have external dependencies installed (e.g.,
# requests cannot be fetched behind strict proxies). If the HTTP client
# dependency is unavailable, skip these smoke tests rather than hard-failing
# the suite.
pytest.importorskip("requests", reason="requests dependency is required for API clients")

from aurora_core.api_manager import build_clients
from aurora_core.config import load_api_config
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
