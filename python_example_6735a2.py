# Fractal Art with Recursion and Python Turtle

# Learning Objective:
# This tutorial will teach you how to create beautiful fractal art using the concept of recursion
# and Python's built-in `turtle` module. We will focus on understanding how a recursive function
# breaks down a complex problem into smaller, self-similar sub-problems to generate intricate patterns.

import turtle
import random # Importing random for potentially adding variations later, though not strictly used in the core example

def setup_screen(width=800, height=600, bgcolor="black"):
    """
    Sets up the turtle screen for drawing.
    Args:
        width (int): The width of the drawing window.
        height (int): The height of the drawing window.
        bgcolor (str): The background color of the drawing window.
    Returns:
        turtle.Screen: The configured turtle screen object.
    """
    screen = turtle.Screen() # Create a screen object to control the window.
    screen.setup(width=width, height=height) # Set the dimensions of the window.
    screen.bgcolor(bgcolor) # Set the background color.
    screen.title("Recursive Fractal Art") # Set the title of the window.
    return screen

def setup_turtle(speed=0, pensize=1, color="white"):
    """
    Sets up the turtle for drawing.
    Args:
        speed (int): The drawing speed (0 is fastest).
        pensize (int): The thickness of the drawing line.
        color (str): The color of the drawing line.
    Returns:
        turtle.Turtle: The configured turtle object.
    """
    artist = turtle.Turtle() # Create a turtle object, which is our drawing pen.
    artist.speed(speed) # Set the drawing speed. 0 is the fastest, 10 is fast, 1 is slow.
    artist.pensize(pensize) # Set the thickness of the pen.
    artist.color(color) # Set the color of the pen.
    artist.penup() # Lift the pen so it doesn't draw while moving to the starting position.
    artist.hideturtle() # Hide the turtle icon to make the artwork cleaner.
    return artist

def draw_sierpinski_triangle(t, order, size, position):
    """
    Recursively draws a Sierpinski triangle.
    This is a classic example of a fractal where each triangle is made up of three smaller,
    identical triangles. The 'order' parameter controls the level of detail.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        order (int): The current recursion depth or level of detail.
                     A higher order means more intricate patterns.
        size (float): The side length of the current triangle.
        position (tuple): The (x, y) coordinates for the bottom-left corner of the triangle.
    """
    if order == 0:
        # Base case: When the order is 0, we draw a simple filled triangle.
        # This is the smallest building block of our fractal.
        t.goto(position) # Move the turtle to the starting position without drawing.
        t.pendown() # Put the pen down to start drawing.
        t.begin_fill() # Start filling the shape with color.
        for _ in range(3):
            t.forward(size) # Move forward by 'size' units.
            t.left(120) # Turn left by 120 degrees to form a corner of the triangle.
        t.end_fill() # Stop filling the shape.
        t.penup() # Lift the pen again.
    else:
        # Recursive step: For orders greater than 0, we divide the current triangle
        # into three smaller triangles and recursively call this function for each.
        # The size of each sub-triangle is half of the current triangle's size.

        # 1. Draw the bottom-left sub-triangle
        draw_sierpinski_triangle(t, order - 1, size / 2, position)

        # 2. Draw the bottom-right sub-triangle
        # The new position is shifted to the right by 'size / 2'.
        new_pos_right = (position[0] + size / 2, position[1])
        draw_sierpinski_triangle(t, order - 1, size / 2, new_pos_right)

        # 3. Draw the top sub-triangle
        # The new position is shifted up and to the right by 'size / 2'.
        # We move horizontally by 'size / 4' and vertically by 'size * sqrt(3) / 4' (height of equilateral triangle).
        # For simplicity and visual correctness, we can approximate this by moving
        # to the midpoint of the top edge of the bottom two triangles.
        new_pos_top = (position[0] + size / 4, position[1] + (size / 2) * (3**0.5 / 2))
        draw_sierpinski_triangle(t, order - 1, size / 2, new_pos_top)

# --- Example Usage ---
if __name__ == "__main__":
    # Setup the screen and turtle
    screen = setup_screen()
    artist = setup_turtle(color="red") # Use red for a more striking fractal

    # Define fractal parameters
    fractal_order = 4  # How many levels of recursion. Higher means more detail.
    triangle_size = 300 # The side length of the largest triangle.
    # Starting position for the bottom-left corner of the initial triangle.
    # We center the fractal by adjusting the x-coordinate.
    start_x = -triangle_size / 2
    start_y = -triangle_size * (3**0.5) / 4 # Adjust y to center the base
    starting_position = (start_x, start_y)

    # Call the recursive function to draw the fractal
    draw_sierpinski_triangle(artist, fractal_order, triangle_size, starting_position)

    # Keep the window open until it's manually closed.
    screen.mainloop()
# The `if __name__ == "__main__":` block ensures that this code only runs
# when the script is executed directly, not when it's imported as a module.
# This is a common Python best practice.