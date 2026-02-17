from typing import Any

REQUIRED_POST_KEYS = {"userId", "id", "title", "body"}
REQUIRED_COMMENT_KEYS = {"postId", "id", "name", "email", "body"}

def assert_post_contract(data: Any) -> None:
    assert isinstance(data, dict)
    assert REQUIRED_POST_KEYS.issubset(data.keys())

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

def assert_comment_contract(data: Any) -> None:
    assert isinstance(data, dict)
    assert REQUIRED_COMMENT_KEYS.issubset(data.keys())

    assert isinstance(data["postId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
    assert isinstance(data["body"], str)
