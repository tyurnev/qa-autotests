from app.api_client import ApiClient

def test_put_post_returns_200_and_echoes_payload(api_client: ApiClient):
    payload = {"id": 1, "title": "new title", "body": "new body", "userId": 1}
    status, data = api_client.put_json("/posts/1", payload)

    assert status == 200
    assert isinstance(data, dict)
    assert data.get("id") == 1
    assert data.get("title") == payload["title"]
    assert data.get("body") == payload["body"]
    assert data.get("userId") == payload["userId"]

def test_patch_post_returns_200_and_updates_field(api_client: ApiClient):
    payload = {"title": "patched title"}
    status, data = api_client.patch_json("/posts/1", payload)

    assert status == 200
    assert isinstance(data, dict)
    assert data.get("id") == 1
    assert data.get("title") == payload["title"]

def test_delete_post_returns_success_status(api_client: ApiClient):
    status = api_client.delete("/posts/1")
    assert status in (200, 204)