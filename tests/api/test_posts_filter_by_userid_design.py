import pytest
from app.api_client import ApiClient
from tests.helpers.api_contracts import assert_post_contract


TEST_CASES = [
    ("APR-01", "/posts?userId=1", 200, True, 1),
    ("APR-02", "/posts?userId=10", 200, True, 10),
    ("APR-03", "/posts?userId=0", 200, False, None),
    ("APR-04", "/posts?userId=11", 200, False, None),
    ("APR-05", "/posts?userId=-1", 200, False, None),
    ("APR-06", "/posts?userId=abc", 200, False, None),
    ("APR-07", "/posts", 200, True, None),
    ("APR-08", "/posts?userId=", 200, False, None),
]


@pytest.mark.parametrize(
    "case_id,path,expected_status,expect_non_empty,expected_user_id",
    TEST_CASES,
    ids=[c[0] for c in TEST_CASES],
)
def test_posts_filter_by_userid_matches_test_design(
    api_client: ApiClient,
    case_id: str,
    path: str,
    expected_status: int,
    expect_non_empty: bool,
    expected_user_id: int | None,
):
    status, data = api_client.get_json(path)

    assert status == expected_status
    assert isinstance(data, list)

    if len(data) == 0:
        if expect_non_empty:
            pytest.fail(f"{case_id}: expected non-empty list, got empty list")
        assert data == []
        return

    for item in data[:3]:
        assert_post_contract(item)

    if expected_user_id is not None:
        for item in data[:3]:
            assert item["userId"] == expected_user_id

    if not expect_non_empty:
        pytest.fail(f"{case_id}: expected empty list, got {len(data)} items")
