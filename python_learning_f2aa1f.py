# Learning Objective:
# This tutorial will teach you how to visualize and interactively explore
# fractals using Python's Turtle graphics and the concept of recursion.
# We'll focus on creating a classic fractal: the Sierpinski Triangle.

import turtle
import sys

# Increase recursion depth for complex fractals.
# This is necessary because some fractals can have very deep recursion.
# Be cautious with very high numbers, as it can lead to stack overflow.
sys.setrecursionlimit(2000)

def draw_sierpinski(t, order, size):
    """
    Recursively draws a Sierpinski Triangle.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The current recursion depth (order of the fractal).
        size (float): The length of the base of the current triangle.
    """
    # Base case for the recursion:
    # If the order is 0, we draw a simple filled triangle.
    # This stops the recursion.
    if order == 0:
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    else:
        # Recursive step:
        # We divide the current triangle into four smaller triangles.
        # Three of these are Sierpinski triangles of the next lower order,
        # and one is the "hole" in the middle.

        # 1. Draw the bottom-left Sierpinski triangle.
        # This is a Sierpinski triangle with order-1 and half the size.
        draw_sierpinski(t, order - 1, size / 2)

        # 2. Move to the starting position for the bottom-right triangle.
        # We move right by half the size of the current triangle.
        t.forward(size / 2)

        # 3. Draw the bottom-right Sierpinski triangle.
        draw_sierpinski(t, order - 1, size / 2)

        # 4. Move to the starting position for the top triangle.
        # We move left by half the size, then left again by half the size
        # to return to the center of the original base. Then we move up
        # by half the height of a triangle of size/2.
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)

        # 5. Draw the top Sierpinski triangle.
        draw_sierpinski(t, order - 1, size / 2)

        # 6. Move back to the original starting position for this triangle.
        # This is crucial to ensure the next recursive call starts from the
        # correct place, effectively creating the "hole" in the middle.
        t.left(60)
        t.backward(size / 2)
        t.right(60)

def setup_turtle(speed="fastest", pencolor="blue", fillcolor="yellow"):
    """
    Sets up the turtle screen and turtle object.

    Args:
        speed (str): The drawing speed of the turtle. Options: "fastest", "fast", "normal", "slow", "slowest".
        pencolor (str): The color of the lines drawn by the turtle.
        fillcolor (str): The color used to fill the shapes.

    Returns:
        turtle.Turtle: The configured turtle object.
    """
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("white")
    screen.title("Sierpinski Triangle Explorer")

    t = turtle.Turtle()
    t.speed(speed)
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.hideturtle()  # Hide the turtle icon while drawing for a cleaner look.
    t.penup()       # Lift the pen so we don't draw while moving to the start.
    t.goto(-150, -100) # Position the turtle to draw the triangle nicely on screen.
    t.pendown()     # Put the pen down to start drawing.
    return t

# --- Example Usage ---
if __name__ == "__main__":
    # Get user input for the fractal order.
    # This allows for interactive exploration.
    while True:
        try:
            fractal_order = int(input("Enter the order of the Sierpinski Triangle (e.g., 0, 1, 2, 3, 4): "))
            if 0 <= fractal_order <= 6: # Limit order to prevent excessive computation
                break
            else:
                print("Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Setup the turtle environment
    my_turtle = setup_turtle(pencolor="darkgreen", fillcolor="lightgreen")

    # Define the initial size of the base of the largest triangle
    initial_size = 300

    # Start drawing the Sierpinski Triangle
    print(f"Drawing Sierpinski Triangle of order {fractal_order}...")
    draw_sierpinski(my_turtle, fractal_order, initial_size)
    print("Drawing complete!")

    # Keep the window open until it's manually closed.
    turtle.done()