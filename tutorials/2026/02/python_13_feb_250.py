# Segment Tree
# ===========

class SegmentTree:
    def __init__(self, arr):
        """
        Initialize the segment tree with an array.
        
        Args:
            arr (list): The input array.
        """
        n = len(arr)
        # Calculate the size of the segment tree
        self.tree = [0] * (4 * n)
        self.build_tree(arr, 0, 0, n - 1)

    def build_tree(self, arr, node, start, end):
        """
        Build the segment tree recursively.
        
        Args:
            arr (list): The input array.
            node (int): The current node index.
            start (int): The start index of the current segment.
            end (int): The end index of the current segment.
        """
        # Base case: If the segment is empty, return
        if start > end:
            return
        # Calculate the middle point of the segment
        mid = (start + end) // 2
        # Recursively build the left and right subtrees
        self.build_tree(arr, 2 * node + 1, start, mid)
        self.build_tree(arr, 2 * node + 2, mid + 1, end)
        # Initialize the current node with the sum of its children
        self.tree[node] = arr[mid] if start == end else \
                        self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        """
        Query the segment tree recursively.
        
        Args:
            node (int): The current node index.
            start (int): The start index of the current segment.
            end (int): The end index of the current segment.
            left (int): The start index of the query segment.
            right (int): The end index of the query segment.
        
        Returns:
            int: The sum of the values in the query segment.
        """
        # Base case: If the query segment is empty, return 0
        if start > end or left > right:
            return 0
        # Calculate the middle point of the segment
        mid = (start + end) // 2
        # Check if the entire query segment is within the current segment
        if left <= start and end <= right:
            return self.tree[node]
        # Recursively query the left or right subtrees
        elif left <= mid:
            return self.query(2 * node + 1, start, mid, left, right)
        else:
            return self.query(2 * node + 2, mid + 1, end, left, right)

    def update(self, node, start, end, idx, val):
        """
        Update the segment tree recursively.
        
        Args:
            node (int): The current node index.
            start (int): The start index of the current segment.
            end (int): The end index of the current segment.
            idx (int): The index to update in the current segment.
            val (int): The new value for the updated index.
        """
        # Base case: If the segment is empty, return
        if start > end:
            return
        # Calculate the middle point of the segment
        mid = (