import random
from visualizer import animate
from typing import Generator, Tuple, Optional


def selection_sort_steps(
    arr: list[int],
) -> Generator[Tuple[list[int], Optional[tuple[int, int]]], None, None]:
    if not arr:
        yield [], None
        return

    result = arr.copy()
    yield result[:], None

    n = len(result)
    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            # highlight: current best vs candidate
            yield result[:], (min_idx, j)

            if result[j] < result[min_idx]:
                min_idx = j
                # highlight: new min vs current i (still 2 values)
                yield result[:], (min_idx, i)

        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
            yield result[:], (i, min_idx)

    yield result[:], None


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate(
        selection_sort_steps,
        data,
        title="Selection Sort Visualization",
        filename="selection_sort.gif",
        fps=30,
    )
