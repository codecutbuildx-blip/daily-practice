# Divide and Conquer Algorithm
# ==============================
# This code provides an example of the divide and conquer algorithm
# using the merge sort algorithm.

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # Create a new array to store the merged result
    merged = []
    left_index = 0
    right_index = 0

    # Merge the two arrays by comparing elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Test the merge sort algorithm
def test_merge_sort():
    # Create a test array
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)

    # Sort the array using merge sort
    sorted_array = merge_sort(test_array)
    print("Sorted array:", sorted_array)


# Run the test
test_merge_sort()