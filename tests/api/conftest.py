import pytest
import requests
from app.api_client import ApiClient
from tests.helpers.data_factory import (
    build_patch_payload,
    build_post_payload,
    build_put_post_payload,
)


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

@pytest.fixture(scope="function")
def generated_post_payload() -> dict[str, int | str]:
    return build_post_payload()


@pytest.fixture(scope="function")
def generated_put_post_payload() -> dict[str, int | str]:
    return build_put_post_payload()


@pytest.fixture(scope="function")
def generated_patch_payload() -> dict[str, str]:
    return build_patch_payload()