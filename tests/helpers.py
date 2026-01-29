import random
from typing import Callable


def generate_test_cases():
    return [
        [],
        [0],
        [0, 1, 2],
        [2, 1, 0],
        [4, 5, 2, 1, 8, 9],
        list(range(20)),
        list(range(20, 0, -1)),
        [random.randint(-20, 20) for _ in range(40)],
    ]


def assert_sort(sort_fn: Callable[[list], list]):
    for arr in generate_test_cases():
        original = arr[:]
        sorted_arr = sort_fn(arr[:])
        assert sorted_arr == sorted(original), f"Failed on {original}"
    return True
