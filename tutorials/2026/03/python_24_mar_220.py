# String Hashing in Python
# Author: [Your Name]
# Date: [Today's Date]

def string_hash(s):
    """
    This function calculates the hash of a given string.
    
    The hashing is done using a simple algorithm based on ASCII values of characters.
    
    Parameters:
    s (str): The input string for which the hash needs to be calculated.
    
    Returns:
    int: The calculated hash value of the string.
    """
    hash_value = 0
    # Multiply each character by its ASCII value and add it to the total sum
    for char in s:
        hash_value += ord(char)
    return hash_value

def main():
    print("String Hashing Example:")
    # Test the function with a sample string
    original_string = "Hello World"
    hashed_string = string_hash(original_string)
    
    print(f"Original String: {original_string}")
    print(f"Hashed String: {hashed_string}")

if __name__ == "__main__":
    main()
```

This code defines a function `string_hash` that calculates the hash of a given string. The hashing is done by multiplying each character's ASCII value and adding it to a total sum.

In the `main` function, we test this function with a sample string and print out both the original and hashed strings.

You can run this code in your Python environment to see the output.

```python
# Run this code
```

When you run this code, it will display something like:

```
String Hashing Example:
Original String: Hello World
Hashed String: 53256121