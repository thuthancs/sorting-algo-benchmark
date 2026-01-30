from typing import Generator, Tuple, Optional, List
import random
from visualizer import animate


def quick_sort_steps(
    arr: List[int],
) -> Generator[Tuple[List[int], Optional[tuple[int, ...]]], None, None]:
    if not arr:
        yield [], None
        return

    result = arr.copy()
    yield result[:], None  # initial state

    yield from _quick_sort_steps(result, 0, len(result) - 1)

    yield result[:], None  # final state


def _quick_sort_steps(
    arr: List[int],
    start: int,
    end: int,
) -> Generator[Tuple[List[int], Optional[tuple[int, ...]]], None, None]:
    if start < end:
        # highlight current subarray boundaries
        yield arr[:], (start, end)

        pivot_index = yield from _partition_steps(arr, start, end)

        # recursively sort partitions
        yield from _quick_sort_steps(arr, start, pivot_index - 1)
        yield from _quick_sort_steps(arr, pivot_index + 1, end)


def _partition_steps(
    arr: List[int],
    start: int,
    end: int,
) -> Generator[Tuple[List[int], Optional[tuple[int, ...]]], None, int]:
    pivot_value = arr[end]
    i = start - 1

    # highlight pivot
    yield arr[:], (end,)

    for j in range(start, end):
        # highlight comparison with pivot
        yield arr[:], (j, end)

        if arr[j] <= pivot_value:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                # highlight swap
                yield arr[:], (i, j)

    # place pivot in correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    yield arr[:], (i + 1, end)

    return i + 1


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate(
        quick_sort_steps(data),
        title="Quick Sort Visualization",
        filename="quick_sort.gif",
        fps=30,
    )
