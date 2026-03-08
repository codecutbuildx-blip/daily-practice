# Trie Data Structure in Python

# Importing the necessary module
import collections

# Defining the TrieNode class
class TrieNode:
    def __init__(self):
        # Each node will have a dictionary to store children and a boolean to mark the end of a word
        self.children = collections.defaultdict(TrieNode)
        self.is_end_of_word = False

# Defining the Trie class
class Trie:
    def __init__(self):
        # The root of the trie
        self.root = TrieNode()

    # Method to insert a word into the trie
    def insert(self, word):
        # Start at the root
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    # Method to search for a word in the trie
    def search(self, word):
        # Start at the root
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the children, the word is not in the trie
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # If we've reached the end of the word and it's marked as the end of a word, return True
        return node.is_end_of_word

    # Method to check if a prefix exists in the trie
    def starts_with(self, prefix):
        # Start at the root
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the children, the prefix is not in the trie
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # If we've reached the end of the prefix, return True
        return True

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("orange"))  # Output: True
print(trie.search("grape"))   # Output: False

print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("ora"))  # Output: True
print(trie.starts_with("gra"))  # Output: False