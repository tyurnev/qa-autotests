import pytest

@pytest.fixture(scope="module")
def unit_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]

@pytest.fixture(scope="module")
def required_user_keys() -> list[str]:
    return ["id", "email", "name"]