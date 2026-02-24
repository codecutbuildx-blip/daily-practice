# Divide and Conquer in Python
# This script provides an implementation of the Divide and Conquer algorithm

def merge_sort(arr):
    # Base Case
    # If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively call merge_sort on both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # Create an empty list to store the merged result
    merged = []
    left_index = 0
    right_index = 0

    # Merge the two lists by comparing elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left list
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Append any remaining elements from the right list
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Return the merged list
    return merged

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))