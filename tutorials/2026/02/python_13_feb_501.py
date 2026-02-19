# Monotonic Stack Implementation in Python
=====================================================

This code teaches you how to implement a monotonic stack using Python. A monotonic stack is a data structure that stores elements in such a way that the top element is always greater than or equal to all other elements.

```python
class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to store the stack
        self.stack = []

    def push(self, val):
        # While the stack is not empty and the current value is smaller than the top element
        while self.stack and val < self.stack[-1]:
            # Pop the top element from the stack
            self.stack.pop()
        # Push the new value onto the stack
        self.stack.append(val)

    def pop(self):
        # If the stack is not empty, return the top element
        if self.stack:
            return self.stack.pop()
        # If the stack is empty, raise an IndexError
        else:
            raise IndexError("Cannot pop from an empty stack")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

# Example usage and test
if __name__ == "__main__":
    monotonic_stack = MonotonicStack()

    # Push elements onto the stack
    monotonic_stack.push(5)
    monotonic_stack.push(2)
    monotonic_stack.push(8)

    # Check if the stack is empty
    print("Is stack empty?", monotonic_stack.is_empty())

    # Pop elements from the stack
    print("Popped element:", monotonic_stack.pop())
    print("Popped element:", monotonic_stack.pop())

    # Check if the stack is empty
    print("Is stack empty?", monotonic_stack.is_empty())

    try:
        # Try to pop from an empty stack
        monotonic_stack.pop()
    except IndexError as e:
        print("Error:", e)