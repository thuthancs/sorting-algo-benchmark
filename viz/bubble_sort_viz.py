from typing import Generator, Tuple, Optional
import random
from visualizer import animate


def bubble_sort_steps(
    arr: list[int],
) -> Generator[Tuple[list[int], Optional[tuple[int, int]]], None, None]:
    result = arr.copy()
    n = len(result)

    yield result[:], None  # initial state

    for i in range(n):
        for j in range(0, n - i - 1):
            # highlight comparison
            yield result[:], (j, j + 1)

            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                yield result[:], (j, j + 1)  # state after swap

    yield result[:], None  # final state


if __name__ == "__main__":
    data = random.sample(range(1, 20), 10)
    animate(
        bubble_sort_steps,
        data,
        title="Bubble Sort Visualization",
        filename="bubble_sort.gif",
        fps=30,
    )
