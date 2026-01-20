from app.validators import (
    is_status_ok,
    is_valid_uuid,
    is_non_empty_string,
    is_valid_email,
    has_keys,
)

def test_is_status_ok_true_for_2xx():
    assert is_status_ok(200) is True
    assert is_status_ok(204) is True
    assert is_status_ok(299) is True

def test_is_status_ok_false_for_non_2xx():
    assert is_status_ok(199) is False
    assert is_status_ok(300) is False
    assert is_status_ok(404) is False

def test_is_valid_uuid_accepts_real_uuid():
    assert is_valid_uuid("550e8400-e29b-41d4-a716-446655440000") is True

def test_is_valid_uuid_rejects_invalid_value():
    assert is_valid_uuid("not-a-uuid") is False

def test_validation_helpers():
    assert is_non_empty_string("  hi  ") is True
    assert is_non_empty_string("   ") is False
    assert is_valid_email("User@Test.com") is True
    assert is_valid_email("not-an-email") is False
    assert has_keys({"a": 1, "b": 2}, ["a", "b"]) is True
    assert has_keys({"a": 1}, ["a", "b"]) is False
