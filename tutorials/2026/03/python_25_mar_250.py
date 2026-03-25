# Binary Search Algorithm in Python

def binary_search(arr, target):
    # Initialize the left and right pointers
    left = 0
    right = len(arr) - 1
    
    # Continue the search until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Compare the target with the middle element of the array
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the target is greater than the middle element, update the left pointer to be one more than the middle index
            left = mid + 1
        else:
            # If the target is less than the middle element, update the right pointer to be one less than the middle index
            right = mid - 1
    
    # Return -1 to indicate that the target was not found in the array
    return -1

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

index = binary_search(arr, target)

if index != -1:
    print(f"Target found at index {index}")
else:
    print("Target not found in the array")

# Test case: Target is present in the array
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
print(binary_search(arr, target))

# Test case: Target is not present in the array
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 100
print(binary_search(arr, target))