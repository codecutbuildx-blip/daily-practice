# Divide and Conquer Algorithm
# A divide and conquer algorithm is a type of algorithm that solves a problem by breaking it down into smaller sub-problems, solving each sub-problem recursively, and then combining the solutions to the sub-problems to solve the original problem.

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle of the array.
    mid = len(arr) // 2

    # Divide the array into two halves.
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine the sorted halves into a single sorted array.
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []

    # Initialize indices for the left and right arrays.
    left_index = 0
    right_index = 0

    # Compare elements from the left and right arrays and add the smaller one to the merged list.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left array.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add any remaining elements from the right array.
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Return the merged list.
    return merged


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))