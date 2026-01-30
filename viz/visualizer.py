import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(step_generator, title, filename=None, fps=30):
    # Get first frame to size the plot
    first_arr, first_highlight = next(step_generator)
    n = len(first_arr)

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(0, (max(first_arr) if first_arr else 1) * 1.1)

    bars = ax.bar(range(n), first_arr)

    def update(frame):
        arr, highlight = frame

        # update heights + reset colors
        for bar, h in zip(bars, arr):
            bar.set_height(h)
            bar.set_color("C0")

        # highlight any number of indices safely
        if highlight is not None:
            for idx in highlight:
                if 0 <= idx < n:
                    bars[idx].set_color("C3")

        return bars

    # IMPORTANT:
    # We already consumed 1 frame (first_arr).
    # So chain it back in front of the remaining generator frames.
    def frames():
        yield (first_arr, first_highlight)
        yield from step_generator

    anim = FuncAnimation(
        fig,
        update,
        frames=frames(),
        interval=1000 // fps,
        repeat=False,
        blit=False,
    )

    if filename:
        anim.save(filename, writer="pillow", fps=fps)
        plt.close(fig)
    else:
        plt.show()
