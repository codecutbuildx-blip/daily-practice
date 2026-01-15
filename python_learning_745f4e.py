# Tutorial: Real-Time Audio Visualizer with Pygame
# Learning Objective: This tutorial will teach you how to create a basic real-time audio visualizer
# in Python using the Pygame library. We will focus on capturing audio input, processing it to get
# frequency data, and then drawing a simple visualization based on that data.
# This will help you understand how audio data can be represented visually and how to interact
# with real-time audio streams in Python.

import pygame
import numpy as np
import pyaudio
import math

# --- Configuration ---
# These constants control the behavior of our visualizer.
# You can experiment with these values to see how they affect the output.

SAMPLE_RATE = 44100       # The number of audio samples taken per second. Higher is better quality.
CHUNK_SIZE = 1024         # The number of audio frames to process at once. Affects responsiveness.
FORMAT = pyaudio.paInt16  # The audio sample format (e.g., 16-bit integers).
CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo).
BAR_WIDTH = 10            # Width of each bar in our visualizer.
BAR_SPACING = 5           # Space between each bar.
MAX_HEIGHT = 400          # Maximum height of the bars.
SCREEN_WIDTH = 800        # Width of the Pygame window.
SCREEN_HEIGHT = 600       # Height of the Pygame window.
BAR_COLOR = (0, 255, 0)   # Color of the bars (RGB tuple).
BACKGROUND_COLOR = (0, 0, 0) # Background color of the window.

# --- Initialization ---
# We need to initialize Pygame and PyAudio to start our application.

pygame.init() # Initialize all Pygame modules.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the display surface.
pygame.display.set_caption("Real-Time Audio Visualizer") # Set the window title.

# Initialize PyAudio.
p = pyaudio.PyAudio()

# Open an audio input stream.
# This allows us to capture audio from the microphone.
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)

# --- Helper Functions ---
# These functions will help us process the audio data and draw on the screen.

def get_audio_data():
    # Read a chunk of audio data from the stream.
    # The data is returned as a byte string.
    data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

    # Convert the byte string to a NumPy array of integers.
    # This makes it easier to perform mathematical operations on the audio data.
    # We use 'int16' because our FORMAT is pyaudio.paInt16.
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Calculate the Root Mean Square (RMS) of the audio data.
    # RMS is a measure of the amplitude (loudness) of the audio signal.
    # We square each sample, take the average, and then the square root.
    rms = np.sqrt(np.mean(audio_data**2))

    # Normalize the RMS value to a scale between 0 and 1.
    # This makes it easier to map the loudness to the height of our visualizer bars.
    # The maximum possible value for a 16-bit integer is 32767.
    normalized_rms = rms / 32767.0

    # Return the normalized loudness.
    return normalized_rms

def draw_visualizer(loudness):
    # Fill the screen with the background color.
    # This clears the previous frame, so we can draw the new visualization.
    screen.fill(BACKGROUND_COLOR)

    # Calculate the number of bars we can fit on the screen.
    num_bars = (SCREEN_WIDTH - BAR_SPACING) // (BAR_WIDTH + BAR_SPACING)

    # Calculate the base height of the bars.
    # This will be a fraction of the maximum height, proportional to the loudness.
    base_height = loudness * MAX_HEIGHT

    # Iterate through the number of bars to draw them.
    for i in range(num_bars):
        # Calculate the height of the current bar.
        # We add a small random variation to make it look more dynamic.
        bar_height = base_height + np.random.uniform(0, 5)

        # Ensure the bar height doesn't exceed the screen height.
        bar_height = min(bar_height, MAX_HEIGHT)

        # Calculate the x-coordinate for the left edge of the bar.
        x = i * (BAR_WIDTH + BAR_SPACING) + BAR_SPACING

        # Calculate the y-coordinate for the top edge of the bar.
        # This positions the bar at the bottom of the screen.
        y = SCREEN_HEIGHT - bar_height

        # Create a rectangle for the current bar.
        bar_rect = pygame.Rect(x, y, BAR_WIDTH, bar_height)

        # Draw the bar on the screen.
        pygame.draw.rect(screen, BAR_COLOR, bar_rect)

    # Update the Pygame display to show the drawn bars.
    pygame.display.flip()

# --- Main Application Loop ---
# This is where the program runs continuously, processing audio and updating the display.

running = True
while running:
    # Event handling: Check for user input (like closing the window).
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user clicks the close button.
            running = False          # Set running to False to exit the loop.

    # Get the current audio loudness.
    loudness = get_audio_data()

    # Draw the visualizer based on the loudness.
    draw_visualizer(loudness)

# --- Cleanup ---
# When the loop finishes, we need to properly close the audio stream and Pygame.

stream.stop_stream() # Stop the audio stream.
stream.close()       # Close the audio stream.
p.terminate()        # Terminate the PyAudio session.
pygame.quit()        # Uninitialize Pygame modules.

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Python installed.
# 2. Install Pygame and PyAudio:
#    pip install pygame numpy pyaudio
# 3. Save the code as a Python file (e.g., visualizer.py).
# 4. Run from your terminal:
#    python visualizer.py
#
# You should see a Pygame window appear, and as you speak or make noise into your
# microphone, the green bars should rise and fall in response to the loudness.
# Experiment with the CONFIGURATION constants at the top to change the visualizer's appearance.