from algorithms.comparison import bubble_sort
from algorithms.comparison import insertion_sort
from algorithms.comparison import selection_sort
from algorithms.comparison import merge_sort
from algorithms.comparison import heap_sort
from tests.helpers import assert_sort


def test_bubble_sort():
    assert_sort(bubble_sort)


def test_insertion_sort():
    assert_sort(insertion_sort)


def test_selection_sort():
    assert_sort(selection_sort)


def test_merge_sort():
    assert_sort(merge_sort)


def test_heap_sort():
    assert_sort(heap_sort)
