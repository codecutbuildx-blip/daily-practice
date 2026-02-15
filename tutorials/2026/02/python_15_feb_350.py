# Dynamic Programming Memoization Example

def fibonacci(n, memo={}):
    # Base case for recursion
    if n <= 0:
        return 0
    
    # Check if result already computed
    elif n in memo:
        return memo[n]
    
    # Recursive case with memoization
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

# Test the function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")