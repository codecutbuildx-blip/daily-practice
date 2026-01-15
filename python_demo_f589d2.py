# LEARNING OBJECTIVE:
# This tutorial teaches you how to simulate basic IoT sensor data streams,
# process these streams in a simple real-time manner, and trigger alerts
# when predefined thresholds are exceeded or fallen below. You will learn
# to combine random data generation, conditional logic, and timed execution
# to mimic a rudimentary IoT monitoring system, all using clear and concise Python.

import random # Used to generate random sensor readings, simulating real-world variability.
import time   # Used to pause the execution, simulating the time interval between sensor readings.

# --- Configuration Constants ---
# These constants define the behavior of our simulation and alerting system.
# Using constants makes the code easier to read, understand, and modify
# without changing the core logic.

# Sensor Simulation Parameters:
NORMAL_TEMP_MIN: float = 20.0 # The lower bound for the 'normal' temperature range in Celsius.
NORMAL_TEMP_MAX: float = 25.0 # The upper bound for the 'normal' temperature range in Celsius.
OUTLIER_CHANCE: float = 0.1   # The probability (10%) that a reading will be an 'outlier'
                              # (a reading significantly outside the normal range).
OUTLIER_MAGNITUDE: float = 10.0 # How far an outlier can deviate from the normal range
                                # (e.g., normal max + 10, or normal min - 10).

# Alert Thresholds:
TEMP_WARNING_HIGH: float = 27.0  # Temperature above this value triggers a 'warning' alert.
TEMP_CRITICAL_HIGH: float = 30.0 # Temperature above this value triggers a 'critical' alert,
                                 # indicating a more severe issue.
TEMP_WARNING_LOW: float = 18.0   # Temperature below this value triggers a 'warning' alert.
TEMP_CRITICAL_LOW: float = 15.0  # Temperature below this value triggers a 'critical' alert.

# Simulation Control:
SIMULATION_DURATION_SECONDS: int = 30 # Total time the simulation will run in seconds.
SENSOR_READ_INTERVAL_SECONDS: float = 2.0 # How often a new sensor reading is generated
                                          # and processed during the simulation.

# --- Sensor Data Simulation Function ---
def simulate_temperature_reading() -> float:
    """
    Generates a simulated temperature reading. Most readings will be within a
    'normal' range, but occasionally an 'outlier' reading will occur to
    simulate unusual conditions or potential sensor malfunctions.
    """
    # Decide if this reading should be an outlier based on the predefined OUTLIER_CHANCE.
    if random.random() < OUTLIER_CHANCE:
        # If it's an outlier, randomly decide if it's a high outlier or a low outlier.
        if random.choice([True, False]): # True for high outlier, False for low outlier.
            # Generate a high outlier, significantly above the normal max.
            # random.uniform generates a float between the two given numbers (inclusive).
            return random.uniform(NORMAL_TEMP_MAX + 1, NORMAL_TEMP_MAX + OUTLIER_MAGNITUDE)
        else:
            # Generate a low outlier, significantly below the normal min.
            return random.uniform(NORMAL_TEMP_MIN - OUTLIER_MAGNITUDE, NORMAL_TEMP_MIN - 1)
    else:
        # Most of the time, generate a normal reading within the defined range.
        return random.uniform(NORMAL_TEMP_MIN, NORMAL_TEMP_MAX)

# --- Data Processing and Alerting Function ---
def process_and_alert(temperature: float, timestamp: float) -> None:
    """
    Processes a given temperature reading by comparing it against predefined
    thresholds and prints an alert message if a threshold is breached.
    """
    # Using an f-string for formatted output, displaying the current reading and time.
    # time.ctime() converts a timestamp (seconds since epoch) into a readable string.
    print(f"[{time.ctime(timestamp)}] Current Temperature: {temperature:.2f}°C")

    # Check for critical high temperature first, as it's the most severe condition.
    if temperature >= TEMP_CRITICAL_HIGH:
        print("!!! ALERT: CRITICAL HIGH TEMPERATURE detected! Immediate action required! !!!")
    # If not critically high, check for warning high temperature.
    elif temperature >= TEMP_WARNING_HIGH:
        print("WARNING: High temperature detected. Monitor closely.")
    # If not high, check for critical low temperature.
    elif temperature <= TEMP_CRITICAL_LOW:
        print("!!! ALERT: CRITICAL LOW TEMPERATURE detected! Immediate action required! !!!")
    # If not critically low, check for warning low temperature.
    elif temperature <= TEMP_WARNING_LOW:
        print("WARNING: Low temperature detected. Monitor closely.")
    else:
        # If none of the thresholds are breached, the temperature is within the normal range.
        print("Status: Normal temperature.")
    print("-" * 40) # Print a separator line for better readability between readings.

# --- Main Simulation Loop (Example Usage) ---
# This block of code ensures that the simulation runs only when the script is
# executed directly (not when imported as a module into another script).
if __name__ == "__main__":
    print("Starting IoT Sensor Data Stream Simulation...")
    print(f"Monitoring temperature for {SIMULATION_DURATION_SECONDS} seconds,")
    print(f"generating a new reading every {SENSOR_READ_INTERVAL_SECONDS} seconds.")
    print("--------------------------------------------------")

    # Calculate the end time for the simulation to control its duration.
    end_time: float = time.time() + SIMULATION_DURATION_SECONDS
    
    # Loop continuously, generating and processing data, until the simulation duration is over.
    while time.time() < end_time:
        current_timestamp: float = time.time() # Get the current time as a floating-point timestamp.
        
        # 1. Simulate a new sensor reading.
        # This calls our simulation function to get a random temperature value.
        current_temp: float = simulate_temperature_reading()
        
        # 2. Process the reading and trigger alerts if necessary.
        # The reading and its timestamp are passed to our processing function for evaluation.
        process_and_alert(current_temp, current_timestamp)
        
        # 3. Pause for the defined interval to simulate real-time data flow.
        # This makes the simulation run at a realistic pace, rather than instantly.
        time.sleep(SENSOR_READ_INTERVAL_SECONDS)
        
    print("\nSimulation Finished.")
    print("--------------------------------------------------")
    print("You can adjust constants like thresholds, outlier chance, and simulation duration")
    print("at the top of the script to experiment with different scenarios.")