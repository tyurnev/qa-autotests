from app.api_client import ApiClient


def test_create_post_returns_201_and_echoes_payload(
    api_client: ApiClient,
    generated_post_payload: dict[str, int | str],
):
    status, data = api_client.post_json("/posts", generated_post_payload)

    assert status == 201
    assert isinstance(data, dict)

    assert "id" in data
    assert data["title"] == generated_post_payload["title"]
    assert data["body"] == generated_post_payload["body"]
    assert data["userId"] == generated_post_payload["userId"]