# Tree Traversal Algorithms
================================

This script teaches the three primary tree traversal algorithms: Inorder, Preorder, and Postorder. Understanding these algorithms is crucial for traversing trees in a systematic way.

```python
class Node:
    # Define a class to represent a node in the tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    # Function to perform an Inorder traversal of the tree
    if root is not None:
        # Recursively traverse the left subtree
        inorder_traversal(root.left)
        print(root.value, end=" ")  # Visit the current node
        # Recursively traverse the right subtree
        inorder_traversal(root.right)

def preorder_traversal(root):
    # Function to perform a Preorder traversal of the tree
    if root is not None:
        print(root.value, end=" ")  # Visit the current node
        # Recursively traverse the left subtree
        preorder_traversal(root.left)
        # Recursively traverse the right subtree
        preorder_traversal(root.right)

def postorder_traversal(root):
    # Function to perform a Postorder traversal of the tree
    if root is not None:
        # Recursively traverse the left subtree
        postorder_traversal(root.left)
        # Recursively traverse the right subtree
        postorder_traversal(root.right)
        print(root.value, end=" ")  # Visit the current node

# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal:")
inorder_traversal(root)
print("\nPreorder traversal:")
preorder_traversal(root)
print("\nPostorder traversal:")
postorder_traversal(root)