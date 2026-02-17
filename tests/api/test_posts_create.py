from app.api_client import ApiClient

def test_create_post_returns_201_and_echoes_payload(api_client: ApiClient):
    payload = {"title": "foo", "body": "bar", "userId": 1}

    status, data = api_client.post_json("/posts", payload)

    assert status == 201
    assert isinstance(data, dict)

    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
