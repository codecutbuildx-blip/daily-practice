# Introduction to HashMap in Python

# Import the built-in dict class
from collections import defaultdict

# Define a class to represent a key-value pair in the HashMap
class Key:
    def __init__(self, key):
        self.key = key

# Define a class to represent a HashMap
class HashMap:
    def __init__(self):
        # Initialize the HashMap as a dictionary
        self.hash_map = defaultdict(int)
        self.size = 100  # Initial size of the HashMap

    # Method to insert a key-value pair into the HashMap
    def insert(self, key, value):
        # Calculate the index using the hash function
        index = hash(key) % self.size
        # If the key already exists, update its value
        if key in self.hash_map:
            self.hash_map[key] = value
        # Otherwise, add the key-value pair to the HashMap
        else:
            self.hash_map[key] = value

    # Method to get the value associated with a key from the HashMap
    def get(self, key):
        # Calculate the index using the hash function
        index = hash(key) % self.size
        # If the key exists in the HashMap, return its value
        if key in self.hash_map:
            return self.hash_map[key]
        # Otherwise, return None
        else:
            return None

    # Method to delete a key-value pair from the HashMap
    def delete(self, key):
        # Calculate the index using the hash function
        index = hash(key) % self.size
        # If the key exists in the HashMap, remove it
        if key in self.hash_map:
            del self.hash_map[key]

# Create an instance of the HashMap
hash_map = HashMap()

# Insert some key-value pairs into the HashMap
hash_map.insert('apple', 5)
hash_map.insert('banana', 7)
hash_map.insert('cherry', 3)

# Get the values associated with some keys from the HashMap
print(hash_map.get('apple'))  # Output: 5
print(hash_map.get('banana'))  # Output: 7
print(hash_map.get('cherry'))  # Output: 3

# Delete a key-value pair from the HashMap
hash_map.delete('banana')

# Get the value associated with the deleted key
print(hash_map.get('banana'))  # Output: None