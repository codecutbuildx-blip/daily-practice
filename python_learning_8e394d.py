# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art
# using recursion and the Python Turtle graphics module.
# We will focus on the concept of self-similarity, a key characteristic of fractals,
# and how to implement it using a recursive function.

import turtle

# --- Configuration ---
# Setting up the screen for our artwork
screen = turtle.Screen()
screen.setup(width=800, height=700)  # Set the size of the drawing window
screen.bgcolor("black")            # Set the background color to black for a dramatic effect
screen.title("Recursive Fractal Art") # Title for our window

# Create a turtle object to draw with
artist = turtle.Turtle()
artist.speed(0)          # Set the fastest drawing speed (0 is the fastest)
artist.pensize(2)        # Make the pen a bit thicker for better visibility
artist.color("cyan")     # Set the drawing color to cyan

# --- Recursive Function for Fractal Generation ---

def draw_fractal(t, length, level, angle):
    """
    Recursively draws a fractal pattern.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        length (int): The current length of the line segment to draw.
        level (int): The current recursion level. Controls complexity.
        angle (int): The angle (in degrees) for branching.
    """
    # Base Case: When we reach the maximum recursion level, stop drawing.
    # This prevents infinite recursion and makes the fractal finite.
    if level == 0:
        # Draw a small line segment at the end of a branch.
        # This helps to visualize the termination points of the recursion.
        t.forward(length)
        t.backward(length) # Move back to the starting point of this segment
        return # Exit the function for this branch

    # Recursive Step: If not at the base case, draw the fractal by
    # breaking it down into smaller, similar sub-problems.

    # 1. Draw the main branch of the current segment.
    t.forward(length)

    # 2. Branch 1: Turn left and draw a smaller version of the fractal.
    t.left(angle)
    # Recursively call draw_fractal with reduced length and level.
    # We make the length smaller (length * 0.7) and decrease the level by 1.
    draw_fractal(t, length * 0.7, level - 1, angle)

    # 3. Branch 2: Turn right to return to the original direction and draw another fractal.
    # We turn right by twice the angle because we previously turned left by 'angle'.
    # This brings us back to the orientation of the main branch.
    t.right(angle * 2)
    # Recursively call draw_fractal for the second branch.
    draw_fractal(t, length * 0.7, level - 1, angle)

    # 4. Return to the starting position of this segment.
    # After drawing both branches, we need to move the turtle back to
    # where it started for this particular call. This allows other branches
    # to be drawn correctly from the same parent branch.
    t.left(angle) # Turn back to the original direction of the segment
    t.backward(length) # Move back along the segment

# --- Example Usage ---

# Positioning the turtle for the start of the fractal.
# We start at the bottom center of the screen, pointing upwards.
artist.penup()          # Lift the pen so it doesn't draw while moving
artist.goto(0, -250)    # Move to a starting Y-coordinate
artist.pendown()        # Put the pen down to start drawing
artist.left(90)         # Point the turtle upwards (90 degrees)

# Define parameters for the fractal.
initial_length = 100    # The length of the initial "trunk"
recursion_level = 9     # How many times the pattern repeats (higher = more complex)
branching_angle = 25    # The angle between branches

# Call the recursive function to generate the fractal art.
print("Generating fractal... this might take a moment!")
draw_fractal(artist, initial_length, recursion_level, branching_angle)
print("Fractal generation complete!")

# Keep the window open until it's manually closed.
screen.mainloop()