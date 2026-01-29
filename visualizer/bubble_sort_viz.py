from typing import Generator, Tuple, Optional
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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


def animate_bubble_sort(
    data: list[int], filename="bubble_sort.gif", fps=30, show=False
):
    steps = iter(bubble_sort_steps(data))

    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    ax.set_xlim(-0.5, len(data) - 0.5)
    ax.set_ylim(0, max(data) * 1.1)

    bars = ax.bar(range(len(data)), data)

    def update(_):
        arr, highlight = next(steps)

        for bar, height in zip(bars, arr):
            bar.set_height(height)
            bar.set_color("C0")

        if highlight is not None:
            i, j = highlight
            bars[i].set_color("C3")
            bars[j].set_color("C3")

        return bars

    anim = FuncAnimation(
        fig,
        update,
        frames=10**6,
        interval=1000 // fps,
        repeat=False,
        blit=False,
    )

    anim.save(filename, writer="pillow", fps=fps)
    plt.close(fig)
    if show:
        plt.show()


if __name__ == "__main__":
    data = random.sample(range(1, 50), 40)
    animate_bubble_sort(data, filename="bubble_sort.gif", fps=30)
