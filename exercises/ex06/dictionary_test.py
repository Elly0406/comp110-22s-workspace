"""EX06 - test for funtions in dictionary."""

__author__ = "730365499"


from dictionary import invert, favorite_color, count


def test_invert_one() -> None:
    """Test for invert function. Switch the position of value and key."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two() -> None:
    """Test for invert function."""
    a: dict[str, str] = {'apple': 'cat'}
    assert invert(a) == {'cat': 'apple'}


def test_invert_three() -> None:
    """Test for invert function."""
    a: dict[str, str] = {'happy': 'weekend'}
    assert invert(a) == {'weekend': 'happy'}


def test_color_one() -> None:
    """Test for favorite colors function to return the most frequent value."""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_color_two() -> None:
    """Test for favorite colors function when there is a tie."""
    a: dict[str, str] = {"lily": "blue", "zoe": "pink", "jerry": "purple"}
    assert favorite_color(a) == "blue"


def test_color_three() -> None:
    """Test for favorite colors function to return the most frequent value."""
    a: dict[str, str] = {"jeff": "white", "elly": "white", "RJ": "black"}
    assert favorite_color(a) == "white"


def test_count_one() -> None:
    """Test for count funtion."""
    xs: list[str] = ['apple', 'orange', 'orange', 'banana', 'apple']
    assert count(xs) == {'apple': 2, 'orange': 2, 'banana': 1}


def test_count_two() -> None:
    """Test for count function when there is no str in list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_three() -> None:
    """Test for count function."""
    xs: list[str] = ['1', '2', '3', '3']
    assert count(xs) == {'1': 1, '2': 1, '3': 2}