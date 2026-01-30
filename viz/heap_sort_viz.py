from typing import Generator, Tuple, Optional, List
from visualizer import animate
import random


def heap_sort_steps(
    arr: List[int],
) -> Generator[Tuple[List[int], Optional[tuple[int, ...]]], None, None]:
    if not arr:
        yield [], None
        return

    a = arr.copy()
    n = len(a)

    yield a[:], None  # initial

    # --- helpers (steps version) ---
    def max_heapify_steps(i: int, heap_size: int):
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i

            # highlight comparisons
            if l < heap_size:
                yield a[:], (i, l)
                if a[l] > a[largest]:
                    largest = l
            if r < heap_size:
                yield a[:], (largest, r)
                if a[r] > a[largest]:
                    largest = r

            if largest == i:
                break

            a[i], a[largest] = a[largest], a[i]
            yield a[:], (i, largest)  # swap
            i = largest

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from max_heapify_steps(i, n)

    # extract max repeatedly
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        yield a[:], (0, end)  # swap max to the end
        yield from max_heapify_steps(0, end)

    yield a[:], None  # final


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate(
        heap_sort_steps(data),
        title="Heap Sort Visualization",
        filename="heap_sort.gif",
        fps=30,
    )
