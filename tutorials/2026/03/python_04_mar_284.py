# Segment Tree Implementation in Python
#=====================================

import random

class SegmentTree:
    # Initialize segment tree with values from 1 to n
    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (4 * self.n)
        self.build_tree(values, 0, 0, self.n - 1)

    # Build segment tree recursively
    def build_tree(self, values, node, start, end):
        # Base case: leaf node
        if start == end:
            self.tree[node] = values[start]
            return

        # Calculate midpoint
        mid = (start + end) // 2
        # Recursively build left and right subtrees
        self.build_tree(values, 2 * node + 1, start, mid)
        self.build_tree(values, 2 * node + 2, mid + 1, end)
        # Combine values from left and right subtrees
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # Update value at index
    def update(self, index, value):
        # Base case: leaf node
        if index < 0 or index >= self.n:
            return
        # Calculate midpoint
        mid = (self.n - 1) // 2
        # Recursively update left and right subtrees
        self.update(index, value, 0, 0, mid)
        self.update(index, value, 0, mid + 1, self.n - 1)
        # Update value in current node
        self.tree[0] = self.tree[1] + self.tree[2]

    # Recursively update value at index
    def update_helper(self, index, value, node, start, end):
        # Base case: leaf node
        if start == end:
            self.tree[node] = value
            return
        # Calculate midpoint
        mid = (start + end) // 2
        # Check if index is in left subtree
        if index <= mid:
            self.update_helper(index, value, 2 * node + 1, start, mid)
        # Check if index is in right subtree
        else:
            self.update_helper(index, value, 2 * node + 2, mid + 1, end)
        # Combine values from left and right subtrees
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # Get sum of values in range [start, end]
    def query(self, start, end):
        # Base case: empty range
        if start > end:
            return 0
        # Calculate midpoint
        mid = (start + end) // 2
        # Recursively get sum of values in left and right subtrees
        left_sum = self.query(start, mid)
        right_sum = self.query(mid + 1, end)
        # Combine values from left and right subtrees
        return left_sum + right_sum

# Test the implementation
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    st =