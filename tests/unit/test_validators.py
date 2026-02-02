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

@pytest.mark.parametrize(
    "value,expected",
    [("  hi  ", True), ("   ", False), ("", False), (None, False), (123, False)],
)
def test_is_non_empty_string(value, expected: bool):
    assert is_non_empty_string(value) is expected

@pytest.mark.parametrize("email", ["User@Test.com", "a.b+c@test.co.uk", "test@example.com"])
def test_is_valid_email_accepts_valid_emails(email: str):
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", ["not-an-email", "test@", "@test.com", "test @mail.com", "test@mail", "", "   "])
def test_is_valid_email_rejects_invalid_emails(email: str):
    assert is_valid_email(email) is False

def test_has_keys_true_when_all_keys_present(sample_user_dict: dict):
    assert has_keys(sample_user_dict, ["id", "email"]) is True

@pytest.mark.parametrize(
    "obj,keys,expected",
    [
        ({"a": 1, "b": 2}, ["a", "b"], True),
        ({"a": 1}, ["a", "b"], False),
        ("not-a-dict", ["a"], False),
        (None, ["a"], False),
        ({}, [], True),
    ],
)
def test_has_keys(obj, keys, expected: bool):
    assert has_keys(obj, keys) is expected
