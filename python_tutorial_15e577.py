# Learning Objective: Understand and apply recursion by drawing Sierpinski triangles.
# Recursion is a programming technique where a function calls itself.
# We'll use it to create intricate, self-similar patterns.

import turtle

# --- Core Recursive Function ---
def draw_sierpinski(t, order, size):
    """
    Recursively draws a Sierpinski triangle.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        order (int): The current level of recursion (detail level).
        size (float): The length of the side of the current triangle.
    """
    # Base Case: If the order is 0, we stop recursing.
    # This is crucial to prevent infinite loops.
    if order == 0:
        # Draw a filled triangle for the smallest component.
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
        return # Stop this branch of recursion

    # Recursive Step: If order > 0, we divide the problem into smaller,
    # similar sub-problems and call ourselves.
    # We draw three smaller Sierpinski triangles, each with order-1.
    # The size of these smaller triangles is half the current size.

    # 1. Draw the bottom-left smaller triangle
    draw_sierpinski(t, order - 1, size / 2)

    # 2. Move to the starting position for the bottom-right smaller triangle.
    # We move forward by 'size / 2' to reach the midpoint of the base.
    t.forward(size / 2)

    # 3. Draw the bottom-right smaller triangle
    draw_sierpinski(t, order - 1, size / 2)

    # 4. Move to the starting position for the top smaller triangle.
    # First, move back by 'size / 2' to the center of the base.
    t.backward(size / 2)
    # Then, turn left by 60 degrees and move forward by 'size / 2'.
    # This positions the turtle at the apex of the original triangle,
    # but ready to draw a new smaller triangle starting from its base.
    t.left(60)
    t.forward(size / 2)
    t.right(60) # Reset turtle's heading for the next potential move

    # 5. Draw the top smaller triangle
    draw_sierpinski(t, order - 1, size / 2)

    # 6. Move back to the original starting position and orientation for this triangle.
    # This ensures the turtle is in the correct state after drawing the three sub-triangles,
    # so that the parent call can continue drawing correctly.
    t.left(60)
    t.backward(size / 2)
    t.right(60)

# --- Setup and Example Usage ---
if __name__ == "__main__":
    # Create a screen object to manage the drawing window.
    screen = turtle.Screen()
    screen.setup(width=800, height=700) # Set window dimensions
    screen.bgcolor("white") # Set background color
    screen.title("Sierpinski Triangle - A Recursive Pattern")

    # Create a turtle object for drawing.
    my_turtle = turtle.Turtle()
    my_turtle.speed(0) # Set speed to fastest
    my_turtle.penup() # Lift the pen so it doesn't draw while moving to start
    my_turtle.goto(-200, -150) # Position the turtle to draw the base triangle
    my_turtle.pendown() # Put the pen down to start drawing

    # Set drawing color and fill color.
    my_turtle.pencolor("blue")
    my_turtle.fillcolor("lightblue")

    # --- Example: Draw a Sierpinski triangle with order 4 and side length 400 ---
    # Higher 'order' means more detail and computation.
    # 'size' determines the overall dimensions of the fractal.
    recursion_order = 4
    triangle_size = 400

    # Call the recursive function to start drawing.
    draw_sierpinski(my_turtle, recursion_order, triangle_size)

    # Hide the turtle after drawing is complete for a cleaner look.
    my_turtle.hideturtle()

    # Keep the window open until it's manually closed.
    screen.mainloop()