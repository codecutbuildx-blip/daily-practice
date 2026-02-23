# Prefix Sum Algorithm in Python
=====================================================

### Overview

Prefix sum, also known as cumulative sum, is a technique used to calculate the sum of elements in an array without iterating over the entire array. This technique is particularly useful when you need to access the sum of elements in a range.

### Algorithm

The prefix sum algorithm works by maintaining an array of prefix sums, where each element at index i represents the sum of elements from index 0 to i.

### Code

```python
def calculate_prefix_sums(arr):
    # Create a list to store the prefix sums
    prefix_sums = [0] * (len(arr) + 1)

    # Calculate the prefix sums
    for i in range(len(arr)):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]

    return prefix_sums

def query_prefix_sum(prefix_sums, start, end):
    # Calculate the sum of elements from start to end
    return prefix_sums[end] - prefix_sums[start]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sums = calculate_prefix_sums(arr)
print("Prefix Sums:", prefix_sums)

# Query the sum of elements from index 1 to 3
print("Sum of elements from index 1 to 3:", query_prefix_sum(prefix_sums, 1, 3))