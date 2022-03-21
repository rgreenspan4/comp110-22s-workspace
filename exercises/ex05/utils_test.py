"""This program tests utils."""
__author__ = 730530918

from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Only evens empty test."""
    assert only_evens([]) == []


def test_only_evens_single() -> None:
    """Only evens with a single value test."""
    xs: list[int] = [110]
    assert only_evens(xs) == [110]


def test_only_evens_many() -> None:
    """Only evens with many values test."""
    xs: list[int] = [5, 7, 6, 8]
    assert only_evens(xs) == [6, 8]


def test_sub_empty() -> None:
    """Sub empty test."""
    assert sub([], 1, 3) == []


def test_sub_single() -> None:
    """Sub with a single value test."""
    test_list: list[int] = [4]
    assert sub(test_list, 0, 4) == [4]


def test_sub_many() -> None:
    """Sub with many values test."""
    test_list: list[int] = [4, 76, 56, 32, 34, 643, 23, 4]
    assert sub(test_list, 2, 5) == [56, 32, 34]


def test_concat_empty() -> None:
    """Concat empty test."""
    assert concat([], []) == []


def test_concat_single() -> None:
    """Concat with a single value test."""
    assert concat([9], [5]) == [9, 5]


def test_concat_many() -> None:
    """Concat with many values test."""
    assert concat([9, 5, 6, 3], [3, 4, 5]) == [9, 5, 6, 3, 3, 4, 5]