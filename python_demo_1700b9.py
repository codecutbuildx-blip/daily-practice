# Python Bedtime Story Generator Tutorial
#
# Learning Objective: This tutorial will teach you how to use Python
# functions to create dynamic and personalized text. We will focus on:
# 1. Taking user input to gather information.
# 2. Defining and using functions to organize code and avoid repetition.
# 3. String formatting to embed user-provided data into a story template.
#
# This script will create a simple bedtime story based on a child's name
# and their favorite object, making it a fun and engaging way to learn
# basic Python programming concepts.

# --- Step 1: Getting User Input ---
# We need to ask the user for some information to personalize the story.
# The `input()` function displays a message and waits for the user to type
# something and press Enter. It returns whatever the user types as a string.

def get_story_details():
    """
    Prompts the user for the child's name and their favorite object.
    Returns these details as a tuple (child_name, favorite_object).
    """
    # Ask for the child's name.
    # The prompt message inside input() is what the user sees.
    child_name = input("What is the child's name? ")

    # Ask for the child's favorite object.
    favorite_object = input(f"What is {child_name}'s favorite object? ")

    # It's good practice to return multiple values from a function if they
    # are related. We use a tuple for this.
    return child_name, favorite_object

# --- Step 2: Defining the Story Template Function ---
# Functions allow us to group related code and reuse it. This is key to
# writing clean and organized programs. We'll create a function that
# takes the user's details and builds the story.

def generate_bedtime_story(name, favorite_item):
    """
    Generates a personalized bedtime story using the provided name and favorite item.
    This function demonstrates f-strings for easy string formatting.
    """
    # We use f-strings (formatted string literals) for embedding variables
    # directly into strings. The variable names are placed inside curly braces {}.
    # This is a modern and very readable way to format strings in Python.

    story = f"""
Once upon a time, in a cozy little room, lived a wonderful child named {name}.
{name} loved to play with their favorite object, a magical {favorite_item}.

One evening, as the stars began to twinkle, {name} and their {favorite_item}
embarked on a grand adventure! They imagined flying to the moon on a cloud
made of {favorite_item}s. The moon was covered in fluffy {favorite_item}s,
and {name} giggled with delight.

After a fun-filled night, {name} and their {favorite_item} floated gently
back to their cozy room, ready for a good night's sleep.
Sweet dreams, {name}!
"""
    # The triple quotes """ """ allow us to create multi-line strings,
    # which are perfect for story text.

    return story

# --- Step 3: Putting It All Together (The Main Part of the Script) ---
# This is where we call our functions to get the user's input and then
# generate and display the story.

def main():
    """
    The main function to run the bedtime story generator.
    It calls get_story_details() and then generate_bedtime_story().
    Finally, it prints the resulting story.
    """
    print("Let's create a magical bedtime story!")

    # Call our function to get the user's input.
    # We unpack the tuple returned by get_story_details() into two variables.
    child_name, favorite_object = get_story_details()

    # Now, call the story generation function with the gathered details.
    # Again, we are passing the variables as arguments to the function.
    bedtime_story = generate_bedtime_story(child_name, favorite_object)

    # Print the final, personalized story to the console.
    print("\n--- Your Magical Bedtime Story ---")
    print(bedtime_story)
    print("---------------------------------")

# --- Running the Script ---
# This is a standard Python construct. The `if __name__ == "__main__":` block
# ensures that the `main()` function is called only when the script is executed
# directly (not when it's imported as a module into another script).
if __name__ == "__main__":
    main()

# --- Example Usage ---
# To run this script:
# 1. Save the code above as a Python file (e.g., bedtime_story.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python bedtime_story.py
#
# The script will then ask you for input, and after you provide it,
# it will print a personalized story.
#
# Example Interaction:
#
# Let's create a magical bedtime story!
# What is the child's name? Lily
# What is Lily's favorite object? A shiny red ball
#
# --- Your Magical Bedtime Story ---
#
# Once upon a time, in a cozy little room, lived a wonderful child named Lily.
# Lily loved to play with their favorite object, a magical shiny red ball.
#
# One evening, as the stars began to twinkle, Lily and their shiny red ball
# embarked on a grand adventure! They imagined flying to the moon on a cloud
# made of shiny red balls. The moon was covered in fluffy shiny red balls,
# and Lily giggled with delight.
#
# After a fun-filled night, Lily and their shiny red ball floated gently
# back to their cozy room, ready for a good night's sleep.
# Sweet dreams, Lily!
# ---------------------------------