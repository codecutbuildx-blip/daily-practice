# Learning Objective:
# This tutorial teaches how to visualize and analyze patterns in simulated alien
# invasion data using Pygame for visualization and basic Python data manipulation.
# We'll focus on understanding the distribution and movement of invaders.

import pygame
import random
import collections

# --- Constants for Visualization ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
INVADER_COLOR = (0, 255, 0)   # Green
INVADER_SIZE = 5
FPS = 30

# --- Data Simulation Parameters ---
NUM_INVADERS = 100
INITIAL_INVADER_SPREAD = 50 # How far from the center invaders start
MOVE_SPEED = 1 # Pixels per frame invaders move
MAX_MOVEMENT_AREA_X = SCREEN_WIDTH * 0.8 # Limit movement horizontally
MAX_MOVEMENT_AREA_Y = SCREEN_HEIGHT * 0.7 # Limit movement vertically

# --- Data Structure for Invaders ---
# We'll use a list of dictionaries. Each dictionary represents an invader
# and stores its current position (x, y) and its unique ID.
# Using a dictionary allows us to easily add more properties later if needed.
invaders = []

def create_invaders():
    """
    Simulates the initial placement of invaders.
    This function populates the 'invaders' list with starting positions.
    """
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 4 # Start invaders higher up on the screen

    for i in range(NUM_INVADERS):
        # Randomly offset initial positions from the center
        # This creates a dispersed starting pattern.
        start_x = center_x + random.randint(-INITIAL_INVADER_SPREAD, INITIAL_INVADER_SPREAD)
        start_y = center_y + random.randint(-INITIAL_INVADER_SPREAD, INITIAL_INVADER_SPREAD)

        # Ensure invaders start within reasonable screen bounds
        start_x = max(0, min(start_x, SCREEN_WIDTH - 1))
        start_y = max(0, min(start_y, SCREEN_HEIGHT - 1))

        invaders.append({"id": i, "x": start_x, "y": start_y})

def move_invaders():
    """
    Simulates the movement of invaders.
    This function updates the positions of each invader in the 'invaders' list.
    We'll make them move downwards and slightly horizontally to simulate a
    typical invasion pattern.
    """
    for invader in invaders:
        # Randomly decide horizontal movement direction (left or right)
        direction_x = random.choice([-1, 0, 1])
        # Invaders primarily move downwards
        direction_y = 1

        # Update position based on direction and speed
        invader["x"] += direction_x * MOVE_SPEED
        invader["y"] += direction_y * MOVE_SPEED

        # Keep invaders within a defined movement area to prevent them from
        # going off-screen too quickly or too far. This helps in observing patterns.
        invader["x"] = max(0, min(invader["x"], MAX_MOVEMENT_AREA_X))
        invader["y"] = max(0, min(invader["y"], MAX_MOVEMENT_AREA_Y))

def analyze_invader_distribution():
    """
    Analyzes the current distribution of invaders.
    This function demonstrates basic data analysis by counting invaders in
    different horizontal sections of the screen. This can reveal if invaders
    are concentrating in certain areas.
    """
    # We divide the screen width into 10 bins for analysis.
    # This is a simple way to segment the space and count invaders within each segment.
    bins = collections.defaultdict(int) # A dictionary that defaults to 0 for new keys

    for invader in invaders:
        # Calculate which bin the invader falls into based on its x-coordinate.
        # For example, if SCREEN_WIDTH is 800 and we have 10 bins, each bin
        # represents 80 pixels in width.
        bin_index = int(invader["x"] // (SCREEN_WIDTH / 10))
        bins[bin_index] += 1 # Increment the count for that bin

    print("--- Invader Distribution Analysis ---")
    # Print the count for each bin.
    for i in range(10):
        print(f"Horizontal Bin {i} ({i*80}-{ (i+1)*80 }px): {bins[i]} invaders")
    print("-----------------------------------")

def draw_invaders(screen):
    """
    Draws all invaders onto the Pygame screen.
    This function iterates through the 'invaders' list and draws a small
    rectangle for each invader at its current (x, y) coordinates.
    """
    for invader in invaders:
        # Draw a rectangle representing the invader.
        # (x, y) is the top-left corner of the rectangle.
        # INVADER_SIZE is both the width and height of the rectangle.
        pygame.draw.rect(screen, INVADER_COLOR, (invader["x"], invader["y"], INVADER_SIZE, INVADER_SIZE))

def main():
    """
    The main function to run the Pygame simulation and visualization.
    This sets up the Pygame window, initializes invaders, and runs the game loop.
    The game loop handles events, updates game state (invader positions),
    analyzes data, and draws everything to the screen.
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulated Alien Invasion")
    clock = pygame.time.Clock()

    # Create initial invaders
    create_invaders()

    running = True
    frame_count = 0 # To trigger analysis periodically

    # --- The Game Loop ---
    # This loop runs continuously until the user quits the application.
    while running:
        # --- Event Handling ---
        # Check for user input and window events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the close button
                running = False # End the loop

        # --- Game State Updates ---
        # Move invaders to simulate their invasion progress.
        move_invaders()

        # --- Data Analysis ---
        # Analyze distribution every 60 frames (twice a second at 30 FPS).
        # This demonstrates how to extract insights from the simulation data.
        frame_count += 1
        if frame_count % 60 == 0:
            analyze_invader_distribution()

        # --- Drawing ---
        # Clear the screen with the background color.
        screen.fill(BACKGROUND_COLOR)
        # Draw all the invaders at their updated positions.
        draw_invaders(screen)

        # --- Display Update ---
        # Flip the display to show what we've drawn.
        pygame.display.flip()

        # --- Frame Rate Control ---
        # Limit the loop to run at FPS frames per second.
        # This ensures consistent simulation speed.
        clock.tick(FPS)

    # Quit Pygame when the loop ends
    pygame.quit()

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that main() is called only when the script is executed directly.
    # It's a standard Python practice.
    main()