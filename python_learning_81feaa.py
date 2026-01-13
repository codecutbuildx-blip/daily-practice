# Alien Invasion Pattern Visualization

# Learning Objective:
# This tutorial will teach beginners how to visualize geographical patterns of hypothetical
# alien invasions using Python. We'll focus on plotting invasion locations on a world map
# and understanding how to represent data points geographically. This will introduce
# fundamental concepts of data visualization with geographical data and the use of
# libraries like `pandas` for data handling and `matplotlib` with `geopandas` for plotting.

# Import necessary libraries.
# pandas is used for data manipulation and analysis, like reading and structuring our invasion data.
import pandas as pd
# geopandas is an extension of pandas that allows for easy work with geospatial data.
# It builds on matplotlib, so we'll import it for plotting.
import geopandas as gpd
# matplotlib.pyplot is the plotting library we'll use to display our map.
import matplotlib.pyplot as plt

# --- Data Generation (Simulating Alien Invasion Data) ---
# In a real-world scenario, you'd load this data from a CSV, database, or API.
# For this tutorial, we'll create a simple DataFrame to represent our "invasion" data.
# Each row represents an invasion event with a location.

# Create a dictionary to hold our simulated invasion data.
# Keys are column names, and values are lists of data.
invasion_data = {
    'city': ['New York', 'London', 'Tokyo', 'Sydney', 'Rio de Janeiro', 'Cairo', 'Moscow', 'Beijing', 'Los Angeles', 'Berlin'],
    'latitude': [40.7128, 51.5074, 35.6895, -33.8688, -22.9068, 30.0444, 55.7558, 39.9042, 34.0522, 52.5200],
    'longitude': [-74.0060, -0.1278, 139.6917, 151.2093, -43.1729, 31.2357, 37.6173, 116.4074, -118.2437, 13.4050],
    'intensity': [5, 3, 4, 2, 4, 3, 2, 5, 3, 2] # A hypothetical measure of invasion strength
}

# Convert the dictionary into a pandas DataFrame.
# This makes it easy to work with tabular data.
df = pd.DataFrame(invasion_data)

# --- Geospatial Data Handling ---
# To plot on a map, we need to represent our data as geographical points.
# geopandas DataFrames can hold geometric objects like points, lines, and polygons.

# Create a GeoDataFrame from our pandas DataFrame.
# We need to specify the geometry column.
# `gpd.points_from_xy` is a convenient function to create Point objects from longitude and latitude columns.
# We specify the column order for longitude and latitude.
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# --- Map Visualization ---
# Now, let's plot our invasion points on a world map.

# Get the world map data. geopandas comes with built-in datasets, including world countries.
# This dataset provides the shapes (polygons) of countries for our background map.
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create a figure and axes for our plot.
# This is the standard way to set up a plot in matplotlib.
fig, ax = plt.subplots(1, 1, figsize=(15, 10)) # figsize sets the dimensions of the plot

# Plot the world map.
# We plot the 'geometry' column of the 'world' GeoDataFrame.
# 'color' sets the background color of the countries.
# 'edgecolor' sets the color of the country borders.
world.plot(ax=ax, color='lightgray', edgecolor='black')

# Plot our invasion points on top of the world map.
# `gdf.plot` will use the 'geometry' column by default.
# `markersize` controls the size of the dots representing invasions.
# `color` sets the color of the invasion dots.
# `alpha` controls the transparency of the dots (0 is fully transparent, 1 is fully opaque).
# `label` is for the legend, though we won't explicitly show a legend here, it's good practice.
gdf.plot(ax=ax, markersize=100, color='red', alpha=0.7, label='Alien Invasion Sites')

# --- Enhancing the Plot ---

# Set the title of the plot.
ax.set_title('Hypothetical Alien Invasion Patterns', fontsize=18)

# Remove axis labels, as they are not very informative for a world map.
ax.set_xticks([])
ax.set_yticks([])

# Optional: Set the limits of the map to focus on specific regions if needed.
# For a world map, it's often best to let it default or manually adjust if you have a specific focus.
# ax.set_xlim([-180, 180])
# ax.set_ylim([-90, 90])

# Display the plot.
# This command renders the figure we've been building.
plt.show()

# --- Example Usage ---
# The code above directly executes the visualization.
# If you were to run this script, it would generate and display the map.
# You can modify the 'invasion_data' dictionary with your own simulated (or real) data
# to see how different patterns emerge. For instance, adding more invasions in a
# particular region would make that region appear denser with red dots.

# For a more advanced example, you could:
# 1. Read data from a CSV file using `pd.read_csv('invasions.csv')`.
# 2. Color-code invasion points by 'intensity' using the `column` and `cmap` arguments in `gdf.plot()`.
# 3. Add tooltips or interactive elements if using libraries like `plotly` or `folium`.