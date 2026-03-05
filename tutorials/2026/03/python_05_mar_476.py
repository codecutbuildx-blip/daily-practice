class TrieNode:
    # Initialize a new node in the trie
    def __init__(self):
        # Store the children nodes in a dictionary for efficient lookup
        self.children = {}
        # Store the end-of-word flag
        self.is_end_of_word = False

class Trie:
    # Initialize a new trie
    def __init__(self):
        # Start with an empty root node
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the final node as the end of a word
        node.is_end_of_word = True

    # Search for a word in the trie
    def search(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return whether the final node is the end of a word
        return node.is_end_of_word

    # Check if a prefix exists in the trie
    def starts_with(self, prefix):
        # Start at the root node
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if we've reached the end of the prefix
        return True

# Create a new trie
trie = Trie()

# Insert some words into the trie
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")

# Test the trie
print(trie.search("apple"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("cherry"))  # Output: True
print(trie.search("grape"))  # Output: False

print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("che"))  # Output: True
print(trie.starts_with("gra"))  # Output: False