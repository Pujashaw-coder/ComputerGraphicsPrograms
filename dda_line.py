# Program: DDA Line Drawing Algorithm
# Author: Puja Kumari

import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    points = []
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points

x1, y1 = 2, 2
x2, y2 = 8, 6
points = DDA(x1, y1, x2, y2)

for p in points:
    plt.plot(p[0], p[1], 'ro')

plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.show()
