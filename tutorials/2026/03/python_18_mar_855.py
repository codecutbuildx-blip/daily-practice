# String Hashing in Python

# Import the hashlib library for hashing strings
import hashlib

def calculate_hash(input_string):
    """
    This function calculates the hash of a given input string.
    
    :param input_string: The string to be hashed.
    :return: A hexadecimal representation of the hash value.
    """
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Convert the input string into bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash value
    hex_hash = hash_object.hexdigest()
    
    return hex_hash

def main():
    """
    This is the main function to test the string hashing.
    """
    # Test the calculate_hash function with a sample input string
    input_string = "Hello, World!"
    print("Input String:", input_string)
    
    # Calculate and print the hash of the input string
    hex_hash = calculate_hash(input_string)
    print("Hash Value (Hex):", hex_hash)

if __name__ == "__main__":
    main()