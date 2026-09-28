from functions import pressKey
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import numpy as np


# Define array
A = np.array([[0, 1],
              [1, 0]])

# Create a grid
axis, step = 5, 15
x = np.linspace(-axis, axis, step)
y = np.linspace(-axis, axis, step)
X, Y = np.meshgrid(x, y)

# Vector field: F(x,y) = A · [x, y]
U = A[0, 0]*X + A[0, 1]*Y
V = A[1, 0]*X + A[1, 1]*Y

fig, ax = plt.subplots(figsize=(8, 8))
ax.quiver(X, Y, U, V, color='green', scale=100, width=0.003)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

ax.set_xlim(-axis, axis)
ax.set_ylim(-axis, axis)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.tick_params(labelsize=12)

for _, spine in ax.spines.items():
    spine.set_visible(True)

plt.tight_layout()
fig.canvas.mpl_connect('key_press_event', pressKey)
plt.show()
