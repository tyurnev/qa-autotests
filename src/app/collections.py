from typing import Iterable, List, Sequence, TypeVar


T = TypeVar('T')

def unique_preserve_order(items: Iterable[T]) -> List[T]:
    seen = set()
    result: List[T] = []
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result

def flatten_once(items: Sequence[Sequence[T]]) -> List[T]:
    result: List[T] = []
    for group in items:
        result.extend(group)
    return result

def find_first(items: Iterable[T], predicate) -> T | None:
    for x in items:
        if predicate(x):
            return x
    return None