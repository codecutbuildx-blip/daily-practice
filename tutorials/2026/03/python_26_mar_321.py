# Merge Sort Algorithm in Python

def merge_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together.
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []
    
    # Continue merging until one of the lists is exhausted.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    # Append any remaining elements from either list.
    merged.extend(left)
    merged.extend(right)
    
    return merged


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

```

Output:

```
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]