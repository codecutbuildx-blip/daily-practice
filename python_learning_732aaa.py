# Procedural Art Generation with Python Turtle: Exploring Random Colors

# Learning Objective:
# This tutorial will teach you how to procedurally generate unique, abstract visual art
# using Python's `turtle` module. We will focus on the concept of using random colors
# to create variations and explore how simple instructions can lead to complex visual
# patterns. This will help beginners understand the basics of procedural generation
# and how to introduce randomness for artistic effect.

import turtle
import random

# --- Setup the Turtle Screen ---

# Create a screen object. This is the window where our drawing will appear.
screen = turtle.Screen()
# Set the background color of the screen. Black often makes bright colors stand out.
screen.bgcolor("black")
# Set the title of the window.
screen.title("Procedural Turtle Art - Random Colors")

# --- Setup the Turtle Pen ---

# Create a turtle object. This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
# Set the drawing speed. '0' is the fastest, '1' is slowest, and '10' is fast.
# For procedural art, faster speeds allow us to see the overall pattern emerge.
artist.speed(0)
# Hide the turtle icon (the arrow) after it has finished drawing.
artist.hideturtle()
# Set the initial pen color. We will change this randomly later.
artist.pencolor("white")
# Set the initial pen size. A slightly larger pen can create bolder lines.
artist.pensize(2)

# --- Core Drawing Function ---

def draw_art(num_lines):
    """
    Draws a piece of abstract art by repeatedly drawing lines with random colors.

    Args:
        num_lines (int): The number of lines to draw. This controls the complexity.
    """
    # Loop 'num_lines' times to draw each line of our art.
    for _ in range(num_lines):
        # --- Random Color Generation ---
        # We want to pick random RGB values for our color.
        # RGB stands for Red, Green, Blue, and each component can range from 0 to 255.
        # The `random.randint(0, 255)` function picks a random integer within this range.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Set the turtle's pen color using the generated random RGB values.
        # Turtle expects colors as a tuple of three floats between 0.0 and 1.0.
        # We need to divide our 0-255 values by 255.0 to get the correct format.
        artist.pencolor(r / 255.0, g / 255.0, b / 255.0)

        # --- Random Movement and Drawing ---
        # Choose a random distance to move the turtle.
        # This creates variations in line length.
        distance = random.randint(20, 150)

        # Choose a random angle to turn the turtle.
        # This determines the orientation of each line.
        # `random.randint(-180, 180)` allows for turns in both clockwise and counter-clockwise directions.
        angle = random.randint(-180, 180)

        # Lift the pen up before moving to a new random position.
        # This prevents drawing lines between disconnected elements.
        artist.penup()
        # Move the turtle to a random position on the screen.
        # `random.randint(-300, 300)` positions the turtle within a good portion of the screen.
        artist.goto(random.randint(-300, 300), random.randint(-300, 300))
        # Put the pen down to start drawing.
        artist.pendown()

        # Set the heading (direction) of the turtle.
        # This ensures the line is drawn in the desired direction after moving.
        artist.setheading(angle)

        # Move the turtle forward by the randomly chosen distance.
        # This draws the line with the current random color.
        artist.forward(distance)

# --- Example Usage ---

# Call the draw_art function to generate a piece of art.
# You can change the number '100' to create more or fewer lines.
# A larger number will result in a more complex and potentially denser artwork.
print("Generating abstract art with random colors...")
draw_art(100)
print("Art generation complete!")

# --- Keep the Window Open ---

# This line is crucial! It keeps the turtle graphics window open
# until the user manually closes it. Without this, the window
# would appear and disappear instantly after the drawing is finished.
turtle.done()