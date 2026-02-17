import pytest
from app.api_client import ApiClient
from tests.helpers.api_contracts import assert_comment_contract

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_for_post_returns_200_and_valid_items(api_client: ApiClient, post_id: int):
    status, data = api_client.get_json(f"/posts/{post_id}/comments")

    assert status == 200
    assert isinstance(data, list)
    assert len(data) > 0

    # Проверяем первые 3 элемента
    for comment in data[:3]:
        assert_comment_contract(comment)
        assert comment["postId"] == post_id
