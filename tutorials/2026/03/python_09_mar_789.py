# Monotonic Stack Implementation in Python

class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to store the stack
        self.stack = []

    def is_monotonic(self):
        # Check if the stack is monotonic
        # A stack is monotonic if it's either strictly increasing or strictly decreasing
        return self.is_strictly_increasing() or self.is_strictly_decreasing()

    def is_strictly_increasing(self):
        # Check if the stack is strictly increasing
        # A stack is strictly increasing if all elements are in sorted order
        return self.is_sorted()

    def is_strictly_decreasing(self):
        # Check if the stack is strictly decreasing
        # A stack is strictly decreasing if all elements are in reverse sorted order
        return self.is_reverse_sorted()

    def is_sorted(self):
        # Check if the stack is sorted
        # A stack is sorted if all elements are in sorted order
        return all(self.stack[i] <= self.stack[i+1] for i in range(len(self.stack)-1))

    def is_reverse_sorted(self):
        # Check if the stack is reverse sorted
        # A stack is reverse sorted if all elements are in reverse sorted order
        return all(self.stack[i] >= self.stack[i+1] for i in range(len(self.stack)-1))

    def push(self, x):
        # Push an element onto the stack
        self.stack.append(x)

    def pop(self):
        # Pop an element from the stack
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack.pop()


# Example usage
if __name__ == "__main__":
    # Create a monotonic stack
    stack = MonotonicStack()

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    # Check if the stack is monotonic
    print("Is stack monotonic?", stack.is_monotonic())  # True

    # Pop elements from the stack
    print("Popped element:", stack.pop())  # 5
    print("Popped element:", stack.pop())  # 4
    print("Popped element:", stack.pop())  # 3
    print("Popped element:", stack.pop())  # 2
    print("Popped element:", stack.pop())  # 1

    # Check if the stack is monotonic after popping
    print("Is stack monotonic?", stack.is_monotonic())  # False