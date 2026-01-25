# Fractal Art Generation with Recursion

# Learning Objective:
# This tutorial will teach you how to programmatically generate intricate fractal art
# using the concept of recursion and basic Python graphics.
# We will focus on understanding how a recursive function can break down a complex
# problem into smaller, self-similar sub-problems to create beautiful, detailed patterns.
# This example will generate a Sierpinski Triangle.

import turtle  # The turtle module provides a simple graphics canvas.

def draw_triangle(points, color, my_turtle):
    """
    Draws a filled triangle given three points and a color.
    This is a helper function to draw the basic shapes in our fractal.
    """
    my_turtle.fillcolor(color)  # Set the fill color for the triangle.
    my_turtle.up()  # Lift the pen to move without drawing.
    my_turtle.goto(points[0])  # Move to the first point.
    my_turtle.down()  # Put the pen down to start drawing.
    my_turtle.begin_fill()  # Start filling the shape.
    my_turtle.goto(points[1])  # Draw to the second point.
    my_turtle.goto(points[2])  # Draw to the third point.
    my_turtle.goto(points[0])  # Draw back to the first point to close the triangle.
    my_turtle.end_fill()  # Finish filling the shape.

def get_midpoint(p1, p2):
    """
    Calculates the midpoint between two points.
    This is a fundamental operation for generating the smaller triangles in our fractal.
    A midpoint is found by averaging the x and y coordinates of the two points.
    """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, level, my_turtle):
    """
    Recursively draws the Sierpinski triangle.

    Args:
        points: A list of three (x, y) tuples representing the vertices of the current triangle.
        level: The current level of recursion. This determines the detail of the fractal.
               Higher levels mean more recursion and more detail.
        my_turtle: The turtle object used for drawing.
    """
    # Define colors for different levels of recursion. This makes the fractal visually appealing.
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']

    # Draw the current triangle. The color is determined by the recursion level.
    draw_triangle(points, colormap[level % len(colormap)], my_turtle)

    # Base Case for Recursion:
    # If the level of recursion is 0, we stop. This is crucial to prevent infinite recursion.
    if level > 0:
        # Recursive Step:
        # If we are not at the base case, we create three smaller triangles.
        # Each smaller triangle is formed by taking two original vertices and the midpoint
        # of the opposite side. This creates self-similarity.

        # Top triangle: uses top vertex and midpoints of bottom two sides.
        sierpinski([points[0], get_midpoint(points[0], points[1]), get_midpoint(points[0], points[2])],
                   level - 1, my_turtle)

        # Left triangle: uses left vertex and midpoints of top and bottom-left sides.
        sierpinski([points[1], get_midpoint(points[0], points[1]), get_midpoint(points[1], points[2])],
                   level - 1, my_turtle)

        # Right triangle: uses right vertex and midpoints of top and bottom-right sides.
        sierpinski([points[2], get_midpoint(points[0], points[2]), get_midpoint(points[1], points[2])],
                   level - 1, my_turtle)

# --- Example Usage ---

if __name__ == "__main__":
    # Initialize the turtle screen.
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Set the dimensions of the drawing window.
    screen.title("Sierpinski Triangle Fractal") # Set the window title.
    screen.tracer(0) # Turn off screen updates to speed up drawing.

    # Create a turtle object.
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)  # Set the fastest drawing speed.
    my_turtle.hideturtle()  # Hide the turtle cursor for a cleaner look.

    # Define the initial vertices of the largest triangle.
    # These points define the bounding box for our fractal.
    initial_points = [[-200, -100], [0, 200], [200, -100]]

    # Define the desired level of recursion (complexity).
    # A higher number will result in a more detailed and intricate fractal.
    recursion_level = 4

    # Start the recursive drawing process.
    sierpinski(initial_points, recursion_level, my_turtle)

    # Update the screen to show the completed fractal.
    screen.update()

    # Keep the window open until it's manually closed.
    screen.mainloop()