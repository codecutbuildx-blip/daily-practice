# Segment Tree Implementation in Python

class SegmentTree:
    def __init__(self, arr):
        # Initialize the segment tree with a given array
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        # Build the segment tree recursively by dividing the array into two halves
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            # Update the node with the minimum of its left and right child
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, left, right):
        # Query the segment tree for a given range
        if start > right or end < left:
            return float('inf')
        elif start >= left and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            # Recursively query the left and right child
            return min(self.query(2 * node + 1, start, mid, left, right),
                       self.query(2 * node + 2, mid + 1, end, left, right))

    def update(self, node, start, end, index, val):
        # Update the segment tree for a given range
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            # Recursively update the left and right child
            if index <= mid:
                self.update(2 * node + 1, start, mid, index, val)
            else:
                self.update(2 * node + 2, mid + 1, end, index, val)
            # Update the node with the minimum of its left and right child
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

# Test the segment tree implementation
arr = [10, 20, 30, 40, 50]
segment_tree = SegmentTree(arr)

print("Querying segment tree for range (1, 4):", segment_tree.query(0, 0, len(arr) - 1, 1, 3))
print("Updating the segment tree at index 2 with value 60:", segment_tree.update(0, 0, len(arr) - 1, 2, 60))

arr = [10, 20, 30, 40, 50]
segment_tree = SegmentTree(arr)

# Run query
print("Querying segment tree for range (3, 4):", segment_tree.query(0, 0, len(arr) - 1, 3, 4))

# Run update
segment_tree.update(0, 0, len(arr) - 1, 2, 60)

# Run query again to see