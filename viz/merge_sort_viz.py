from typing import Generator, Tuple, Optional
from visualizer import animate
import random


def merge_sort_steps(
    arr: list[int],
) -> Generator[Tuple[list[int], Optional[tuple[int, ...]]], None, None]:
    if not arr:
        yield [], None
        return

    result = arr.copy()
    yield result[:], None  # initial state

    # use a nested generator-based sort
    yield from _sort_steps(result, 0, len(result) - 1)

    yield result[:], None  # final state


def _sort_steps(
    arr: list[int],
    start: int,
    end: int,
) -> Generator[Tuple[list[int], Optional[tuple[int, ...]]], None, None]:
    if start >= end:
        return

    mid = (start + end) // 2

    yield from _sort_steps(arr, start, mid)
    yield from _sort_steps(arr, mid + 1, end)

    # optional: highlight the current merge range boundaries
    yield arr[:], (start, mid, end)

    yield from _merge_steps(arr, start, mid, end)

    # optional: show merged segment done
    yield arr[:], (start, end)


def _merge_steps(
    arr: list[int],
    start: int,
    mid: int,
    end: int,
) -> Generator[Tuple[list[int], Optional[tuple[int, ...]]], None, None]:
    n1 = mid - start + 1
    n2 = end - mid

    left = [arr[start + i] for i in range(n1)]
    right = [arr[mid + 1 + j] for j in range(n2)]

    i = j = 0
    k = start

    while i < n1 and j < n2:
        # highlight: comparing heads + target write position
        yield arr[:], (start + i, mid + 1 + j, k)

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        # highlight: wrote position k
        yield arr[:], (k,)
        k += 1

    while i < n1:
        yield arr[:], (start + i, k)
        arr[k] = left[i]
        i += 1
        yield arr[:], (k,)
        k += 1

    while j < n2:
        yield arr[:], (mid + 1 + j, k)
        arr[k] = right[j]
        j += 1
        yield arr[:], (k,)
        k += 1


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate(
        merge_sort_steps(data),
        title="Merge Sort Visualization",
        filename="merge_sort.gif",
        fps=30,
    )
