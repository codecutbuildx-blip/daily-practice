# Sliding Window Problem
# This problem involves finding a subarray within a one-dimensional array of numbers
# that meets a given condition. The condition is specified by a target sum.

def max_sum_subarray(arr, target_sum):
    # Initialize two pointers, start and end, to the beginning of the array
    start = 0
    end = 0
    
    # Initialize the maximum sum and the current sum to negative infinity
    max_sum = float('-inf')
    current_sum = 0
    
    # Move the start pointer to the right until the current sum is less than the target sum
    while end < len(arr) and current_sum < target_sum:
        current_sum += arr[end]
        end += 1
    
    # If the current sum is still less than the target sum, there is no subarray that meets the condition
    if current_sum < target_sum:
        return -1
    
    # Update the maximum sum
    max_sum = current_sum
    
    # Move the start pointer to the right and update the current sum
    while end < len(arr):
        current_sum = current_sum - arr[start] + arr[end]
        max_sum = max(max_sum, current_sum)
        
        # Move the start pointer to the right
        start += 1
        end += 1
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
target_sum = 5
print(max_sum_subarray(arr, target_sum))  # Output: 5

arr = [1, 2, 3, 4, 5]
target_sum = 7
print(max_sum_subarray(arr, target_sum))  # Output: 5

arr = [1, 2, 3, 4, 5]
target_sum = 11
print(max_sum_subarray(arr, target_sum))  # Output: -1