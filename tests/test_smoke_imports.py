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
