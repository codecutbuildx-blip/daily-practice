# Two Pointers Code
# ===============

## Problem Statement

Given an array of integers and an integer k, return the k-th smallest element from the array.

## Solution

We will use two pointers to solve this problem efficiently.

```python
def findKthSmallest(nums, k):
    """
    Returns the k-th smallest element in the given array.
    
    Parameters:
    nums (list): The input array of integers.
    k (int): The position of the desired element.
    
    Returns:
    int: The k-th smallest element in the array.
    """

    # Sort the array in ascending order
    nums.sort()

    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(nums) - 1

    # Continue until we find the k-th smallest element
    while True:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the middle element is equal to the k-th smallest element, return it
        if nums[mid] == nums[k - 1]:
            return nums[mid]
        
        # If the middle element is less than the k-th smallest element, move the left pointer to the right
        elif nums[mid] < nums[k - 1]:
            left = mid + 1
        
        # If the middle element is greater than the k-th smallest element, move the right pointer to the left
        else:
            right = mid - 1


# Run the code with an example array and k=3
if __name__ == "__main__":
    nums = [7,10,4,3,20,15]
    k = 3
    result = findKthSmallest(nums, k)
    print("The {}-th smallest element is: {}".format(k, result))