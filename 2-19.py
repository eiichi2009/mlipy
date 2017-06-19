import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10,10))
frame_num = int(3.14*2 / 0.1)

def update(i, fig_title, A):
    if i != 0:
        plt.cla()
    theta = i * 0.1
    x = np.cos(theta)
    y = np.sin(theta)
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.plot(x,y, marker="o", markersize=10)
    plt.title(fig_title + "theta=" + str(i))

ani = anm.FuncAnimation(fig, update, fargs = ("Initial Animation", 2.0), interval=1, frames = frame_num)

plt.show()
