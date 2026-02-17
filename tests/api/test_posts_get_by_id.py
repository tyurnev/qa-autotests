import pytest
import requests
from tests.helpers.api_contracts import assert_post_contract


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post_by_id_returns_200_and_valid_schema(api_base_url: str, http_timeout_seconds: int, post_id: int):
    url = f"{api_base_url}/posts/{post_id}"
    r = requests.get(url, timeout=http_timeout_seconds)

    assert r.status_code == 200
    assert "application/json" in r.headers.get("Content-Type", "")

    data = r.json()
    assert_post_contract(data)
    assert data["id"] == post_id
