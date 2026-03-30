# Merge Sort Algorithm in Python
=====================================

Merge sort is a popular sorting algorithm that uses the divide-and-conquer technique to sort elements of an array.

```python
def merge_sort(arr):
    # If the length of the array is 1 or less, return the array (since it's already sorted)
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively call merge_sort on both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged array
    merged = []
    
    # While both lists have elements, keep removing and appending the smallest one to the merged list
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # If there are remaining elements in either list, append them to the merged list
    merged.extend(left)
    merged.extend(right)

    return merged


# Test the merge sort algorithm with an example array
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)