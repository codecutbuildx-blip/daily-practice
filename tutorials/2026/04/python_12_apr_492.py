# String Hashing in Python
=====================================================

### Introduction

String hashing is an essential concept in computer science and information security. It involves calculating a numerical value from the characters of a string. This tutorial will guide you through implementing a simple string hashing algorithm using Python.

### Choosing a Hash Function

There are many hash functions available, including:

*   **Plain Hash**: Simple, but vulnerable to collisions.
*   **Rolling Hash**: More efficient than plain hash, but still has collision issues.
*   **FNV-1a Hash**: A widely used hashing algorithm that is less prone to collisions.

For this example, we will use the FNV-1a hash function.

### Python Implementation

```python
def fnv_1a_hash(string):
    # Define the initial hash value and prime number
    hash_value = 2166136261
    prime_number = 16777219
    
    # Iterate through each character in the string
    for char in string:
        # Convert the character to its ASCII value
        ascii_value = ord(char)
        
        # Calculate the new hash value using FNV-1a formula
        hash_value = (hash_value ^ ascii_value) * prime_number
        
    # Return the final hash value as a 32-bit integer
    return hash_value & 0xFFFFFFFF

# Test the implementation with a sample string
sample_string = "Hello, World!"
print("Hash Value:", fnv_1a_hash(sample_string))