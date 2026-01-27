# Educational Tutorial: Generating Animated ASCII Art in the Console

# Learning Objective:
# This tutorial will teach you how to create simple animated ASCII art
# directly in your Python console. We will achieve this by leveraging
# the `time` module for timing our animations and the `os` module
# to clear the console screen between frames, creating a dynamic visual effect.
# This is a fundamental technique for creating interactive text-based
# applications and visualizers.

# Import necessary modules
import time  # For controlling the speed of our animation (pauses)
import os    # For interacting with the operating system, specifically clearing the console

def clear_console():
    # This function clears the console screen.
    # The command to clear the console is different on Windows and other operating systems (Linux/macOS).
    # `os.name` is 'nt' for Windows and 'posix' for Linux/macOS.
    # `os.system()` executes a command in the system's shell.
    # 'cls' is the command to clear screen on Windows.
    # 'clear' is the command to clear screen on Linux/macOS.
    if os.name == 'nt':
        os.system('cls') # Clear console on Windows
    else:
        os.system('clear') # Clear console on Linux/macOS

def animate_text(frames, delay=0.1):
    # This is our main animation function.
    # `frames` is a list of strings, where each string represents a single frame of our animation.
    # `delay` is the time in seconds to pause between displaying each frame.
    # A smaller delay results in a faster animation.

    try:
        # Loop through each frame in the provided list.
        for frame in frames:
            clear_console() # First, clear the console to remove the previous frame.
            print(frame)    # Then, print the current frame of our ASCII art.
            time.sleep(delay) # Pause for the specified `delay` duration. This controls the animation speed.

    except KeyboardInterrupt:
        # This block handles the case where the user presses Ctrl+C to interrupt the animation.
        # It's good practice to include this for user-friendly termination.
        print("\nAnimation interrupted by user.")
        clear_console() # Clean up by clearing the console one last time.

# --- Example Usage ---

if __name__ == "__main__":
    # This block of code will only run when the script is executed directly (not imported as a module).
    # It's a standard Python idiom for including example usage.

    # Define the frames for our animation.
    # Each string is a separate frame. We can use multi-line strings for complex art.
    # Notice how the characters shift or change to create movement.
    animation_frames = [
        # Frame 1: Starting position
        """
        o--o
        |  |
        o--o
        """,

        # Frame 2: Moving the arms
        """
        o--o
       /|  |
        o--o
        """,

        # Frame 3: Further movement
        """
        o--o
       /|  |\
        o--o
        """,

        # Frame 4: Completing the movement
        """
        o--o
       /|  |\
        o--o
         --
        """,

        # Frame 5: Reversing the movement
        """
        o--o
       /|  |
        o--o
         --
        """,

        # Frame 6: Back to initial
        """
        o--o
        |  |
        o--o
         --
        """,
    ]

    print("Starting ASCII animation. Press Ctrl+C to stop.")
    # Give the user a moment to read the starting message.
    time.sleep(2)

    # Call the animation function with our defined frames and a slight delay.
    # A delay of 0.2 seconds means each frame is shown for 0.2 seconds.
    animate_text(animation_frames, delay=0.2)

    print("\nAnimation finished!")
    # Ensure the console is cleared one last time after the animation ends gracefully.
    # This prevents the last frame from lingering if the animation completes without interruption.
    # However, animate_text already clears on KeyboardInterrupt, so this might be redundant
    # if animation_frames is not empty. Let's keep it for clarity.
    clear_console()
    print("Console cleared.")