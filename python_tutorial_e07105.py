# Learning Objective:
# This tutorial will teach you how to create interactive visualizations
# with Matplotlib by using simple event handling. We'll focus on
# responding to mouse clicks on specific plot elements to reveal
# more information or change the visualization. This is a fundamental
# step towards building data stories that engage users.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Setting up our Data ---
# Let's imagine we have some data about different cities and their populations.
# We'll represent this data as points on a scatter plot.
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
populations = [8.4, 3.9, 2.7, 2.3, 1.7] # in millions
coordinates = [(0, 0), (1, 2), (2, 1), (3, 3), (4, 0)] # Example coordinates

# For each city, we'll also have some additional information to reveal on click.
city_details = {
    'New York': 'The Big Apple, known for its diversity and iconic landmarks.',
    'Los Angeles': 'City of Angels, famous for Hollywood and its sprawling beaches.',
    'Chicago': 'The Windy City, renowned for its architecture and deep-dish pizza.',
    'Houston': 'Space City, home to NASA\'s Johnson Space Center.',
    'Phoenix': 'Valley of the Sun, known for its hot desert climate and vibrant arts scene.'
}

# --- 2. Creating the Base Visualization ---
# We'll create a figure and an axes object, which are the fundamental
# building blocks of any Matplotlib plot.
fig, ax = plt.subplots(figsize=(10, 6)) # Create a figure and an axes. Adjust size as needed.

# Scatter plot: Each city will be a point.
# We store the scatter plot objects (the points themselves) in a list.
# This is crucial for event handling, as we'll need to identify which point was clicked.
scatter_points = []
for i, (x, y) in enumerate(coordinates):
    # Create a scatter point for each city.
    # 's' is the marker size, 'c' is the color.
    # 'label' is important for identifying the data associated with the point.
    point, = ax.scatter(x, y, s=200, c=f'C{i}', label=cities[i], picker=True, pickradius=5)
    # 'picker=True' enables picking for this artist (the scatter point).
    # 'pickradius' defines the tolerance in points around the artist for a pick event.
    scatter_points.append(point)
    # Annotate the plot with the city name next to its point.
    ax.annotate(cities[i], (x, y), textcoords="offset points", xytext=(10, 5), ha='left')

# Set plot title and labels for clarity.
ax.set_title('City Populations and Locations (Click to Learn More!)')
ax.set_xlabel('Location X Coordinate')
ax.set_ylabel('Location Y Coordinate')
ax.grid(True, linestyle='--', alpha=0.6) # Add a grid for better readability.

# --- 3. Setting up Event Handling ---
# This is the core of our interactivity. We'll define a function that
# gets called whenever an "event" happens, like a mouse click.

# This list will store the active text annotation for details.
# We only want one detail annotation visible at a time.
current_detail_annotation = None

def on_pick(event):
    """
    This function is called when a pick event occurs (e.g., clicking on a scatter point).
    It displays additional information about the clicked city.
    """
    global current_detail_annotation # Access the global variable to modify it.

    # 'event.artist' is the Matplotlib artist that was picked (e.g., our scatter point).
    # 'event.artist.get_label()' retrieves the label we assigned earlier (the city name).
    clicked_city = event.artist.get_label()

    # Find the coordinate of the clicked city.
    # We need the original x, y of the clicked point to place the annotation.
    clicked_x, clicked_y = event.artist.get_offsets()[0] # For scatter, get_offsets() returns an array of [x, y]

    # If there's an existing detail annotation, remove it.
    if current_detail_annotation:
        current_detail_annotation.remove()
        current_detail_annotation = None # Reset the variable.

    # Get the details for the clicked city.
    details = city_details.get(clicked_city, 'No details available.')

    # Add a new text annotation to display the details.
    # We'll place it slightly above and to the right of the clicked point.
    current_detail_annotation = ax.annotate(
        f"{clicked_city}: {details}", # The text to display.
        (clicked_x, clicked_y),      # The point to anchor the annotation to.
        textcoords="offset points",  # How to interpret xytext.
        xytext=(0, 15),              # Offset from the anchor point (x, y).
        ha='left',                   # Horizontal alignment.
        fontsize=9,                  # Smaller font size for details.
        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5) # Add a background box.
    )

    # Redraw the canvas to show the new annotation.
    fig.canvas.draw_idle()

# Connect the 'pick_event' to our 'on_pick' function.
# This tells Matplotlib: "When a pick event happens on this figure, call the 'on_pick' function."
fig.canvas.mpl_connect('pick_event', on_pick)

# --- 4. Displaying the Visualization ---
# This is the final step that shows the plot window.
# The window will remain open and responsive to events until it's closed by the user.
print("Creating interactive plot. Click on a city point to see details!")
plt.show()

# --- Example Usage Notes ---
# 1. Run this script. A window will appear with the scatter plot.
# 2. Click on any of the colored circles representing a city.
# 3. You should see a text box appear near the clicked city, revealing its description.
# 4. Clicking another city will remove the previous description and show the new one.
# 5. The 'picker=True' and 'pickradius' in the 'ax.scatter' call are essential for enabling clicks.
# 6. The 'fig.canvas.mpl_connect('pick_event', on_pick)' line is where we link the click event to our handler function.