import re
from typing import Any
from uuid import UUID


_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def is_status_ok(status_code: int) -> bool:
    return 200 <= status_code <= 299

def is_valid_uuid(value: str) -> bool:
    try:
        UUID(value)
        return True
    except (ValueError, AttributeError, TypeError):
        return False

def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""

def is_valid_email(value: str) -> bool:
    if not isinstance(value, str):
        return False
    return _EMAIL_RE.match(value.strip()) is not None

def has_keys(obj: Any, keys: list[str]) -> bool:
    if not isinstance(obj, dict):
        return False
    return all(k in obj for k in keys)