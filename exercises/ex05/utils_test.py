"""EX05 -- unit test for funtions in utils."""

__author__ = "730365499"

from utils import only_evens, sub, concat


def test_even_number_none() -> None:
    """Test for even number function with no even number in list."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_even_number_one() -> None:
    """Test for even number function with only one even number in list."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_even_number_all() -> None:
    """Test for even number function with all numbers in list are even."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_one() -> None:
    """Test for sub function when start and end index numbers are within the list length."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_two() -> None:
    """Test for sub function when start index less than 0."""
    a_list: list[int] = [1, 2, 3, 5, 9, 10]
    assert sub(a_list, -1, 5) == [1, 2, 3, 5, 9, 10]


def test_sub_three() -> None:
    """Test for sub function when length of list is 0."""
    a_list: list[int] = []
    assert sub(a_list, 1, 5) == []


def test_concat_one() -> None:
    """Test for concat function when two lists have numbers."""
    xs: list[int] = [1, 3, 5, 7]
    ys: list[int] = [2, 4, 6, 8]
    assert concat(xs, ys) == [1, 3, 5, 7, 2, 4, 6, 8]


def test_concat_two() -> None:
    """Test for concat function when first list is empty."""
    xs: list[int] = []
    ys: list[int] = [9]
    assert concat(xs, ys) == [9]


def test_concat_three() -> None:
    """Test for concat function when second list is empty."""
    xs: list[int] = [4, 6, 1, 2, 7]
    ys: list[int] = []
    assert concat(xs, ys) == [4, 6, 1, 2, 7]