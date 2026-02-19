# Tree Traversal Algorithms in Python

This code teaches three fundamental tree traversal algorithms: In-Order, Pre-Order, and Post-Order Traversal.

Tree traversal is a crucial concept in computer science that allows us to visit each node in a tree data structure exactly once. The order of visitation depends on the algorithm used. Each algorithm has its own strengths and weaknesses, making them suitable for different applications.

## In-Class Code

```python
class Node:
    """Represents a node in a binary tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):
    """
    Performs an in-order traversal of the binary tree.

    Args:
    node: The root node of the binary tree.
    """
    # Base case: If the node is None, return immediately
    if node is None:
        return

    # Recursively traverse the left subtree
    inorder_traversal(node.left)

    # Visit the current node
    print(node.value, end=" ")

    # Recursively traverse the right subtree
    inorder_traversal(node.right)


def preorder_traversal(node):
    """
    Performs a pre-order traversal of the binary tree.

    Args:
    node: The root node of the binary tree.
    """
    # Base case: If the node is None, return immediately
    if node is None:
        return

    # Visit the current node
    print(node.value, end=" ")

    # Recursively traverse the left subtree
    preorder_traversal(node.left)

    # Recursively traverse the right subtree
    preorder_traversal(node.right)


def postorder_traversal(node):
    """
    Performs a post-order traversal of the binary tree.

    Args:
    node: The root node of the binary tree.
    """
    # Base case: If the node is None, return immediately
    if node is None:
        return

    # Recursively traverse the left subtree
    postorder_traversal(node.left)

    # Recursively traverse the right subtree
    postorder_traversal(node.right)

    # Visit the current node
    print(node.value, end=" ")


# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("In-Order Traversal:")
    inorder_traversal(root)
    print()

    print("Pre-Order Traversal:")
    preorder_traversal(root)
    print()

    print("Post-Order Traversal:")
    postorder_traversal(root)