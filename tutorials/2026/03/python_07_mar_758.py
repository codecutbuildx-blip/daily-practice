# Binary Search Algorithm in Python
# This script demonstrates the implementation of binary search algorithm in Python.

def binary_search(arr, target):
    # Initialize two pointers at the start and end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue the search until the two pointers meet
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target is found, return its index
        if arr[mid] == target:
            return mid
        
        # If the target is less than the middle element, move the right pointer
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is greater than the middle element, move the left pointer
        else:
            left = mid + 1
    
    # If the target is not found, return -1
    return -1

# Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")

# Test the binary search function with a sorted array
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")

# Test the binary search function with an unsorted array
arr = [16, 23, 2, 5, 8, 12, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")