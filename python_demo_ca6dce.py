"""
Learning Objective:
This tutorial will teach you how to create a Python bot that generates
unique abstract art using the `turtle` module. We'll focus on using
randomness to control the placement, size, and color of shapes,
demonstrating how simple commands can lead to complex and beautiful results.
This is a great introduction to procedural art generation.
"""

# Import the 'turtle' module, which is perfect for drawing graphics.
# It's like having a virtual pen on a canvas!
import turtle

# Import the 'random' module to introduce unpredictability.
# This will allow us to vary our art with random colors, sizes, and positions.
import random

# --- Setup the Canvas ---
# We create a 'Screen' object, which is our drawing canvas.
screen = turtle.Screen()
# Set the background color of our canvas. 'lightgray' is a nice, neutral choice.
screen.bgcolor("lightgray")
# Set the title of the window that will display our art.
screen.title("Abstract Art Generator")

# --- Setup the Turtle (our drawing pen) ---
# We create a 'Turtle' object. Think of this as our artist.
artist = turtle.Turtle()
# Set the drawing speed. '0' means the fastest possible speed,
# useful for generating art quickly. You can try slower speeds like '1' or '5'
# to see the drawing process step-by-step.
artist.speed(0)
# Hide the turtle icon itself. We only care about the art it creates.
artist.hideturtle()

# --- Define Helper Functions for Art Elements ---

def get_random_color():
    """
    Generates a random hexadecimal color code (e.g., '#RRGGBB').
    This function is key to creating visually diverse art.
    """
    # Each pair of characters in a hex color code represents red, green, or blue.
    # We generate 6 random hexadecimal characters (0-9, A-F).
    color_code = "#"
    for _ in range(6):
        # random.choice picks a random element from the given sequence.
        color_code += random.choice("0123456789ABCDEF")
    return color_code

def draw_random_shape(turtle_obj):
    """
    Draws a random geometric shape (rectangle or circle) with random properties.
    This is the core of our art generation.
    """
    # First, lift the pen so we don't draw a line while moving to a random position.
    turtle_obj.penup()

    # Choose a random position on the screen.
    # The screen dimensions are usually from -width/2 to width/2 and -height/2 to height/2.
    # We'll use -200 to 200 for both x and y to keep shapes within a reasonable area.
    x_pos = random.randint(-200, 200)
    y_pos = random.randint(-200, 200)
    # Move the turtle to the chosen random position.
    turtle_obj.goto(x_pos, y_pos)

    # Put the pen down to start drawing again.
    turtle_obj.pendown()

    # Choose a random color for the shape.
    color = get_random_color()
    # Set the fill color of the shape.
    turtle_obj.fillcolor(color)
    # Set the outline color of the shape.
    turtle_obj.pencolor(color) # Using the same color for both makes it solid

    # Decide randomly whether to draw a rectangle or a circle.
    shape_type = random.choice(["rectangle", "circle"])

    # Get a random size for the shape.
    size = random.randint(20, 100)

    # Begin filling the shape with the chosen color.
    turtle_obj.begin_fill()

    if shape_type == "rectangle":
        # Draw a rectangle. We need width and height.
        # Let's make the height proportional to the size.
        height = size * random.uniform(0.5, 2.0) # Height can vary relative to size
        # Draw the rectangle: move forward, turn, repeat for sides.
        for _ in range(2):
            turtle_obj.forward(size)
            turtle_obj.left(90)
            turtle_obj.forward(height)
            turtle_obj.left(90)
    else: # It's a circle
        # Draw a circle with the chosen size as the radius.
        turtle_obj.circle(size)

    # End filling the shape. This completes the drawing and filling process.
    turtle_obj.end_fill()

# --- Main Art Generation Loop ---

# How many shapes do we want in our artwork? Let's choose a random number.
num_shapes = random.randint(50, 200)
print(f"Generating {num_shapes} shapes...")

# Loop 'num_shapes' times to draw each shape.
for _ in range(num_shapes):
    # Call our helper function to draw one random shape.
    draw_random_shape(artist)

# --- Keep the Window Open ---
# This line is crucial! It keeps the turtle graphics window open
# until you manually close it. Without it, the program would run and
# the window would disappear immediately after drawing.
screen.mainloop()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., 'abstract_art.py').
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python abstract_art.py
# A window will pop up and start drawing your unique abstract art!
# Feel free to change 'num_shapes' or the range of 'size' in 'draw_random_shape'
# to experiment with different artistic styles.