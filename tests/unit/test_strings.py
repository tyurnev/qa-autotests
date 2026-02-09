import pytest
from app.strings import normalize_email, is_palindrome, mask_token


def test_normalize_email_strips_spaces_and_lowercases():
    assert normalize_email("  Test@Email.COM  ") == "test@email.com"

def test_normalize_email_keeps_internal_chars():
    assert normalize_email("A.B+C@Example.com") == "a.b+c@example.com"

def test_is_palindrome_simple_true():
    assert is_palindrome("abba") is True

def test_is_palindrome_ignores_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_mask_token_masks_all_but_last_visible_chars():
    assert mask_token("1234567890", visible=4) == "******7890"

def test_run_id_is_available_in_strings(run_id: str):
    assert isinstance(run_id, str)
    assert len(run_id) > 0
