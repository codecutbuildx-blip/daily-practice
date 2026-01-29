################################################################################
# Learning Objective:
# This tutorial demonstrates how to generate infinite, evolving 2D terrain
# using Perlin noise. It combines Perlin noise generation with basic game
# loop concepts (updating and rendering) to create a dynamic and visually
# interesting terrain that can be explored.
#
# Concepts Covered:
# 1. Perlin Noise: Understanding how Perlin noise generates natural-looking
#    randomness that can be used for terrain heightmaps.
# 2. Game Loop: Implementing a simple game loop to continuously update
#    and render the terrain, allowing for 'evolution'.
# 3. Offset/Scrolling: Moving through the infinite terrain by changing an offset.
#
# Tools Used:
# - Perlin Noise Library: `noise` (install via pip: pip install noise)
# - Visualization: `pygame` (install via pip: pip install pygame)
################################################################################

# Import necessary libraries
import noise  # For Perlin noise generation
import pygame # For creating a window and drawing

# --- Configuration Constants ---
# These constants control the appearance and behavior of our terrain.
SCREEN_WIDTH = 800  # Width of the display window
SCREEN_HEIGHT = 600 # Height of the display window
TILE_SIZE = 10      # The size of each individual 'pixel' or tile in the terrain
SCALE = 100.0       # Controls the 'zoom' level of the Perlin noise.
OCTAVES = 6         # Number of noise layers to combine for detail. Higher = more detail.
PERSISTENCE = 0.5   # Amplitude multiplier for each octave. Lower = smoother terrain.
LACUNARITY = 2.0    # Frequency multiplier for each octave. Higher = more jagged terrain.
MOVE_SPEED = 5      # How fast we move through the terrain (in tiles per frame).

# --- Perlin Noise Setup ---
# We use a seed to make the generated terrain reproducible.
# Changing this seed will generate a completely different world.
SEED = 12345

# --- Game State Variables ---
# These variables will change during the game loop, representing the current state.
offset_x = 0.0 # Current horizontal position in the infinite terrain
offset_y = 0.0 # Current vertical position in the infinite terrain

def get_terrain_height(x: int, y: int) -> float:
    """
    Calculates the height of the terrain at a given coordinate using Perlin noise.

    Args:
        x: The x-coordinate in the world.
        y: The y-coordinate in the world.

    Returns:
        A float representing the height value (typically between -1.0 and 1.0).
    """
    # We use 'noise.pnoise2' for 2D Perlin noise.
    # `x / SCALE` and `y / SCALE` normalize the coordinates based on our desired zoom.
    # `octaves`, `persistence`, and `lacunarity` control the complexity of the noise.
    # `SEED` ensures the same terrain is generated if we restart with the same seed.
    return noise.pnoise2(
        x / SCALE,
        y / SCALE,
        octaves=OCTAVES,
        persistence=PERSISTENCE,
        lacunarity=LACUNARITY,
        base=SEED
    )

def map_height_to_color(height: float) -> tuple[int, int, int]:
    """
    Maps a Perlin noise height value to an RGB color for visualization.
    This simulates different terrain types (e.g., water, grass, mountains).

    Args:
        height: The Perlin noise height value (typically -1.0 to 1.0).

    Returns:
        An RGB tuple (red, green, blue) between 0 and 255.
    """
    # We scale and clamp the height to map it onto our color palette.
    # A simple gradient from blue (water) to green (grass) to brown/white (mountains).
    scaled_height = (height + 1) / 2  # Normalize height to 0.0 - 1.0

    if scaled_height < 0.3: # Water
        return (0, 0, int(200 * (1 - scaled_height / 0.3)))
    elif scaled_height < 0.6: # Grass
        green_level = int(100 + 155 * ((scaled_height - 0.3) / 0.3))
        return (0, green_level, 0)
    elif scaled_height < 0.8: # Rock/Dirt
        brown_level = int(100 + 155 * ((scaled_height - 0.6) / 0.2))
        return (int(139 - (scaled_height - 0.6) / 0.2 * 100), int(69 - (scaled_height - 0.6) / 0.2 * 20), int(0 + (scaled_height - 0.6) / 0.2 * 50))
    else: # Snow/Peaks
        white_level = int(255 * ((scaled_height - 0.8) / 0.2))
        return (white_level, white_level, white_level)

def create_terrain_surface(current_offset_x: float, current_offset_y: float) -> pygame.Surface:
    """
    Generates a Pygame Surface representing the terrain for the current view.

    Args:
        current_offset_x: The current horizontal offset for terrain generation.
        current_offset_y: The current vertical offset for terrain generation.

    Returns:
        A Pygame Surface containing the rendered terrain.
    """
    # Create a blank surface to draw on.
    terrain_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Iterate through each visible tile on the screen.
    for y in range(0, SCREEN_HEIGHT // TILE_SIZE):
        for x in range(0, SCREEN_WIDTH // TILE_SIZE):
            # Calculate the world coordinates for this tile.
            # We add the current offset to the tile's screen position.
            world_x = x * TILE_SIZE + int(current_offset_x)
            world_y = y * TILE_SIZE + int(current_offset_y)

            # Get the Perlin noise height for this world coordinate.
            height = get_terrain_height(world_x, world_y)

            # Map the height to a color.
            color = map_height_to_color(height)

            # Draw a rectangle (our tile) on the terrain surface.
            # The position is `(x * TILE_SIZE, y * TILE_SIZE)` in screen coordinates.
            pygame.draw.rect(
                terrain_surface,
                color,
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )
    return terrain_surface

# --- Main Game Loop ---
def main():
    """
    Initializes Pygame, sets up the display, and runs the main game loop.
    Handles user input for movement and continuously updates/renders the terrain.
    """
    pygame.init() # Initialize Pygame modules

    # Set up the display window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Infinite Evolving Terrain") # Set window title

    # Load a font for potential future text display (not used in this basic version)
    font = pygame.font.Font(None, 36)

    running = True # Game loop control flag
    while running:
        # --- Event Handling ---
        # Process all events that have occurred since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the close button
                running = False # Exit the game loop

        # --- Input Handling (Movement) ---
        # Get the state of all keyboard buttons.
        keys = pygame.key.get_pressed()
        # If the right arrow key is pressed, move the offset to the right.
        if keys[pygame.K_RIGHT]:
            offset_x += MOVE_SPEED
        # If the left arrow key is pressed, move the offset to the left.
        if keys[pygame.K_LEFT]:
            offset_x -= MOVE_SPEED
        # If the down arrow key is pressed, move the offset down.
        if keys[pygame.K_DOWN]:
            offset_y += MOVE_SPEED
        # If the up arrow key is pressed, move the offset up.
        if keys[pygame.K_UP]:
            offset_y -= MOVE_SPEED

        # --- Game State Updates ---
        # In this simple example, the 'evolution' is achieved by moving the offset.
        # As we move, different parts of the infinite Perlin noise field are sampled,
        # creating the illusion of a changing, vast world.

        # --- Rendering ---
        # Fill the screen with a background color (optional, but good practice).
        screen.fill((0, 0, 0)) # Black background

        # Generate the terrain surface for the current view.
        terrain_surface = create_terrain_surface(offset_x, offset_y)

        # Blit (draw) the generated terrain surface onto the main screen.
        screen.blit(terrain_surface, (0, 0)) # Draw at top-left corner of the screen

        # Update the full display Surface to the screen.
        pygame.display.flip()

    pygame.quit() # Uninitialize Pygame modules and exit

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that main() is called only when the script is executed directly.
    # It's the standard way to run the main part of a Python program.
    print("Starting the infinite terrain generator...")
    print(f"Screen resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Tile size: {TILE_SIZE}x{TILE_SIZE}")
    print("Use arrow keys to move around. Close the window to exit.")
    main()
    print("Application closed.")
################################################################################