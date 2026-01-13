# Learning Objective:
# This tutorial teaches you how to build a simple text-based adventure game
# in Python. We will focus on using conditional statements (if/elif/else)
# to control the game's flow based on player input and introduce a
# very basic form of AI-driven decision-making by predicting player intent.

# --- Game Components ---

def display_intro():
    # This function displays the introductory text for the game.
    # It sets the scene and introduces the player to the game world.
    print("Welcome, brave adventurer, to the Whispering Woods!")
    print("You find yourself at a fork in the path.")
    print("To your left, a dark, ominous forest beckons.")
    print("To your right, a sun-drenched meadow stretches out before you.")
    print("-" * 30) # A visual separator for readability.

def get_player_choice():
    # This function prompts the player for their choice and returns it.
    # We convert the input to lowercase to make comparisons easier.
    print("What do you do? (enter 'left' or 'right')")
    choice = input("> ").lower().strip() # .lower() for case-insensitivity, .strip() to remove whitespace.
    return choice

def simple_ai_decision(player_choice):
    # This function simulates a very basic AI that tries to understand
    # player intent and provide a slightly tailored response.
    # It's not "intelligent" in a complex way, but demonstrates
    # how we can use conditions to react to player input.

    # We're looking for keywords that might indicate the player's general direction.
    if "left" in player_choice:
        # If "left" is mentioned, the AI assumes the player wants to go left.
        return "forest"
    elif "right" in player_choice:
        # If "right" is mentioned, the AI assumes the player wants to go right.
        return "meadow"
    else:
        # If the input doesn't clearly indicate a direction, the AI defaults to a safe option.
        # This also handles invalid inputs gracefully.
        return "uncertain"

def process_decision(ai_prediction):
    # This function handles the game's narrative based on the AI's prediction.
    # This is where the core "if/elif/else" logic for game branching happens.

    if ai_prediction == "forest":
        # Scenario for choosing the forest path.
        print("\nYou bravely step into the dark forest.")
        print("Twisted trees loom over you, and the air grows cold.")
        print("Suddenly, you hear a rustling in the undergrowth!")
        print("You have encountered a wild boar! It charges!")
        print("You barely manage to leap aside. You are safe, but shaken.")
        print("You continue deeper into the woods, looking for a way out.")
        return "forest_end" # Indicate the player is now in the forest ending path.
    elif ai_prediction == "meadow":
        # Scenario for choosing the meadow path.
        print("\nYou stroll into the sun-drenched meadow.")
        print("Butterflies flutter around you, and the scent of wildflowers fills the air.")
        print("You spot a sparkling stream in the distance.")
        print("You quench your thirst and feel refreshed.")
        print("You follow the stream, which leads you out of the woods.")
        return "meadow_end" # Indicate the player is now in the meadow ending path.
    else:
        # Scenario for invalid or uncertain input.
        print("\nYou hesitate, unsure of which path to take.")
        print("A mysterious mist rolls in, disorienting you.")
        print("You stumble around aimlessly until you find yourself back where you started.")
        # We could return to the start of the game here, or end it. For simplicity, let's end.
        return "game_over_uncertain"

def display_ending(outcome):
    # This function displays a concluding message based on the game's outcome.
    print("-" * 30)
    if outcome == "forest_end":
        print("You have navigated the dangers of the Whispering Woods!")
        print("Your adventure continues elsewhere.")
    elif outcome == "meadow_end":
        print("You have found a peaceful exit from the Whispering Woods.")
        print("Your journey has been successful.")
    elif outcome == "game_over_uncertain":
        print("Your indecision has led you astray. The woods remain a mystery.")
        print("Game Over.")

# --- Game Flow ---

def play_game():
    # This is the main function that orchestrates the game's execution.
    display_intro() # Show the introduction.

    player_input = get_player_choice() # Get input from the player.

    # The AI prediction guides the narrative.
    ai_response = simple_ai_decision(player_input)

    # Process the AI's prediction to determine the next game state.
    game_state = process_decision(ai_response)

    # Display the appropriate ending based on the final game state.
    display_ending(game_state)

# --- Example Usage ---
# To run the game, simply call the play_game() function.
# This is the entry point for our adventure.

if __name__ == "__main__":
    # The 'if __name__ == "__main__":' block ensures that play_game()
    # is called only when the script is executed directly (not when imported as a module).
    play_game()

# --- Key Concepts Learned ---
# 1. Functions: Organizing code into reusable blocks (display_intro, get_player_choice, etc.).
# 2. Input/Output: Getting player input (input()) and displaying text (print()).
# 3. Conditional Statements: Using if, elif, and else to control program flow based on conditions.
# 4. String Methods: Using .lower() and .strip() to process user input effectively.
# 5. Basic AI Simulation: Using conditionals to react to player input in a simulated intelligent way.
# 6. Program Structure: Understanding how to put different parts of a program together to create a complete experience.