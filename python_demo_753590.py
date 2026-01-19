# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art patterns
# using the power of recursion and Python's built-in Turtle graphics library.
# We will focus on understanding how recursive functions can create self-similar
# and complex designs by breaking down a problem into smaller, identical sub-problems.

import turtle

# --- Configuration ---
# These constants allow easy modification of the fractal's appearance.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INITIAL_SPEED = 0  # 0 is the fastest speed for Turtle
PEN_COLOR = "blue"
BACKGROUND_COLOR = "black"
PEN_SIZE = 1

# --- Recursive Fractal Function ---
def draw_fractal(t, order, size):
    """
    Recursively draws a fractal pattern.

    Args:
        t (turtle.Turtle): The Turtle object to draw with.
        order (int): The current level of recursion. This determines the detail.
        size (float): The current length of the line segment to draw.
    """
    if order == 0:
        # Base Case: When the order reaches 0, we stop recursing.
        # This is the simplest part of the fractal, a single line segment.
        t.forward(size)
        return

    # Recursive Step: If order is greater than 0, we break down the current
    # drawing task into smaller, identical tasks.

    # 1. Draw the first part of the fractal.
    # We divide the current size by 3 for the next smaller segment.
    draw_fractal(t, order - 1, size / 3)

    # 2. Turn left by 60 degrees. This prepares for the next segment.
    t.left(60)

    # 3. Draw the second part of the fractal.
    draw_fractal(t, order - 1, size / 3)

    # 4. Turn right by 120 degrees. This is a combination of turning back
    # from the left turn and then turning right for the next segment.
    t.right(120)

    # 5. Draw the third part of the fractal.
    draw_fractal(t, order - 1, size / 3)

    # 6. Turn left by 60 degrees. This brings us back to the original heading.
    t.left(60)

    # 7. Draw the fourth part of the fractal.
    draw_fractal(t, order - 1, size / 3)

# --- Main Execution ---
if __name__ == "__main__":
    # Initialize the screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Recursive Fractal Art")

    # Create a Turtle object
    artist = turtle.Turtle()
    artist.speed(INITIAL_SPEED)
    artist.color(PEN_COLOR)
    artist.pensize(PEN_SIZE)

    # Position the turtle to start drawing from the center-left
    # This helps in keeping the fractal within the screen boundaries.
    artist.penup()  # Lift the pen so we don't draw while moving
    artist.goto(-SCREEN_WIDTH / 3, 0)  # Move to a starting position
    artist.pendown() # Put the pen down to start drawing

    # --- Example Usage ---
    # You can change these values to create different fractal patterns.
    # 'fractal_order' controls the level of detail. Higher numbers mean more detail
    # but also more computation.
    # 'initial_size' controls the overall scale of the fractal.
    fractal_order = 4
    initial_size = 400

    # Call the recursive function to draw the fractal
    draw_fractal(artist, fractal_order, initial_size)

    # Hide the turtle cursor after drawing for a cleaner look
    artist.hideturtle()

    # Keep the window open until it's manually closed
    screen.mainloop()