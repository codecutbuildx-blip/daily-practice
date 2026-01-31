################################################################################
# LEARNING OBJECTIVE:
# This tutorial will teach you how to visualize audio frequencies in real-time
# using Python's Pygame for audio playback and visualization, and NumPy for
# efficient numerical operations, specifically the Fast Fourier Transform (FFT).
#
# We will focus on understanding:
# 1. How to load and play an audio file with Pygame.
# 2. How to capture audio data from the currently playing sound.
# 3. How to use NumPy's FFT to convert time-domain audio data into frequency-domain data.
# 4. How to draw a simple frequency spectrum visualization on a Pygame window.
#
# This is a fundamental step towards understanding audio processing and
# creating audio-reactive visualizations.
################################################################################

# Import necessary libraries.
# Pygame is used for audio playback and creating the visual window.
# NumPy is essential for mathematical operations, especially the FFT.
import pygame
import numpy as np

# --- Pygame Initialization ---
# Initialize Pygame. This is crucial for using any Pygame functionality,
# including its mixer module for audio.
pygame.init()

# --- Audio Settings ---
# Define audio parameters that are often required for audio processing.
# These should ideally match the format of your audio file, but Pygame
# is generally flexible.
SAMPLE_RATE = 44100  # Samples per second (standard for CDs and most digital audio).
CHANNELS = 2         # Number of audio channels (1 for mono, 2 for stereo).
FORMAT = -16        # Sample format (-16 for 16-bit signed integers, common).
BUFFER_SIZE = 4096   # Number of samples to read at a time for analysis.
                     # A larger buffer might give smoother results but higher latency.

# --- Pygame Mixer Initialization ---
# Initialize the Pygame mixer module. This is specifically for audio.
# We specify the sample rate, format, and number of channels.
pygame.mixer.init(SAMPLE_RATE, FORMAT, CHANNELS)

# --- Pygame Display Setup ---
# Set up the display window for visualization.
# SCREEN_WIDTH and SCREEN_HEIGHT define the dimensions of our visualization area.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Audio Frequency Visualizer")

# --- Colors ---
# Define some colors to use in our visualization.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# --- Load and Play Audio ---
# Specify the path to your audio file. Make sure this file exists.
# For this example, you'll need an MP3 or WAV file named 'your_audio.mp3'
# in the same directory as the script.
AUDIO_FILE = 'your_audio.mp3' # Replace with your audio file name.

try:
    # Load the sound file. Pygame can load various formats.
    sound = pygame.mixer.Sound(AUDIO_FILE)
    # Play the sound. The argument '0' means to play indefinitely (looping).
    # You can change this to a positive integer for a specific number of loops.
    channel = sound.play()
    print(f"Playing: {AUDIO_FILE}")
except pygame.error as e:
    print(f"Error loading or playing audio file: {e}")
    print("Please ensure 'your_audio.mp3' exists and is a valid audio file.")
    pygame.quit()
    exit() # Exit if audio cannot be loaded/played.

# --- Audio Analysis Function ---
def analyze_frequency(audio_data):
    """
    Takes raw audio data (as a NumPy array) and performs an FFT to get
    the frequency spectrum.

    Args:
        audio_data (np.ndarray): A 1D NumPy array of audio samples.

    Returns:
        np.ndarray: A 1D NumPy array representing the magnitude of frequencies.
    """
    # Perform the Fast Fourier Transform (FFT).
    # np.fft.fft converts the time-domain signal (audio_data) into the
    # frequency domain. The result is complex numbers representing magnitude and phase.
    fft_result = np.fft.fft(audio_data)

    # Calculate the magnitudes of the complex FFT results.
    # np.abs() gives the magnitude of each complex number. This is what we
    # typically visualize as the "strength" of a frequency.
    # We take only the first half of the FFT result because the FFT of a real
    # signal is symmetric. The frequencies above the Nyquist frequency are
    # redundant.
    magnitude = np.abs(fft_result[:BUFFER_SIZE // 2])

    # Normalize the magnitude for better visualization.
    # Dividing by the number of samples and multiplying by 2 (except for DC)
    # helps to scale the magnitudes consistently across different buffer sizes
    # and audio levels.
    magnitude = magnitude / len(audio_data) * 2
    magnitude[0] = magnitude[0] / 2 # DC component (0 Hz) doesn't need doubling.

    return magnitude

# --- Visualization Loop ---
running = True
while running:
    # --- Event Handling ---
    # Check for events like closing the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Audio Data Acquisition ---
    # Pygame's mixer.get_raw_data() allows us to get the audio buffer
    # that is currently being played. This is essential for real-time analysis.
    # We retrieve `BUFFER_SIZE` samples.
    raw_audio_data = pygame.mixer.Sound.get_raw_data(channel, BUFFER_SIZE)

    # Convert the raw byte data to a NumPy array of integers.
    # The format is typically 16-bit signed integers.
    # `dtype=np.int16` tells NumPy how to interpret the bytes.
    # `np.frombuffer` creates an array from a buffer.
    audio_samples = np.frombuffer(raw_audio_data, dtype=np.int16)

    # If the audio is stereo (2 channels), we'll only analyze one channel for simplicity.
    # We take the first `BUFFER_SIZE // 2` samples if it's stereo (each sample is 2 bytes).
    # This ensures we have a consistent number of samples for FFT.
    if audio_samples.size > BUFFER_SIZE: # Check if stereo data is longer than expected
        audio_samples = audio_samples[:BUFFER_SIZE] # Trim to buffer size if needed
    elif audio_samples.size < BUFFER_SIZE:
        # If we don't get enough samples, pad with zeros to reach BUFFER_SIZE.
        # This can happen if audio is ending or buffer is small.
        audio_samples = np.pad(audio_samples, (0, BUFFER_SIZE - audio_samples.size), 'constant')

    # For stereo, process only one channel to simplify the visualization.
    # We assume interleaved stereo: L, R, L, R...
    if CHANNELS == 2:
        audio_samples = audio_samples[0::2] # Take every other sample (e.g., left channel)

    # --- Frequency Analysis ---
    # Get the frequency spectrum using our helper function.
    frequency_magnitudes = analyze_frequency(audio_samples)

    # --- Drawing ---
    # Fill the screen with black to clear the previous frame.
    screen.fill(BLACK)

    # Draw the frequency spectrum.
    # We iterate through the frequency magnitudes.
    # For each frequency, we draw a vertical line.
    # The height of the line represents the magnitude of that frequency.
    for i, magnitude in enumerate(frequency_magnitudes):
        # Calculate the x-position for this frequency bin.
        # `i` is the index of the frequency bin. We map it to the screen width.
        bar_width = SCREEN_WIDTH / len(frequency_magnitudes)
        x_pos = i * bar_width

        # Scale the magnitude to the screen height for visualization.
        # `magnitude` is the strength of the frequency.
        # We clamp it to the screen height and ensure it's not negative.
        bar_height = min(magnitude * 10, SCREEN_HEIGHT) # Adjust multiplier for desired height

        # Draw the bar (line) representing the frequency magnitude.
        # `pygame.draw.line` draws a line from (x1, y1) to (x2, y2) with a given color.
        # Here, we draw a line from (x_pos, SCREEN_HEIGHT) to (x_pos, SCREEN_HEIGHT - bar_height).
        # The y-axis in Pygame is inverted (0 is at the top).
        pygame.draw.line(screen, GREEN, (x_pos, SCREEN_HEIGHT), (x_pos, SCREEN_HEIGHT - bar_height))

    # --- Update Display ---
    # Update the entire screen to show what we've drawn.
    pygame.display.flip()

    # --- Control Frame Rate ---
    # Limit the frame rate to prevent the visualization from consuming too much CPU.
    # This ensures a consistent visualization speed.
    pygame.time.Clock().tick(60) # Aim for 60 frames per second.

# --- Cleanup ---
# Stop the sound playback.
sound.stop()
# Quit Pygame. This is important for releasing resources.
pygame.quit()
print("Audio visualization stopped.")

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Pygame and NumPy installed:
#    pip install pygame numpy
# 2. Save this code as a Python file (e.g., audio_visualizer.py).
# 3. Place an audio file (e.g., a short MP3 or WAV) in the same directory
#    and name it 'your_audio.mp3'. If your file has a different name,
#    update the AUDIO_FILE variable in the script.
# 4. Run the script from your terminal:
#    python audio_visualizer.py
#
# You should see a Pygame window open, playing your audio file, and
# a real-time frequency spectrum visualization will be drawn.
# Close the window to stop the program.