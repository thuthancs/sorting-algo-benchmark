from algorithms.comparison import bubble_sort
from algorithms.comparison import insertion_sort
from tests.helpers import assert_sort


def test_bubble_sort():
    assert_sort(bubble_sort)


def test_insertion_sort():
    assert_sort(insertion_sort)
