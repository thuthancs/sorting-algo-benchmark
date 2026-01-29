from algorithms.comparison import bubble_sort
from tests.helpers import assert_sort


def test_bubble_sort():
    assert_sort(bubble_sort)
