import requests
from tests.helpers.api_contracts import assert_post_contract
from app.api_client import ApiClient



def test_get_post_1_returns_200_and_json(api_client: ApiClient):
    status, data = api_client.get_json("/posts/1")
    assert status == 200
    assert isinstance(data, dict)
    assert data.get("id") == 1

def test_wrong_endpoint_returns_404(api_base_url: str, http_timeout_seconds: int):
    url = f"{api_base_url}/post"  # намеренно неверный endpoint
    r = requests.get(url, timeout=http_timeout_seconds)

    assert r.status_code == 404