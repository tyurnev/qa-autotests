import pytest
import requests
from tests.helpers.api_contracts import assert_post_contract


@pytest.mark.parametrize("index", [0, 1, 2, 9])
def test_get_posts_list_has_valid_items(api_base_url: str, http_timeout_seconds: int, index: int):
    url = f"{api_base_url}/posts"
    r = requests.get(url, timeout=http_timeout_seconds)

    assert r.status_code == 200
    data = r.json()

    assert isinstance(data, list)
    assert len(data) > index

    assert_post_contract(data[index])
