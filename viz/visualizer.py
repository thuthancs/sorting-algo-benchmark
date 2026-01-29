from typing import Callable
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(
    func: Callable,
    data: list[int],
    title: str,
    filename,
    fps=30,
    show=False,
):
    steps = iter(func(data))

    fig, ax = plt.subplots()
    ax.set_title(f"{title}")
    ax.set_xlim(-0.5, len(data) - 0.5)
    ax.set_ylim(0, max(data) * 1.1)

    bars = ax.bar(range(len(data)), data)

    def update(_):
        arr, highlight = next(steps)

        for bar, height in zip(bars, arr):
            bar.set_height(height)
            bar.set_color("C0")

        if highlight is not None:
            for idx in highlight:
                bars[idx].set_color("C3")

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
