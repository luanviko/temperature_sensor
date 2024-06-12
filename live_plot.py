import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize an empty plot
line,      = ax.plot([], [], lw=2, label="Probe", color="blue")
line_room, = ax.plot([], [], lw=2, label="Room",  color="orange")

# Function to initialize the plot
def init():
    room, probe = np.loadtxt("./live_data.csv", usecols=(1,2), delimiter=",", skiprows=1, unpack=True)
    ax.set_xlim(0, len(probe))
    ax.set_ylim(np.min(probe)-10, np.max(probe)+10)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(r"Temperature ($^\circ$C)")
    line.set_data(np.arange(0, len(probe)), probe)
    line_room.set_data(np.arange(0, len(room)), room)
    ax.legend()
    return line,

# Function to update the plot
def update(frame):
    # ax.acl()
    room, probe = np.loadtxt("./live_data.csv", usecols=(1,2), delimiter=",", skiprows=1, unpack=True)
    difference = room[-1]-probe[1]
    print(f"Room: {room[-1]} C. Probe: {probe[-1]} C. Difference: {difference:4.2f} C.")
    ax.set_xlim(0, len(probe)+20)
    ax.set_ylim(np.min(probe)-10, np.max(probe)+10)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(r"Temperature ($^\circ$C)")
    line.set_data(np.arange(0, len(probe)), probe)
    line_room.set_data(np.arange(0, len(room)), room)
    ax.legend()
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, interval=1200, repeat=True)

plt.show()