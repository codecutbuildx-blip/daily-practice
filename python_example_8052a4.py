# Dynamic DNS Updater Tutorial

# Learning Objective:
# This tutorial will guide you through building a Python script
# to automatically update your Dynamic DNS (DDNS) records.
# We will focus on the core concept of interacting with a DDNS
# provider's API to send your current public IP address.
# This script is designed to be run periodically (e.g., via cron)
# to keep your domain name pointing to your ever-changing home IP.

# --- Imports ---
# We need the 'requests' library to make HTTP requests to the DDNS provider.
# If you don't have it installed, you can install it using: pip install requests
import requests
# The 'socket' module is used to get the local machine's hostname, which is
# often required by DDNS providers to identify which record to update.
import socket
# The 'os' module is useful for accessing environment variables, which is a
# secure way to store sensitive credentials like API keys and passwords.
import os

# --- Configuration ---
# IMPORTANT: Replace these with your actual DDNS provider details.
# This is where you'll tell the script about your domain, username, and password.

# The base URL for your DDNS provider's API endpoint for updating records.
# Example for some providers: "https://dynupdate.no-ip.com/nic/update"
# Consult your DDNS provider's documentation for the correct URL.
DDNS_API_URL = "YOUR_DDNS_API_URL"

# Your DDNS hostname (the domain name you want to update).
# Example: "mycoolhome.ddns.net"
DDNS_HOSTNAME = "YOUR_DDNS_HOSTNAME"

# Your DDNS username (often your account email or a specific username).
DDNS_USERNAME = "YOUR_DDNS_USERNAME"

# Your DDNS password or API key.
# It's highly recommended to store these as environment variables for security.
# Example: os.environ.get("DDNS_PASSWORD")
DDNS_PASSWORD = "YOUR_DDNS_PASSWORD" # Or better: os.environ.get("DDNS_PASSWORD")

# --- Helper Functions ---

def get_public_ip():
    # Function to get your current public IP address.
    # We'll use an external service like ifconfig.me to determine this.
    # DDNS providers need to know your *public* IP, not your local network IP.
    try:
        # Making a GET request to a reliable IP lookup service.
        response = requests.get("https://api.ipify.org")
        # Raise an exception for bad status codes (4xx or 5xx).
        response.raise_for_status()
        # The IP address is returned as plain text.
        public_ip = response.text.strip()
        print(f"Detected public IP: {public_ip}")
        return public_ip
    except requests.exceptions.RequestException as e:
        # If there's an error (network issue, service down), we print it.
        print(f"Error fetching public IP: {e}")
        return None

def update_ddns_record(ip_address):
    # Function to send the IP address to your DDNS provider.
    # This is the core logic for updating the record.

    if not ip_address:
        print("Cannot update DDNS: No IP address available.")
        return False

    # Constructing the payload for the API request.
    # The exact parameters depend on your DDNS provider.
    # Common parameters include:
    # - hostname: The domain name to update.
    # - myip: The new IP address.
    # Consult your DDNS provider's documentation for exact parameter names.
    payload = {
        "hostname": DDNS_HOSTNAME,
        "myip": ip_address
    }

    try:
        # Making the HTTP request to the DDNS provider's API.
        # We use basic authentication for security, which is common.
        # The 'auth' parameter takes a tuple of (username, password).
        response = requests.get(DDNS_API_URL, params=payload, auth=(DDNS_USERNAME, DDNS_PASSWORD))

        # Checking the response status code.
        # A 2xx status code generally indicates success.
        # Some providers might return specific codes for successful updates.
        if response.status_code == 200:
            print(f"DDNS update successful for {DDNS_HOSTNAME} to {ip_address}")
            return True
        else:
            # If the status code is not 200, print an error message.
            # It's useful to print the response text for debugging.
            print(f"DDNS update failed. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        # Catching any network-related errors during the request.
        print(f"Error updating DDNS record: {e}")
        return False

# --- Main Script Logic ---

def main():
    # The main function that orchestrates the process.
    print("Starting DDNS update script...")

    # First, get the current public IP address.
    current_public_ip = get_public_ip()

    # If we successfully got an IP address, proceed to update DDNS.
    if current_public_ip:
        update_ddns_record(current_public_ip)
    else:
        print("Could not retrieve public IP address. DDNS update aborted.")

    print("DDNS update script finished.")

# --- Example Usage ---

if __name__ == "__main__":
    # The 'if __name__ == "__main__":' block ensures that the 'main()' function
    # is called only when this script is executed directly (not when imported
    # as a module into another script).

    # Before running, make sure you:
    # 1. Install the 'requests' library: pip install requests
    # 2. Replace placeholder values in the CONFIGURATION section with your actual DDNS details.
    #    - DDNS_API_URL
    #    - DDNS_HOSTNAME
    #    - DDNS_USERNAME
    #    - DDNS_PASSWORD (consider using environment variables for security)

    # To run this script:
    # 1. Save it as a Python file (e.g., ddns_updater.py).
    # 2. Open your terminal or command prompt.
    # 3. Navigate to the directory where you saved the file.
    # 4. Run the script using: python ddns_updater.py

    # To automate this, you would typically schedule this script to run
    # periodically using tools like 'cron' on Linux/macOS or Task Scheduler on Windows.
    # For example, to run every 15 minutes on Linux:
    # crontab -e
    # */15 * * * * /usr/bin/python3 /path/to/your/ddns_updater.py

    # If using environment variables for sensitive information (highly recommended):
    # export DDNS_PASSWORD="your_actual_password_or_api_key"
    # And ensure the script uses os.environ.get("DDNS_PASSWORD") for DDNS_PASSWORD.

    main()