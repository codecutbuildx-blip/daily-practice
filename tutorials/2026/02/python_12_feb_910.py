class SegmentTree:
    def __init__(self, arr):
        # The size of the segment tree is twice the size of the input array
        n = len(arr)
        self.tree = [0] * (4 * n)
        self.build_tree(arr, 0, n - 1, 0)

    def build_tree(self, arr, start, end, index):
        # Base case: if start and end are same, it is a leaf node
        if start == end:
            self.tree[index] = arr[start]
        else:
            # Divide the range into two halves
            mid = (start + end) // 2

            # Recursively build the left and right subtrees
            self.build_tree(arr, start, mid, 2 * index + 1)
            self.build_tree(arr, mid + 1, end, 2 * index + 2)

            # Store the maximum value in the current node
            self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def query(self, start, end):
        # Function to find the maximum sum of a segment
        n = len(self.tree) // 2
        return self.query_helper(start, end, 0, 0, n - 1)

    def query_helper(self, start, end, index, tree_start, tree_end):
        # Base case: if start and end are same, it is a leaf node
        if start > tree_end or end < tree_start:
            return float('-inf')
        
        # If the segment is completely covered by the current subtree
        if start <= tree_start and end >= tree_end:
            return self.tree[index]
        
        # Divide the range into two halves
        mid = (tree_start + tree_end) // 2

        # Recursively query the left and right subtrees
        left_max = self.query_helper(start, min(end, mid), 2 * index + 1, tree_start, mid)
        right_max = self.query_helper(max(start, mid + 1), end, 2 * index + 2, mid + 1, tree_end)

        # Return the maximum of the two subtrees
        return max(left_max, right_max)


# Example usage:
if __name__ == "__main__":
    arr = [3, -5, 0, -7, 10]
    segment_tree = SegmentTree(arr)
    print("Maximum sum of segments:")
    for i in range(1, len(arr)):
        print(f"Sum from index {i-1} to {i}: {segment_tree.query(i-1, i)}")