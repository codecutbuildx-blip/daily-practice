# Hash Map Implementation in Python

class HashMap:
    # Constructor to initialize the hash table with a given size
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Method to insert a key-value pair into the hash map
    def put(self, key, value):
        index = hash(key) % self.size  # Calculate the index using the hash function
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  # Check if the key already exists
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))  # Add the new key-value pair

    # Method to retrieve a value from the hash map by its key
    def get(self, key):
        index = hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:  # Check if the key exists
                return v
        return None

    # Method to remove a key-value pair from the hash map
    def remove(self, key):
        index = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  # Check if the key exists
                del self.table[index][i]
                return

    # Method to display the contents of the hash map
    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}:")
            for item in bucket:
                print(item)

# Example usage
if __name__ == "__main__":
    hash_map = HashMap(10)  # Create a hash map with size 10

    # Insert key-value pairs
    hash_map.put("apple", 1)
    hash_map.put("banana", 2)
    hash_map.put("orange", 3)

    # Retrieve values
    print(hash_map.get("apple"))  # Output: 1
    print(hash_map.get("banana"))  # Output: 2

    # Remove a key-value pair
    hash_map.remove("orange")

    # Display the contents of the hash map
    hash_map.display()