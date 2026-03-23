# Hash Map Implementation in Python

# Importing the necessary modules
import math

# Defining a class to represent the hash map
class HashMap:
    def __init__(self, size):
        # Initializing an empty list of buckets
        self.size = size
        self.buckets = [[] for _ in range(size)]

    # Function to insert a key-value pair into the hash map
    def insert(self, key, value):
        # Calculate the index using the hash function
        index = self._hash(key)

        # Iterate through each bucket and find an empty slot or a collision with the same key
        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0] == key:
                self.buckets[index][i] = (key, value)
                return

        # If no collision, append a new bucket
        self.buckets[index].append((key, value))

    # Function to retrieve the value associated with a given key
    def get(self, key):
        index = self._hash(key)

        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0] == key:
                return self.buckets[index][i][1]

        return None

    # Function to update the value associated with a given key
    def update(self, key, value):
        index = self._hash(key)

        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0] == key:
                self.buckets[index][i] = (key, value)
                return

        # If no collision, append a new bucket
        self.buckets[index].append((key, value))

    # Function to delete the key-value pair associated with a given key
    def delete(self, key):
        index = self._hash(key)

        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0] == key:
                del self.buckets[index][i]
                return

        # If no collision, the key does not exist in the hash map
        pass

    # Helper function to calculate the index using the hash function
    def _hash(self, key):
        return sum(math.pow(31, -i) * ord(c) for i, c in enumerate(str(key))) % self.size


# Example usage:
if __name__ == "__main__":
    # Creating a new hash map with a size of 10
    hash_map = HashMap(10)

    # Inserting key-value pairs into the hash map
    hash_map.insert("John", "Developer")
    hash_map.insert("Jane", "Designer")

    # Retrieving the value associated with a given key
    print(hash_map.get("John"))  # Output: Developer

    # Updating the value associated with a given key
    hash_map.update("John", "Software Engineer")
    print(hash_map.get("John"))  # Output: Software Engineer

    # Deleting the key-value pair associated with a given key
    hash_map.delete("Jane")

    # Trying to retrieve the deleted key's value
    print(hash_map.get("Jane"))  # Output: None