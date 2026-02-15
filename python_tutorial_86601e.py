# Mandelbrot Fractal Explorer with Interactive Zoom

# Learning Objective:
# This tutorial will teach you how to generate and visualize the
# Mandelbrot fractal using Python's `numpy` for numerical computation
# and `matplotlib` for plotting. We will cover the core concept of
# fractal generation by iterating a complex number function and
# implement interactive zooming to explore its intricate details.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector, Button

# --- Fractal Generation Core ---

def mandelbrot(c, max_iterations):
    """
    Calculates the number of iterations for a complex number 'c'
    to escape a bounded region in the complex plane.

    The Mandelbrot set is defined by the iteration of the function:
    z(n+1) = z(n)^2 + c
    where z(0) = 0.

    If the magnitude of z(n) exceeds a certain threshold (usually 2),
    the point 'c' is considered to be outside the Mandelbrot set.
    The number of iterations it takes to escape determines the color.

    Args:
        c (complex): The complex number to test.
        max_iterations (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations before escaping, or max_iterations
             if it does not escape within the limit.
    """
    z = 0  # Initialize z to 0
    for i in range(max_iterations):
        z = z*z + c  # The core Mandelbrot iteration
        # Check if the magnitude of z exceeds 2. If it does, the point is outside.
        # We use abs(z)**2 > 4 for efficiency, avoiding the expensive sqrt.
        if abs(z) > 2:
            return i  # Return the escape iteration count
    return max_iterations  # If it doesn't escape, it's likely in the set

# --- Plotting and Visualization ---

def create_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iterations):
    """
    Generates a 2D NumPy array representing the Mandelbrot fractal
    for a given region of the complex plane.

    This function maps pixels on a 2D image to complex numbers.
    Each pixel's color will be determined by the Mandelbrot iteration count.

    Args:
        xmin, xmax (float): The minimum and maximum real values of the complex plane.
        ymin, ymax (float): The minimum and maximum imaginary values of the complex plane.
        width (int): The width of the output image in pixels.
        height (int): The height of the output image in pixels.
        max_iterations (int): The maximum iterations for the mandelbrot function.

    Returns:
        np.ndarray: A 2D array where each element is the iteration count
                    for the corresponding complex number.
    """
    # Create arrays of real and imaginary parts corresponding to pixel coordinates
    # np.linspace creates evenly spaced numbers over a specified interval.
    real_axis = np.linspace(xmin, xmax, width)
    imag_axis = np.linspace(ymin, ymax, height)

    # Create a grid of complex numbers from the real and imaginary axes.
    # This creates a 2D array where each element is a complex number c = x + iy.
    # We use broadcasting: real_axis[:, np.newaxis] makes it a column vector,
    # then it's combined with imag_axis (a row vector).
    complex_grid = real_axis[:, np.newaxis] + 1j * imag_axis

    # Apply the mandelbrot function to each complex number in the grid.
    # np.vectorize allows us to apply a Python function (like mandelbrot)
    # element-wise to NumPy arrays.
    mandelbrot_iterations = np.vectorize(mandelbrot)(complex_grid, max_iterations)

    # Transpose the result because matplotlib plots images with (height, width)
    # and our current grid calculation leads to (width, height) if not handled.
    return mandelbrot_iterations.T

# --- Interactive Exploration ---

class MandelbrotExplorer:
    """
    Manages the interactive exploration of the Mandelbrot fractal.
    Handles zooming and re-rendering the fractal.
    """
    def __init__(self, ax, initial_xmin, initial_xmax, initial_ymin, initial_ymax, initial_max_iter=100):
        """
        Initializes the Mandelbrot explorer.

        Args:
            ax (matplotlib.axes.Axes): The axes object to draw on.
            initial_xmin, initial_xmax, initial_ymin, initial_ymax: Initial complex plane bounds.
            initial_max_iter: Initial maximum iterations.
        """
        self.ax = ax
        self.xmin, self.xmax = initial_xmin, initial_xmax
        self.ymin, self.ymax = initial_ymin, initial_ymax
        self.max_iterations = initial_max_iter
        self.width, self.height = 800, 600  # Pixel dimensions of the image

        # Initial rendering of the fractal
        self.img = self.ax.imshow(
            create_mandelbrot_image(self.xmin, self.xmax, self.ymin, self.ymax, self.width, self.height, self.max_iterations),
            extent=[self.xmin, self.xmax, self.ymin, self.ymax], # Set axis limits from extent
            cmap='magma' # Color map for visualization
        )
        self.ax.set_title("Mandelbrot Fractal Explorer")
        self.ax.set_xlabel("Real")
        self.ax.set_ylabel("Imaginary")

        # Setup RectangleSelector for zooming
        self.selector = RectangleSelector(
            self.ax,
            self.on_select,
            drawtype='box',
            interactive=True,
            button=[1],  # Left mouse button to select
            minspanx=5, minspany=5, # Minimum selection size
            spinesize=2,
            lineprops=dict(color='r', linestyle='-', linewidth=1, alpha=0.5)
        )

        # Add a reset button
        reset_ax = plt.axes([0.8, 0.025, 0.1, 0.05]) # Position of the button
        self.reset_button = Button(reset_ax, 'Reset')
        self.reset_button.on_clicked(self.reset_view)

    def on_select(self, eclick, erelease):
        """
        Callback function when a rectangle is selected for zooming.
        Updates the view and re-renders the fractal.
        """
        # Get the coordinates of the selected rectangle
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        # Ensure x1 < x2 and y1 < y2 for correct axis setting
        self.xmin, self.xmax = min(x1, x2), max(x1, x2)
        self.ymin, self.ymax = min(y1, y2), max(y1, y2)

        # Increase max_iterations for deeper zooms to reveal more detail
        self.max_iterations = int(self.max_iterations * 1.2)
        if self.max_iterations > 5000: # Cap at a reasonable maximum
            self.max_iterations = 5000

        print(f"Zooming to: Real [{self.xmin:.4f}, {self.xmax:.4f}], Imaginary [{self.ymin:.4f}, {self.ymax:.4f}]")
        print(f"Max Iterations: {self.max_iterations}")

        # Re-render the fractal with the new bounds and increased iterations
        self.update_fractal()

    def update_fractal(self):
        """
        Generates and displays the fractal with current bounds and iterations.
        """
        new_image_data = create_mandelbrot_image(self.xmin, self.xmax, self.ymin, self.ymax, self.width, self.height, self.max_iterations)
        self.img.set_data(new_image_data)
        # Update extent to match new axis limits
        self.img.set_extent([self.xmin, self.xmax, self.ymin, self.ymax])
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)
        plt.draw() # Redraw the canvas to show the changes

    def reset_view(self, event):
        """
        Resets the view to the initial complex plane bounds and iterations.
        """
        print("Resetting view.")
        self.xmin, self.xmax = initial_xmin_global, initial_xmax_global
        self.ymin, self.ymax = initial_ymin_global, initial_ymax_global
        self.max_iterations = initial_max_iter_global
        self.update_fractal()

# --- Example Usage ---

if __name__ == "__main__":
    # Define initial complex plane bounds
    initial_xmin_global, initial_xmax_global = -2.0, 1.0
    initial_ymin_global, initial_ymax_global = -1.5, 1.5
    initial_max_iter_global = 100

    # Create a figure and an axes for plotting
    fig, ax = plt.subplots(figsize=(10, 7))

    # Instantiate the MandelbrotExplorer
    explorer = MandelbrotExplorer(
        ax,
        initial_xmin_global, initial_xmax_global,
        initial_ymin_global, initial_ymax_global,
        initial_max_iter_global
    )

    # Show the plot and enable interactive mode
    plt.show()