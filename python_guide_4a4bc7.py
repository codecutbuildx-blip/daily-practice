# Learning Objective:
# This tutorial will teach you how to create dynamic, animated data
# visualizations in Python using the `matplotlib` library.
# We'll focus on animating a simple line plot to demonstrate how to
# update plot elements over time, making your data tell a story.

# Import the necessary libraries
# `matplotlib.pyplot` is the core plotting library in Python.
# We'll use `FuncAnimation` to create the animation.
import matplotlib.pyplot as plt
# `numpy` is useful for numerical operations, especially for generating data.
import numpy as np

# --- Configuration ---
# Define the number of frames for our animation.
# This controls how long the animation will run.
NUM_FRAMES = 100
# Define the range of our x-axis data.
X_MAX = 10
# Define the amplitude and frequency of our sine wave for demonstration.
# These parameters will influence how the animated line changes.
AMPLITUDE = 1
FREQUENCY = 1

# --- Data Generation ---
# Generate the x-axis data.
# `np.linspace` creates an array of evenly spaced numbers over a specified interval.
x_data = np.linspace(0, X_MAX, NUM_FRAMES)

# --- Plot Initialization ---
# Create a figure and an axes object.
# A figure is the overall window or page that everything is drawn on.
# An axes is the actual plot area where data is visualized.
fig, ax = plt.subplots()

# Initialize an empty line plot.
# We'll update the data of this line in each animation frame.
# `ax.plot([], [])` creates a line with no initial data.
# We store the returned `Line2D` object in `line` so we can modify it later.
line, = ax.plot([], [], lw=2) # lw is line width

# Set the limits for the x and y axes.
# This is important for animation so the axes don't jump around.
ax.set_xlim(0, X_MAX)
# We'll set y-limits based on the potential range of our animated data.
# For a sine wave with AMPLITUDE 1, the range is [-1, 1].
ax.set_ylim(-AMPLITUDE * 1.5, AMPLITUDE * 1.5) # Add a little padding

# Add labels and a title to the plot for clarity.
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Dynamically Animated Data Visualization")

# --- Animation Update Function ---
# This function will be called for each frame of the animation.
# It takes the frame number (`frame`) as an argument.
def update(frame):
    # Calculate the y-data for the current frame.
    # We're simulating a sine wave whose amplitude or phase shifts over time.
    # Here, we're making the frequency increase with the frame number.
    # This creates a wave that gets "faster" as the animation progresses.
    y_data = AMPLITUDE * np.sin(FREQUENCY * x_data + frame * 0.1)

    # Update the data of the line object.
    # `line.set_data(x_data, y_data)` replaces the old data with the new data.
    # This is the core of the animation: changing the plot's content frame by frame.
    line.set_data(x_data, y_data)

    # Return the updated plot elements.
    # `FuncAnimation` needs to know which artists (like our line) have been modified.
    return line,

# --- Animation Creation ---
# Create the animation object.
# `FuncAnimation` takes the figure, the update function, and the number of frames.
# `interval` is the delay between frames in milliseconds.
# `blit=True` means that only the parts of the plot that have changed are redrawn,
# which makes the animation smoother and faster.
ani = plt.animation.FuncAnimation(
    fig,
    update,
    frames=NUM_FRAMES,
    interval=50,  # 50 milliseconds between frames (20 frames per second)
    blit=True
)

# --- Display the Animation ---
# Show the plot with the animation.
# When you run this script, a window will pop up showing the animated graph.
# If you are in a Jupyter Notebook, you might need `plt.show()` for it to render.
plt.show()

# --- Example Usage ---
# To run this script:
# 1. Make sure you have `matplotlib` and `numpy` installed:
#    pip install matplotlib numpy
# 2. Save the code as a Python file (e.g., `animated_plot.py`).
# 3. Run it from your terminal: `python animated_plot.py`
#
# This script generates a sine wave that dynamically changes its frequency
# over time, demonstrating how to create animated visualizations to show
# data evolution or trends.