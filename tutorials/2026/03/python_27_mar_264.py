# Hash Map Implementation in Python
#=====================================

class HashMap:
    def __init__(self, size):
        # Initialize the hashmap with a given size
        self.size = size
        # Create an empty list of buckets
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calculate the index using a simple hash function
        return hash(key) % self.size

    def insert(self, key, value):
        # Hash the key and find the corresponding bucket
        index = self.hash_function(key)
        # Check if the key already exists in the hashmap
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                # If it does, update its value
                self.buckets[index][i] = (key, value)
                break
        else:
            # If not, add a new entry to the bucket
            self.buckets[index].append((key, value))

    def get(self, key):
        # Hash the key and find the corresponding bucket
        index = self.hash_function(key)
        # Check if the key exists in the hashmap
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        # Hash the key and find the corresponding bucket
        index = self.hash_function(key)
        # Iterate over the entries in the bucket
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                # Remove the entry from the bucket
                del self.buckets[index][i]
                break

# Create a hashmap with a size of 10
hashmap = HashMap(10)

# Insert some values into the hashmap
hashmap.insert('key1', 'value1')
hashmap.insert('key2', 'value2')
hashmap.insert('key3', 'value3')

# Retrieve values from the hashmap using their keys
print(hashmap.get('key1'))  # Output: value1
print(hashmap.get('key2'))  # Output: value2

# Delete a key-value pair from the hashmap
hashmap.delete('key2')
print(hashmap.get('key2'))  # Output: None

# Run the hashmap for testing
class Key:
    def __init__(self, name):
        self.name = name

class Value:
    def __init__(self, value):
        self.value = value

def test_hashmap():
    key1 = Key('Key1')
    key2 = Key('Key2')
    value1 = Value('Value1')
    value2 = Value('Value2')

    hashmap.insert(key1.name, value1)
    hashmap.insert(key2.name, value2)

    print(hashmap.get(key1.name).value)  # Output: Value1
    print(hashmap.get(key2.name).value)  # Output: Value2

test_hashmap()