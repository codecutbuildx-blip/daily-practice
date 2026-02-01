# Learning Objective:
# This tutorial will teach you how to generate mesmerizing fractal art
# using the power of recursion and Python's Turtle graphics module.
# We will focus on understanding how recursive functions can create
# complex patterns from simple repeating rules.

import turtle

# --- Configuration ---
# We'll use a turtle to draw. Let's set up its speed and color.
# 'fastest' is 0, 'fast' is 10. A speed of 0 makes drawing much quicker.
turtle.speed(0)
turtle.pencolor("blue")  # Set the pen color for drawing

# --- The Fractal Function (Recursive) ---

def draw_fractal(t, order, size):
    """
    This is the core recursive function that draws our fractal.
    It takes a turtle object 't', the current 'order' of the fractal,
    and the 'size' of the current line segment.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        order (int): The depth of recursion. Higher order means more detail.
        size (float): The length of the current line segment to draw.
    """

    # Base Case: This is crucial for recursion.
    # When the 'order' reaches 0, we stop drawing.
    # This prevents infinite recursion and provides the smallest element
    # of our fractal.
    if order == 0:
        t.forward(size)  # Draw a simple line segment
        return          # Exit the function, stopping this branch of recursion

    # Recursive Step:
    # If the order is greater than 0, we need to break down the current
    # line segment into smaller, similar shapes.
    else:
        # We divide the current 'size' by 3 for the next smaller segments.
        # The idea is to repeat the same pattern at a smaller scale.
        new_size = size / 3

        # Draw the first segment
        draw_fractal(t, order - 1, new_size)

        # Turn left by 60 degrees. This creates the angle for our fractal.
        t.left(60)

        # Draw the second segment
        draw_fractal(t, order - 1, new_size)

        # Turn right by 120 degrees. Notice we turn further right than we turned left.
        # This is to bring the turtle back to the original orientation after drawing
        # the second segment and to prepare for the third segment.
        t.right(120)

        # Draw the third segment
        draw_fractal(t, order - 1, new_size)

        # Turn left by 60 degrees. This returns the turtle to its original orientation
        # before this recursive call, so that subsequent calls in the parent
        # function continue from the correct heading.
        t.left(60)

        # Draw the fourth segment
        draw_fractal(t, order - 1, new_size)

# --- Example Usage ---

if __name__ == "__main__":
    # Create a screen object to manage the drawing window.
    screen = turtle.Screen()
    screen.setup(width=800, height=600) # Set the size of the drawing window
    screen.bgcolor("white") # Set the background color

    # Create a turtle object. This is what will do the drawing.
    my_turtle = turtle.Turtle()
    my_turtle.penup() # Lift the pen so we don't draw while positioning
    my_turtle.goto(-200, 0) # Move the turtle to a starting position on the left
    my_turtle.pendown() # Put the pen down to start drawing

    # --- Customize your fractal ---
    fractal_order = 4      # How detailed do you want the fractal? (Try 1, 2, 3, 4, 5)
    initial_size = 600     # The starting length of the main shape

    # Call the recursive function to draw the fractal.
    # The initial order is set, and the turtle starts drawing.
    draw_fractal(my_turtle, fractal_order, initial_size)

    # Keep the window open until it's closed manually.
    screen.mainloop()