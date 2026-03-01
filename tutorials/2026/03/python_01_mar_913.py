# prefix_sum.py

def calculate_prefix_sum(arr):
    """
    Calculate the prefix sum of a given array.
    
    Args:
        arr (list): The input array.
    
    Returns:
        list: The prefix sum array.
    """
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    return prefix_sum

def calculate_infix_sum(arr):
    """
    Calculate the infix sum of a given array.
    
    Args:
        arr (list): The input array.
    
    Returns:
        list: The infix sum array.
    """
    infix_sum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        infix_sum[i + 1] = infix_sum[i] + arr[i] + arr[i + 1]
    return infix_sum

def main():
    # Create a sample array
    arr = [1, 2, 3, 4, 5]
    
    # Calculate prefix sum
    prefix_sum_arr = calculate_prefix_sum(arr)
    print("Prefix Sum Array:", prefix_sum_arr)
    
    # Calculate infix sum
    infix_sum_arr = calculate_infix_sum(arr)
    print("Infix Sum Array:", infix_sum_arr)

if __name__ == "__main__":
    main()