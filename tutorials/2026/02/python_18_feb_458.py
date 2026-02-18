# Hash Map Implementation in Python

class Node:
    # A node in the linked list to store key-value pairs
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # Main class for hash map implementation
    def __init__(self, size=1000):
        """
        Initializes the hash map with a given size.
        
        Args:
            size (int): The initial size of the hash map. Defaults to 1000.
        """
        self.size = size
        self.map = [None] * self.size

    def _hash(self, key):
        # Calculates the index for the given key using a simple hashing function
        return abs(hash(key) % self.size)

    def put(self, key, value):
        # Inserts or updates a key-value pair in the hash map
        index = self._hash(key)
        
        if not self.map[index]:
            self.map[index] = Node(key, value)
        else:
            node = self.map[index]
            
            while node.next:
                node = node.next
                
            node.next = Node(key, value)

    def get(self, key):
        # Retrieves the value associated with a given key from the hash map
        index = self._hash(key)
        
        if not self.map[index]:
            return None
        
        node = self.map[index]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
            
        return None

    def delete(self, key):
        # Removes a key-value pair from the hash map
        index = self._hash(key)
        
        if not self.map[index]:
            return
        
        node = self.map[index]
        
        if node.key == key:
            self.map[index] = node.next
            return
        
        prev_node = node
        while node.next:
            if node.next.key == key:
                prev_node.next = node.next.next
                return
            prev_node = node
            node = node.next

# Example usage of the hash map implementation
if __name__ == "__main__":
    # Creates a new hash map with an initial size of 1000
    hash_map = HashMap()
    
    # Inserts some key-value pairs into the hash map
    hash_map.put("apple", 1)
    hash_map.put("banana", 2)
    hash_map.put("cherry", 3)

    # Retrieves values from the hash map using keys
    print(hash_map.get("apple"))  # Output: 1
    print(hash_map.get("banana"))  # Output: 2
    print(hash_map.get("cherry"))  # Output: 3
    
    # Deletes a key-value pair from the hash map
    hash_map.delete("banana")
    
    # Retrieves values from the hash map using keys after deletion
    print(hash_map.get("apple"))  # Output: 1
    print(hash_map.get("banana"))  # Output: None
    print(hash_map.get("cherry"))  # Output: 3