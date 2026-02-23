import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_title("Animated Circle")

# Create circle
circle = plt.Circle((0, 5), 0.2, color='blue')
ax.add_patch(circle)

# Animation function
def animate(i):
    circle.center = (i * 0.1, 5)   # Move circle horizontally
    return circle,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,
    interval=50,
    blit=True
)

plt.show()