# Binary Search Algorithm in Python
=====================================

### Overview

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

### Code

```python
def binary_search(arr, target):
    """
    Searches for the target element in the given sorted array using binary search.

    Args:
        arr (list): A sorted list of elements.
        target (int): The element to be searched.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    # Initialize the low and high pointers
    low = 0
    high = len(arr) - 1

    # Continue the search until the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2

        # If the target element is found at the mid index, return the index
        if arr[mid] == target:
            return mid
        # If the target element is less than the element at the mid index, update the high pointer
        elif arr[mid] > target:
            high = mid - 1
        # If the target element is greater than the element at the mid index, update the low pointer
        else:
            low = mid + 1

    # If the target element is not found, return -1
    return -1


# Example usage
if __name__ == "__main__":
    # Define a sorted list of elements
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    # Define the target element to be searched
    target = 23

    # Call the binary search function
    result = binary_search(arr, target)

    # Print the result
    if result != -1:
        print(f"Target element {target} found at index {result}.")
    else:
        print(f"Target element {target} not found in the list.")