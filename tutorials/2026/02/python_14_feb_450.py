# Greedy Algorithms Tutorial

# This script teaches you how to use greedy algorithms, which are a simple and efficient way to solve certain problems.
# A greedy algorithm makes the locally optimal choice at each stage of the problem-solving process in order to find a globally optimal solution.

def coin_change(coins, amount):
    # Create a list to store the minimum number of coins needed for each amount from 0 to the target amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Iterate over each possible amount from 1 to the target amount
    for i in range(1, amount + 1):
        # For each coin denomination
        for coin in coins:
            # If the current amount is greater than or equal to the coin denomination
            if i >= coin:
                # Update the minimum number of coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins needed for the target amount
    return dp[amount]

def knapsack(capacity, weights, values):
    # Create a list to store the maximum value that can be put in a knapsack of capacity 'capacity'
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        max_val = 0
        for i in range(len(weights)):
            if weights[i] <= w:
                max_val = max(max_val, values[i] + dp[w - weights[i]])
        dp[w] = max_val

    # Return the maximum value that can be put in a knapsack of capacity 'capacity'
    return dp[capacity]

# Example usage
coins = [1, 2, 5]
amount = 4
print("Minimum coins needed for", amount, ":", coin_change(coins, amount))

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value that can be put in a knapsack of capacity", capacity, ":", knapsack(capacity, weights, values))