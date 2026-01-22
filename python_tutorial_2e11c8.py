# Dungeon Generation Tutorial: Perlin Noise & Grid Algorithms
#
# Learning Objective:
# This tutorial demonstrates how to generate infinite, playable dungeons
# using a combination of Perlin noise for organic terrain and grid-based
# algorithms for structure and connectivity. We'll focus on creating
# a simple 2D grid where '0' represents a floor and '1' represents a wall.
# This provides a foundation for more complex dungeon generation.

import random
import opensimplex  # A fast, robust Perlin noise implementation

# --- Configuration ---
# Determines the dimensions of our dungeon grid.
GRID_WIDTH = 64
GRID_HEIGHT = 64

# Controls the "smoothness" and scale of the Perlin noise.
# Higher values mean larger, smoother features.
PERLIN_SCALE = 30.0

# Adjusts the threshold for deciding if a point becomes a wall or floor.
# Higher values lead to more walls (smaller open spaces).
WALL_THRESHOLD = 0.45

# Controls how aggressively we carve out open spaces.
# Higher values make openings larger and more connected.
MIN_ROOM_SIZE = 5

# Seed for reproducible random generation (useful for debugging).
# Set to None for truly random generation each time.
RANDOM_SEED = 12345

# --- Helper Functions ---

def initialize_random_seed():
    """
    Initializes the random number generator with a specific seed if provided.
    This ensures that the same "random" dungeon is generated each time
    the seed is the same, which is great for testing and debugging.
    If no seed is provided, the generator will be truly random.
    """
    if RANDOM_SEED is not None:
        random.seed(RANDOM_SEED)
        opensimplex.seed(RANDOM_SEED) # Also seed the noise generator for consistency

# --- Core Dungeon Generation Logic ---

def generate_perlin_noise_grid(width, height, scale):
    """
    Generates a 2D grid of Perlin noise values.

    Args:
        width (int): The width of the grid.
        height (int): The height of the grid.
        scale (float): The scaling factor for the Perlin noise.
                       Larger values create larger, smoother features.

    Returns:
        list[list[float]]: A 2D list representing the grid with noise values.
    """
    noise_grid = [[0.0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            # Sample the Perlin noise at the current (x, y) coordinate.
            # We divide by scale to control the frequency/size of noise features.
            # opensimplex.noise2d returns values typically between -1.0 and 1.0.
            noise_value = opensimplex.noise2d(x / scale, y / scale)
            noise_grid[y][x] = noise_value
    return noise_grid

def create_initial_grid(noise_grid, wall_threshold):
    """
    Converts the Perlin noise grid into a binary grid (walls and floors).

    Args:
        noise_grid (list[list[float]]): The grid of Perlin noise values.
        wall_threshold (float): The threshold for determining walls.
                                Values above this become walls, below become floors.

    Returns:
        list[list[int]]: A 2D list representing the dungeon grid (0=floor, 1=wall).
    """
    height = len(noise_grid)
    width = len(noise_grid[0])
    dungeon_grid = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # If the noise value is greater than our threshold, it's a wall.
            # Otherwise, it's a floor. This creates organic shapes.
            if noise_grid[y][x] > wall_threshold:
                dungeon_grid[y][x] = 1  # 1 represents a wall
            else:
                dungeon_grid[y][x] = 0  # 0 represents a floor
    return dungeon_grid

def find_connected_components(grid):
    """
    Finds all distinct connected regions of floor tiles.
    This is a precursor to ensuring connectivity.

    Args:
        grid (list[list[int]]): The dungeon grid (0=floor, 1=wall).

    Returns:
        list[list[tuple[int, int]]]: A list where each inner list contains
                                     coordinates of tiles belonging to a
                                     single connected component.
    """
    height = len(grid)
    width = len(grid[0])
    visited = [[False for _ in range(width)] for _ in range(height)]
    components = []

    def bfs(start_x, start_y):
        """Breadth-First Search to find all connected floor tiles."""
        component = []
        queue = [(start_x, start_y)]
        visited[start_y][start_x] = True

        while queue:
            x, y = queue.pop(0)
            component.append((x, y))

            # Check neighbors (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                # Check bounds and if it's a floor tile and not visited
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
        return component

    # Iterate through the grid to find unvisited floor tiles
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 0 and not visited[y][x]:
                components.append(bfs(x, y))
    return components

def connect_dungeons(grid, min_room_size):
    """
    Ensures all floor tiles are part of at least one large enough room.
    This is a simplified connectivity algorithm. More robust algorithms
    might involve explicitly carving tunnels.

    Args:
        grid (list[list[int]]): The dungeon grid (0=floor, 1=wall).
        min_room_size (int): The minimum number of tiles a region must have
                             to be considered a valid "room".

    Returns:
        list[list[int]]: The modified dungeon grid with isolated small areas removed.
    """
    components = find_connected_components(grid)
    height = len(grid)
    width = len(grid[0])

    # Iterate through all components found
    for component in components:
        # If a component is too small, convert its tiles to walls.
        # This helps to remove tiny, isolated pockets that might not be playable.
        if len(component) < min_room_size:
            for x, y in component:
                grid[y][x] = 1 # Turn small isolated areas into walls
    return grid

def generate_dungeon(width=GRID_WIDTH, height=GRID_HEIGHT, scale=PERLIN_SCALE, wall_threshold=WALL_THRESHOLD, min_room_size=MIN_ROOM_SIZE):
    """
    Generates a complete dungeon grid using Perlin noise and grid algorithms.

    Args:
        width (int): The desired width of the dungeon.
        height (int): The desired height of the dungeon.
        scale (float): The scaling factor for Perlin noise.
        wall_threshold (float): The threshold for wall/floor determination.
        min_room_size (int): The minimum size for a playable room.

    Returns:
        list[list[int]]: The generated dungeon grid (0=floor, 1=wall).
    """
    initialize_random_seed() # Ensure randomness is set up

    # 1. Generate raw Perlin noise values across the grid.
    noise_grid = generate_perlin_noise_grid(width, height, scale)

    # 2. Convert noise values to a binary grid (walls and floors).
    dungeon_grid = create_initial_grid(noise_grid, wall_threshold)

    # 3. Clean up small, isolated floor areas by turning them into walls.
    # This is a simplified connectivity step to ensure playable spaces.
    dungeon_grid = connect_dungeons(dungeon_grid, min_room_size)

    return dungeon_grid

# --- Example Usage ---

def print_dungeon(dungeon_grid):
    """
    Prints a visual representation of the dungeon grid.
    '#' for walls, '.' for floors.
    """
    for row in dungeon_grid:
        print("".join(['#' if tile == 1 else '.' for tile in row]))

if __name__ == "__main__":
    print("Generating a sample dungeon...")
    # Generate a dungeon with default settings
    my_dungeon = generate_dungeon()

    # Print the generated dungeon to the console
    print_dungeon(my_dungeon)

    print("\nGenerating another dungeon with different settings (larger scale, higher threshold)...")
    # Generate a new dungeon with modified parameters for a different look
    larger_dungeon = generate_dungeon(
        width=40,
        height=20,
        scale=50.0, # Larger scale means bigger, smoother features
        wall_threshold=0.5, # Higher threshold means more walls
        min_room_size=10 # Require larger rooms
    )
    print_dungeon(larger_dungeon)