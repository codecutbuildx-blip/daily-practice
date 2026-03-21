# Merge Sort Algorithm Implementation in Python

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    print(f"Splitting array into two halves of length {len(left_half)} and {len(right_half)}.")
    
    # Recursively sort the left and right halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    print("Merging sorted left and right halves.")
    
    # Merge the sorted left and right halves into a single sorted array.
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    print("Applying any remaining elements from either half.")
    
    # Append any remaining elements from the left or right halves.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    print("Returning the fully sorted array.")
    
    return merged


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array: {sorted_arr}")