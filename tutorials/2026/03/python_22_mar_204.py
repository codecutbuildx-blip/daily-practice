class TrieNode:
    def __init__(self):
        # Initialize an empty dictionary to store children nodes
        self.children = {}
        # Initialize a boolean flag to mark the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the root node of the trie
        self.root = TrieNode()

    def insert(self, word):
        # Start at the root node
        current_node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the children dictionary, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the child node
            current_node = current_node.children[char]
        # Mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        # Start at the root node
        current_node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the children dictionary, return False
            if char not in current_node.children:
                return False
            # Move to the child node
            current_node = current_node.children[char]
        # Return True if the word ends at a node marked as end of word, False otherwise
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        # Start at the root node
        current_node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the children dictionary, return False
            if char not in current_node.children:
                return False
            # Move to the child node
            current_node = current_node.children[char]
        # Return True because we found a match for the prefix
        return True

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("banana")) # Output: True
print(trie.search("banan"))  # Output: False

print(trie.starts_with("ap")) # Output: True
print(trie.starts_with("a"))   # Output: True