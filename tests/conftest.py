import pytest


@pytest.fixture
def valid_uuid() -> str:
    return "550e8400-e29b-41d4-a716-446655440000"

@pytest.fixture
def valid_emails() -> list[str]:
    return [
        "User@Test.com",
        "a.b+c@test.co.uk",
        "test@example.com",
    ]

@pytest.fixture
def invalid_emails() -> list[str]:
    return [
        "not-an-email",
        "test@",
        "@test.com",
        "test @mail.com",
        "test@mail",
        "",
        "   ",
    ]

import pytest


@pytest.fixture
def valid_uuid() -> str:
    return "550e8400-e29b-41d4-a716-446655440000"

@pytest.fixture
def valid_emails() -> list[str]:
    return [
        "User@Test.com",
        "a.b+c@test.co.uk",
        "test@example.com",
    ]

@pytest.fixture
def invalid_emails() -> list[str]:
    return [
        "not-an-email",
        "test@",
        "@test.com",
        "test @mail.com",
        "test@mail",
        "",
        "   ",
    ]

@pytest.fixture
def sample_user_dict() -> dict:
    return {"id": 1, "email": "test@example.com", "name": "John"}