# Divide and Conquer: Merge Sort Algorithm

This code implements the merge sort algorithm, a popular divide-and-conquer technique used for sorting arrays of elements. The merge sort algorithm works by recursively dividing the array into smaller subarrays until each subarray contains only one element, and then merging these subarrays back together in sorted order.

## Code
```python
def merge_sort(arr):
    # Base case: if the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # While both lists have elements, compare and add the smaller one to the merged list
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Add any remaining elements from either list
    merged.extend(left)
    merged.extend(right)

    return merged


# Example usage and test
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

    # Test with random data
    import random

    random_array = [random.randint(1, 100) for _ in range(10)]
    print("\nRandom array:", random_array)
    sorted_random_array = merge_sort(random_array)
    print("Sorted random array:", sorted_random_array)