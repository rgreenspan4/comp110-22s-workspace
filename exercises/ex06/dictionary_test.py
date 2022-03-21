"""This program tests the dictionary function."""
__author__ = 730530918

from dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """This test makes sure it will return an empty dictionary if given an empty dictionary."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """This will test to make sure it can invert one dictionary key/ value."""
    assert invert({"hi": "bye"}) == {"bye": "hi"}


def test_invert_multple() -> None:
    """This will test to make sure it can invert multple dictionary keys/values."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_count_empty() -> None:
    """This test makes sure it will return an empty dictionary if given an empty list."""
    assert count([]) == {}


def test_count_one() -> None:
    """This will test to make sure it can count one dictionary key/ value."""
    assert count(['Jeffery']) == {'Jeffery': 1}


def test_count_many() -> None:
    """This will test to make sure it can count multple dictionary keys/values."""
    assert count(['a', 'a', 'a', 'b', 'b', 'c', 'd']) == {'a': 3, 'b': 2, 'c': 1, 'd': 1}


def test_favorite_color_empty() -> None:
    """This test makes sure it will return an empty dictionary if given an empty string value."""
    assert favorite_color({}) == ""


def test_favorite_color_one() -> None:
    """This will test to make sure it can find the favorite color out of one choice."""
    assert favorite_color({'Robby': 'blue'}) == 'blue'


def test_favorite_color_many() -> None:
    """This will find the most popular color out of many."""
    assert favorite_color({'Robby': 'green', 'Jessie': 'green', 'Danny': 'blue', 'Kris': 'blue', 'jesse': 'blue', 'Jeffery': 'red'}) == 'blue'