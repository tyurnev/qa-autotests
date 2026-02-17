import pytest
import requests
from app.api_client import ApiClient


@pytest.fixture(scope="session")
def api_base_url() -> str:
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def http_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    return session

@pytest.fixture(scope="session")
def http_timeout_seconds() -> int:
    return 10

@pytest.fixture(scope="session")
def api_client(api_base_url: str, http_timeout_seconds: int) -> ApiClient:
    return ApiClient(base_url=api_base_url, timeout_seconds=http_timeout_seconds)