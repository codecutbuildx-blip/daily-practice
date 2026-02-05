# Educational Tutorial: Generating Fractal Art with Python Turtle and Recursion

# Learning Objective:
# This tutorial will teach you how to create beautiful fractal art using the power
# of recursion and Python's built-in Turtle graphics module. You will learn
# how recursion allows for self-similar patterns to be generated efficiently,
# and how to control the Turtle to draw these intricate designs.

import turtle

# --- Configuration ---
# We'll use these constants to easily adjust the fractal's appearance.
# This makes it easier to experiment without changing the core logic.

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PEN_SPEED = 0  # 0 is the fastest, 1-10 are slower speeds
PEN_COLOR = "blue"
BACKGROUND_COLOR = "black"
INITIAL_LENGTH = 100
INITIAL_ANGLE = 90

# --- The Recursive Function: Drawing a Fractal Tree ---
# Recursion is a programming technique where a function calls itself.
# This is perfect for fractals because they are self-similar –
# smaller parts of the fractal look like the whole fractal.

def draw_fractal_tree(t, length, level):
    """
    Recursively draws a fractal tree.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the branch to draw.
        level (int): The current recursion depth or level.
    """

    # Base Case: This is CRUCIAL for recursion.
    # It's the condition that STOPS the recursion from going on forever.
    # If the level is 0, we've reached the end of a branch and don't draw anything further.
    if level <= 0:
        return

    # Drawing the current branch:
    # We move the turtle forward by the specified 'length'.
    t.forward(length)

    # Now, we need to draw the smaller branches that stem from this one.
    # For a tree, we typically draw two branches at an angle.

    # Save the turtle's current state (position and heading)
    # so we can return to it after drawing the sub-branches.
    # This is like bookmarking our place.
    t.penup()  # Lift the pen to avoid drawing lines while repositioning
    t.forward(length * 0.3) # Move forward a bit to create a gap for the trunk
    t.pendown()

    # Store the current position and heading before recursing
    current_pos = t.position()
    current_heading = t.heading()

    # --- Recursive Step 1: Drawing the Left Branch ---
    # We'll make the left branch shorter (e.g., 70% of the current length)
    # and at an angle (e.g., 30 degrees to the left).
    t.left(30)
    # Recursively call the function for the left branch.
    # We decrease the 'length' and the 'level' for the next iteration.
    draw_fractal_tree(t, length * 0.7, level - 1)

    # --- Backtrack 1: Returning to the split point ---
    # After the left branch is drawn, we need to return the turtle
    # to the point where the branches split from the main trunk.
    # This is why we saved the state earlier.
    t.penup()
    t.goto(current_pos) # Go back to the saved position
    t.setheading(current_heading) # Restore the saved heading
    t.pendown()

    # --- Recursive Step 2: Drawing the Right Branch ---
    # Now, we draw the right branch.
    # We'll make it the same length as the left branch and at an angle
    # to the right (e.g., 30 degrees).
    t.right(30)
    # Recursively call the function for the right branch.
    # Again, decrease 'length' and 'level'.
    draw_fractal_tree(t, length * 0.7, level - 1)

    # --- Backtrack 2: Returning to the previous branch ---
    # After the right branch is drawn, we return to the starting point
    # of the current 'draw_fractal_tree' call.
    # This allows the function to return to its caller (which might be
    # another recursive call).
    t.penup()
    t.goto(current_pos) # Go back to the saved position
    t.setheading(current_heading) # Restore the saved heading
    t.pendown()

    # Move the turtle back to where it started this call to 'draw_fractal_tree'
    # to prepare for the parent call's subsequent operations (if any).
    t.backward(length)


# --- Example Usage ---
if __name__ == "__main__":
    # This block runs only when the script is executed directly.

    # 1. Set up the screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Recursive Fractal Tree")
    screen.tracer(0) # Turn off screen updates for faster drawing

    # 2. Create a turtle object
    artist = turtle.Turtle()
    artist.speed(PEN_SPEED)
    artist.color(PEN_COLOR)
    artist.hideturtle() # Hide the turtle icon for a cleaner look

    # 3. Position the turtle at the bottom center for the tree base
    artist.penup()
    artist.goto(0, -SCREEN_HEIGHT / 2 + 50) # Move to bottom, slightly up
    artist.left(90) # Point the turtle upwards
    artist.pendown()

    # 4. Set the initial drawing parameters for the fractal
    # We call the recursive function to start drawing the tree.
    # The 'level' determines the complexity of the fractal. Higher levels
    # mean more detail but take longer to draw.
    # Let's start with a level of 8.
    INITIAL_LEVEL = 8
    draw_fractal_tree(artist, INITIAL_LENGTH, INITIAL_LEVEL)

    # 5. Update the screen to show the finished drawing
    screen.update()

    # 6. Keep the window open until it's closed by the user
    screen.mainloop()