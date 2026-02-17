import pytest
import requests


@pytest.mark.parametrize("path", ["/post", "/postsx", "/userss", "/unknown"])
def test_wrong_endpoints_return_404(api_base_url: str, http_timeout_seconds: int, path: str):
    url = f"{api_base_url}{path}"
    r = requests.get(url, timeout=http_timeout_seconds)

    assert r.status_code == 404
