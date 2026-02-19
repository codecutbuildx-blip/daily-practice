# Tree Traversal Algorithms in Python
=====================================

This script demonstrates three fundamental tree traversal algorithms: Inorder, Preorder, and Postorder traversal. These algorithms are crucial for traversing and manipulating trees in computer science.

## Importing necessary libraries

```python
from collections import deque
```

## Defining a Node class

The `Node` class represents each node in the binary tree. Each node has a value and pointers to its left and right children.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## Defining a BinaryTree class

The `BinaryTree` class represents the binary tree itself. It contains methods for traversing the tree using Inorder, Preorder, and Postorder algorithms.

```python
class BinaryTree:
    def __init__(self):
        self.root = None
```

## Implementing Inorder traversal algorithm

Inorder traversal visits the left subtree, the current node, and then the right subtree. This is useful when we want to process nodes in ascending order or in a specific order based on their values.

```python
    def inorder(self):
        # Initialize an empty list to store the visited nodes
        result = []
        
        # Define a helper function for recursive traversal
        def traverse(node):
            if node:
                # Traverse the left subtree
                traverse(node.left)
                
                # Append the current node's value to the result list
                result.append(node.value)
                
                # Traverse the right subtree
                traverse(node.right)
        
        # Start traversing from the root node
        traverse(self.root)
        
        return result
```

## Implementing Preorder traversal algorithm

Preorder traversal visits the current node, then its left and right subtrees. This is useful when we want to create a copy of the tree or process nodes in a specific order based on their values.

```python
    def preorder(self):
        # Initialize an empty list to store the visited nodes
        result = []
        
        # Define a helper function for recursive traversal
        def traverse(node):
            if node:
                # Append the current node's value to the result list
                result.append(node.value)
                
                # Traverse the left subtree
                traverse(node.left)
                
                # Traverse the right subtree
                traverse(node.right)
        
        # Start traversing from the root node
        traverse(self.root)
        
        return result
```

## Implementing Postorder traversal algorithm

Postorder traversal visits the left and right subtrees, then the current node. This is useful when we want to delete a tree or process nodes in a specific order based on their values.

```python
    def postorder(self):
        # Initialize an empty list to store the visited nodes
        result = []
        
        # Define a helper function for recursive traversal
        def traverse(node):
            if node:
                # Traverse the left subtree
                traverse(node.left)
                
                # Traverse the right subtree
                traverse(node.right)
                
                # Append the current node's value to the result list
                result.append(node.value)
        
        # Start traversing from the root node
        traverse(self.root)
        
        return result
```

## Example usage and test