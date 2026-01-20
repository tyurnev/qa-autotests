import re

def normalize_email(email: str) -> str:
    return email.strip().lower()

def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

def mask_token(token: str, visible: int = 4) -> str:
    if visible < 0:
        raise ValueError("Visible must be non-negative")
    if len(token) <= visible:
        return "*" * len(token)
    hidden_len = len(token) - visible
    return "*" * hidden_len + token[-visible:]