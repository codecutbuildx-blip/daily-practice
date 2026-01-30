# Fractal Art with Recursion and Turtle Graphics

# Learning Objective:
# This tutorial will teach you how to generate mesmerizing fractal art
# using the power of recursion and the built-in Python turtle graphics module.
# We will focus on understanding how recursive functions can be used to
# create self-similar patterns, a hallmark of fractals.

import turtle

# --- Configuration ---
# These are global settings for our fractal generation.
# Changing these values will affect the appearance of the fractal.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_SPEED = 0  # 0 is the fastest, 1-10 are progressively slower
PEN_SIZE = 2       # Thickness of the lines drawn
BACKGROUND_COLOR = "black" # Color of the drawing screen
PEN_COLOR = "cyan"     # Color of the lines (our fractal)
INITIAL_LENGTH = 200   # The starting length of the main line segments
RECURSION_DEPTH = 6    # How many levels of recursion to apply
ANGLE = 90             # The angle for turning at each step

# --- The Recursive Fractal Function ---

def draw_fractal(t, length, depth):
    """
    This is the core recursive function that draws the fractal.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the line segment to draw.
        depth (int): The current recursion depth. This tells us how many
                     more levels of recursion we have left.

    The 'why' behind recursion here:
    Fractals are characterized by self-similarity – they look the same
    at different scales. Recursion is a natural fit for this because
    a recursive function calls itself with smaller versions of the problem.
    In this case, we're drawing a line segment (length) and then, at its
    endpoints, we're drawing smaller versions of the same pattern.
    """

    # Base Case: The stopping condition for the recursion.
    # When the depth reaches 0, we stop drawing further branches.
    # This is crucial to prevent infinite recursion and stack overflow errors.
    if depth == 0:
        # For a simple fractal like this, we might just draw a tiny dot
        # or simply do nothing at the deepest level.
        # Here, we'll just return to stop this branch of recursion.
        return

    # --- Drawing the current segment ---
    # Move the turtle forward by the specified length.
    t.forward(length)

    # --- Recursive Steps ---
    # This is where the fractal magic happens!
    # We make a copy of the current length and reduce it for the next level.
    next_length = length * 0.7 # We make the next segment 70% of the current length.
                               # This scaling factor is key to how the fractal appears.

    # 1. Draw the left branch:
    # Turn left by the specified angle.
    t.left(ANGLE)
    # Recursively call draw_fractal for the left branch.
    # We pass the reduced length and the decremented depth.
    # depth - 1 means we've used up one level of recursion.
    draw_fractal(t, next_length, depth - 1)

    # 2. Return to the branching point and draw the right branch:
    # Turn right to face the original direction before the left turn.
    t.right(ANGLE * 2) # We need to turn right by twice the angle to get to the right side.
    # Recursively call draw_fractal for the right branch.
    draw_fractal(t, next_length, depth - 1)

    # 3. Return to the branching point and draw the backward segment (optional for some fractals)
    # Turn left to face the original direction again.
    t.left(ANGLE)
    # Move back to the starting position of this segment. This is important
    # so that when the function returns to its caller, the turtle is in the
    # correct position to draw the next part of the pattern.
    t.backward(length)

# --- Setup the Turtle Environment ---
def setup_turtle():
    """
    Initializes the turtle screen and the turtle object.
    Sets up basic properties like speed, size, and color.
    """
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Mesmerizing Recursive Fractal Art")

    artist = turtle.Turtle()
    artist.speed(DRAWING_SPEED)
    artist.pensize(PEN_SIZE)
    artist.color(PEN_COLOR)
    artist.penup() # Lift the pen to move to the starting position without drawing.

    # Move the turtle to the bottom center of the screen to start drawing upwards.
    artist.goto(0, -SCREEN_HEIGHT // 2 + 50) # Adjust Y slightly to avoid drawing off the bottom edge.
    artist.pendown() # Put the pen down to start drawing.
    artist.left(90) # Point the turtle upwards.

    return artist

# --- Main Execution Block ---
if __name__ == "__main__":
    # This block ensures the code runs only when the script is executed directly.

    # 1. Set up the drawing environment.
    turtle_object = setup_turtle()

    # 2. Start the fractal generation.
    # We call our recursive function with the initial length and the maximum depth.
    print(f"Generating fractal with depth {RECURSION_DEPTH} and initial length {INITIAL_LENGTH}...")
    draw_fractal(turtle_object, INITIAL_LENGTH, RECURSION_DEPTH)

    # 3. Keep the window open until it's manually closed.
    print("Fractal generation complete. Close the window to exit.")
    turtle_object.hideturtle() # Hide the turtle icon after drawing.
    turtle.done() # This command keeps the turtle graphics window open.

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., fractal_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python fractal_art.py
#
# Experiment by changing the global variables at the top of the script, such as:
# - RECURSION_DEPTH: Controls the complexity and detail. Higher values take longer.
# - INITIAL_LENGTH: Affects the overall size of the fractal.
# - ANGLE: Changes the branching pattern. Try 60, 45, or even more dynamic angles.
# - PEN_COLOR and BACKGROUND_COLOR: For different visual styles.