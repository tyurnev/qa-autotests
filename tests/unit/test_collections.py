from app.collections import unique_preserve_order, flatten_once, find_first


def test_unique_preserve_order_removes_duplicates_and_keeps_order():
    assert unique_preserve_order([1, 2, 1, 3, 2]) == [1, 2, 3]

def test_unique_preserve_order_works_with_strings():
    assert unique_preserve_order(["a", "b", "a", "c"]) == ["a", "b", "c"]

def test_flatten_once_flattens_one_level():
    assert flatten_once([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]

def test_find_first_returns_first_match():
    assert find_first([1, 3, 4, 6], lambda x: x % 2 == 0) == 4

def test_find_first_returns_none_when_no_match():
    assert find_first([1, 3, 5], lambda x: x % 2 == 0) is None