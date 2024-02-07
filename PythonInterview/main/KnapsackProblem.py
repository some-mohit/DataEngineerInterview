"""Example: Planning a Backpack for a Hiking Trip
Suppose you are going on a hiking trip, and you have a backpack with a limited weight capacity.
You want to maximize the total value of the items you carry while staying within the weight limit.
Items available:

Water bottle (weight: 1 kg, value: $10)
Food pack (weight: 3 kg, value: $25)
Sleeping bag (weight: 2 kg, value: $20)
Camera (weight: 4 kg, value: $30)
Backpack capacity: 5 kg

The 0/1 Knapsack Problem now becomes:
What combination of items should you take to maximize the total value while not exceeding the weight capacity of your backpack?"""

def knapsack_01(values, weights, capacity):
    n = len(values)
    # Initialize a 2D list to store the maximum value for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If the current item's weight exceeds the current capacity, skip it
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Either include the current item or exclude it, choose the maximum value
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][capacity]

# Example usage:
values = [10, 25, 20, 30]
weights = [1, 3, 2, 4]
backpack_capacity = 5

result = knapsack_01(values, weights, backpack_capacity)
print(f"Maximum value that can be obtained: {result}")
