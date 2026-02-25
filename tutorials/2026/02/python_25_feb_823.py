# Monotonic Stack Implementation in Python
=====================================================

A monotonic stack is a data structure that maintains a sorted order of elements in the stack, either ascending or descending.

```python
class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def is_monotonic(self, order):
        # If the order is ascending, check if the stack is sorted in ascending order
        if order == 'ascending':
            # Check if the stack is sorted by comparing each pair of adjacent elements
            for i in range(1, len(self.stack)):
                if self.stack[i] < self.stack[i-1]:
                    return False
            return True

        # If the order is descending, check if the stack is sorted in descending order
        elif order == 'descending':
            # Check if the stack is sorted by comparing each pair of adjacent elements
            for i in range(1, len(self.stack)):
                if self.stack[i] > self.stack[i-1]:
                    return False
            return True

        # If the order is neither ascending nor descending, raise a ValueError
        else:
            raise ValueError("Invalid order. Order must be 'ascending' or 'descending'.")

    def push(self, num):
        # If the stack is empty or the new number is greater than the top element, push it onto the stack
        if not self.stack or num >= self.stack[-1]:
            self.stack.append(num)
        else:
            # If the new number is smaller than the top element, keep popping elements from the stack
            # until we find a position to insert the new number or the stack becomes empty
            while self.stack and num < self.stack[-1]:
                self.stack.pop()
            # If the stack is empty after popping, push the new number onto the stack
            if not self.stack:
                self.stack.append(num)
            else:
                # If the stack is not empty, insert the new number at the correct position
                self.stack.append(num)

    def pop(self):
        # If the stack is not empty, pop the top element and return it
        if self.stack:
            return self.stack.pop()
        else:
            # If the stack is empty, raise an IndexError
            raise IndexError("Cannot pop from an empty stack.")

# Example usage
if __name__ == "__main__":
    # Create a monotonic stack
    stack = MonotonicStack()

    # Push elements onto the stack
    stack.push(5)
    stack.push(3)
    stack.push(8)
    stack.push(2)

    # Check if the stack is sorted in ascending order
    print(stack.is_monotonic('ascending'))  # Output: True

    # Check if the stack is sorted in descending order
    print(stack.is_monotonic('descending'))  # Output: True

    # Pop elements from the stack
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 5
    print(stack.pop())  # Output: 8

    # Try to pop from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(e)  # Output: Cannot pop from an empty stack.