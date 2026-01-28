import pytest
from app.validators import (
    is_status_ok,
    is_valid_uuid,
    is_non_empty_string,
    is_valid_email,
    has_keys,
)

@pytest.mark.parametrize("code", [200, 204, 299])
def test_is_status_ok_true_for_2xx(code: int):
    assert is_status_ok(code) is True

@pytest.mark.parametrize("code", [199, 300, 404])
def test_is_status_ok_false_for_non_2xx(code: int):
    assert is_status_ok(code) is False

def test_is_valid_uuid_accepts_real_uuid(valid_uuid: str):
    assert is_valid_uuid(valid_uuid) is True

@pytest.mark.parametrize("value", ["not-a-uuid", "", "   ", None, 123])
def test_is_valid_uuid_rejects_invalid_value(value):
    assert is_valid_uuid(value) is False

@pytest.mark.parametrize("value,expected", [("  hi  ", True), ("   ", False), ("", False), (None, False), (123, False)])
def test_is_non_empty_string(value, expected: bool):
    assert is_non_empty_string(value) is expected

def test_is_valid_email_accepts_valid_emails(valid_emails: list[str]):
    for email in valid_emails:
        assert is_valid_email(email) is True

def test_validation_helpers():
    assert is_non_empty_string("  hi  ") is True
    assert is_non_empty_string("   ") is False
    assert is_valid_email("User@Test.com") is True
    assert is_valid_email("not-an-email") is False
    assert has_keys({"a": 1, "b": 2}, ["a", "b"]) is True
    assert has_keys({"a": 1}, ["a", "b"]) is False
