# Hash Map Implementation in Python
#=====================================

class HashMap:
    def __init__(self, size):
        # Initialize the hash map with a given size
        self.size = size
        # Create an array of empty lists to store key-value pairs
        self.table = [None] * size

    def _hash_function(self, key):
        # Calculate the index using the hash function (simple modulo operation)
        return hash(key) % self.size

    def put(self, key, value):
        # Find the index for the given key and update or insert the value
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    # Update existing key-value pair
                    pair[1] = value
                    return
            self.table[index].append((key, value))

    def get(self, key):
        # Retrieve the value associated with a given key
        index = self._hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        # Remove the key-value pair associated with a given key
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    del self.table[index][i]
                    return

    def display(self):
        # Print the current contents of the hash map
        for index, pairs in enumerate(self.table):
            print(f"Index {index}:")
            for pair in pairs:
                print(pair[0], ":", pair[1])
            if pairs:
                print()


# Run an example with a hash map of size 10
hash_map = HashMap(10)
hash_map.put("apple", 5)
hash_map.put("banana", 7)
hash_map.put("cherry", 3)
print("Hash Map Contents:")
hash_map.display()
print("Retrieving value for 'banana':", hash_map.get("banana"))
hash_map.remove("cherry")
print("Hash Map Contents after removal:", end=" ")
hash_map.display()