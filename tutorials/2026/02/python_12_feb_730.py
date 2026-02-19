# Hash Map in Python: A Practical Guide
======================================

This script teaches how to use hash maps (also known as dictionaries) in Python for efficient data storage and retrieval.

Hash maps are useful when you need to store key-value pairs where the key is unique and can be used to quickly look up its corresponding value. This is particularly useful for tasks such as:

*   Caching frequently accessed data
*   Storing configuration settings
*   Implementing a simple database

### Overview of Hash Maps

In Python, hash maps are implemented using the built-in `dict` class.

### Example Usage

```python
# Import the necessary modules
import hashlib

class SimpleHashMap:
    def __init__(self, size):
        # Initialize an empty list to store key-value pairs
        self.size = size
        self.map = [None] * size

    def _hash(self, key):
        # Calculate a hash value for the given key using SHA-256 algorithm
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.size

    def put(self, key, value):
        # Calculate the index where the key-value pair should be stored based on its hash value
        index = self._hash(key)
        
        # If a value is already at this index, update it
        if self.map[index] is not None:
            self.map[index] = (key, value)
        else:
            # Otherwise, store the key-value pair at this index
            self.map[index] = (key, value)

    def get(self, key):
        # Calculate the index where the key should be stored based on its hash value
        index = self._hash(key)
        
        # If a key is found at this index, return its corresponding value
        if self.map[index] is not None and self.map[index][0] == key:
            return self.map[index][1]
        else:
            # Otherwise, return None (no key-value pair found)
            return None

    def delete(self, key):
        # Calculate the index where the key should be stored based on its hash value
        index = self._hash(key)
        
        # If a key is found at this index, remove it from the map
        if self.map[index] is not None and self.map[index][0] == key:
            self.map[index] = None

# Create an instance of SimpleHashMap with size 10
hash_map = SimpleHashMap(10)

# Put some key-value pairs into the hash map
hash_map.put('name', 'John Doe')
hash_map.put('age', 30)
hash_map.put('city', 'New York')

# Get a value from the hash map using its key
print(hash_map.get('name'))  # Output: John Doe

# Delete a key-value pair from the hash map
hash_map.delete('age')

# Try to get a deleted key's value (should return None)
print(hash_map.get('age'))  # Output: None