# Segment Tree in Python

class SegmentTree:
    def __init__(self, nums):
        """
        Initialize the Segment Tree.

        Args:
            nums (list): A list of numbers.
        """
        self.n = len(nums)
        # Calculate the size of the segment tree
        self.size = 1 << (self.n - 1).bit_length()
        # Allocate space for the segment tree
        self.tree = [0] * (2 * self.size)

        # Build the segment tree
        for i in range(self.n):
            self.tree[self.size + i] = nums[i]
        for i in range(self.size - 1, 0, -1):
            # Update the tree using the formula: f(x, y) = min(x, y)
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        """
        Query the segment tree for a range of values.

        Args:
            left (int): The starting index of the range.
            right (int): The ending index of the range.

        Returns:
            int: The minimum value in the range.
        """
        # Calculate the indices of the left and right subtrees
        left_index = self.size + left
        right_index = self.size + right

        # Initialize the result as infinity
        result = float('inf')
        # Traverse up the tree, updating the result using the formula: f(x, y) = min(x, y)
        while left_index < right_index:
            if left_index & 1:
                result = min(result, self.tree[left_index])
                left_index += 1
            if right_index & 1:
                right_index -= 1
                result = min(result, self.tree[right_index])
            left_index >>= 1
            right_index >>= 1

        # Return the minimum value in the range
        return result

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 1, 4]
    st = SegmentTree(nums)
    print("Minimum value on index 0:", st.query(0, 0))
    print("Minimum value on index 3:", st.query(3, 3))
    print("Minimum value in range (1, 3):", st.query(1, 3))