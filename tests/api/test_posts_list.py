import requests
from tests.helpers.api_contracts import assert_post_contract


def test_get_posts_returns_list_of_posts(api_base_url: str, http_timeout_seconds: int):
    url = f"{api_base_url}/posts"
    r = requests.get(url, timeout=http_timeout_seconds)

    assert r.status_code == 200
    assert "application/json" in r.headers.get("Content-Type", "")

    data = r.json()
    assert len(data) > 0
    for post in data:
        assert_post_contract(post)
