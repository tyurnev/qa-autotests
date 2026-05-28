from app.api_client import ApiClient

def test_put_post_returns_200_and_echoes_payload(
    api_client: ApiClient,
    generated_put_post_payload: dict[str, int | str],
):
    post_id = generated_put_post_payload["id"]

    status, data = api_client.put_json(f"/posts/{post_id}", generated_put_post_payload)

    assert status == 200
    assert isinstance(data, dict)

    assert data["id"] == generated_put_post_payload["id"]
    assert data["title"] == generated_put_post_payload["title"]
    assert data["body"] == generated_put_post_payload["body"]
    assert data["userId"] == generated_put_post_payload["userId"]

def test_patch_post_returns_200_and_updates_title(
    api_client: ApiClient,
    generated_patch_payload: dict[str, str],
):
    status, data = api_client.patch_json("/posts/1", generated_patch_payload)

    assert status == 200
    assert isinstance(data, dict)

    assert data["title"] == generated_patch_payload["title"]

def test_delete_post_returns_success_status(api_client: ApiClient):
    status = api_client.delete("/posts/1")
    assert status in (200, 204)