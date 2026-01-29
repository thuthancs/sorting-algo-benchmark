from typing import Generator, Tuple, Optional
from visualizer import animate
import random


def insertion_sort_steps(
    arr: list[int],
) -> Generator[Tuple[list[int], Optional[tuple[int, ...]]], None, None]:
    result = arr.copy()
    n = len(result)

    # initial state
    yield result[:], None

    for i in range(1, n):
        key = result[i]
        j = i - 1

        # highlight key being inserted
        yield result[:], (i,)

        while j >= 0 and result[j] > key:
            # highlight comparison + shift
            yield result[:], (j, j + 1)

            result[j + 1] = result[j]
            yield result[:], (j, j + 1)

            j -= 1

        result[j + 1] = key
        # highlight insertion position
        yield result[:], (j + 1,)

    # final state
    yield result[:], None


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate(
        insertion_sort_steps,
        data,
        title="Insertion Sort Visualization",
        filename="insertion_sort.gif",
        fps=30,
    )
