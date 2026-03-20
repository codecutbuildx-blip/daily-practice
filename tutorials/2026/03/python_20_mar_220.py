# Hash Map Implementation in Python
# _______________________________________

class Node:
    """Represents an individual node in the hash map."""
    
    def __init__(self, key, value):
        # Initialize a new node with a given key and value.
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    """A basic implementation of a hash map."""
    
    def __init__(self, size=1000):
        # Initialize the hash map with a specified size.
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # Calculate the hash value for a given key using a simple modulo operation.
        return hash(key) % self.size

    def put(self, key, value):
        # Add or update a key-value pair in the hash map.
        index = self._hash(key)
        
        if self.table[index] is None:
            # If the table at the given index is empty, create a new node.
            self.table[index] = Node(key, value)
        else:
            # If the table at the given index is not empty, search for an existing key.
            current_node = self.table[index]
            while current_node.next is not None:
                if current_node.key == key:
                    # If a matching key is found, update its value.
                    current_node.value = value
                    return
                current_node = current_node.next

            # If no matching key is found, add a new node to the end of the list.
            current_node.next = Node(key, value)

    def get(self, key):
        # Retrieve the value associated with a given key from the hash map.
        index = self._hash(key)
        
        if self.table[index] is None:
            # If the table at the given index is empty, return None.
            return None
        
        current_node = self.table[index]
        while current_node.next is not None:
            if current_node.key == key:
                # If a matching key is found, return its value.
                return current_node.value
            current_node = current_node.next
        
        # If no matching key is found, return None.
        return None

    def delete(self, key):
        """Remove a key-value pair from the hash map."""
        
        index = self._hash(key)
        if self.table[index] is None:
            # If the table at the given index is empty, do nothing.
            return
        
        current_node = self.table[index]
        previous_node = None
        while current_node.next is not None:
            if current_node.key == key:
                # If a matching key is found, remove it from the list.
                if previous_node is None:
                    self.table[index] = current_node.next
                else:
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

# Example usage
if __name__ == "__main__":
    hash_map = HashMap()
    
    # Add key-value pairs to the hash map.
    hash_map.put("apple", 5)
    hash_map.put("banana", 7)
    hash_map.put("orange", 3)
    
    # Retrieve values from the hash map.
    print(hash_map.get("apple"))  # Output: 5
    print(hash_map.get