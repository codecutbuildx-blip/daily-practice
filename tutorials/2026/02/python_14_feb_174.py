# Sliding Window Problem

def max_sum_subarray(arr, k):
    # Initialize the maximum sum and the current window sum
    max_sum = float('-inf')
    curr_sum = 0
    
    # Initialize two pointers for the sliding window
    left = 0
    right = 0
    
    # Calculate the initial window sum
    while right < len(arr):
        curr_sum += arr[right]
        right += 1
        
        # Check if the window size is equal to k
        if right - left == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[left]
            left += 1
    
    return max_sum

# Test the function with an example array and a window size of 3
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum subarray is:", max_sum_subarray(arr, k))

# Test the function with another example array and a window size of 2
arr = [1, 2, 3, 4, 5, 6]
k = 2
print("Maximum sum subarray is:", max_sum_subarray(arr, k))