
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation


C = [0, 0]

B = [50, 0]

A = [25, 25 * math.sqrt(3)]

point = {3: A, 2: A, 5: B, 1: B, 4: C, 6: C}
x = 10
y = 20

fig, ax = plt.subplots()
k, m = [], []
sc = ax.scatter(k, m, c='r', s=0.4)
plt.xlim(-10, 60)
plt.ylim(-10, 60)
last = {"x": 10, "y": 20}

fig.set_size_inches(11.5, 6.5, forward=True)


def animate(i):

    for j in range(30):

        p = point[random.randrange(1, 7)]

        x = last["x"]
        y = last["y"]
        xdist = abs(x - p[0]) / 2
        ydist = abs(y - p[1]) / 2

        if p[0] < x:
            x -= xdist
        else:
            x += xdist

        if p[1] < y:
            y -= ydist
        else:
            y += ydist
        k.append(x)
        m.append(y)
        last["x"] = x
        last["y"] = y
    sc.set_offsets(np.c_[k, m])


ani = matplotlib.animation.FuncAnimation(fig, animate,
                                         frames=1, interval=1, repeat=True)
plt.show()
