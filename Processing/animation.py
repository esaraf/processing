'''
Purpose: Gain comfort in processing code (p5)
Goal: Generate a moving circle
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
(line,) = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # update the data
    return (line,)


ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)
plt.show()
