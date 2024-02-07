def min_coins(coinsList, amount):
    # Create a list to store the minimum number of coins for each amount

    dp = [float('inf')] * (amount + 1)

    print(dp[amount])
    # Base case: Zero coins needed for amount 0
    dp[0] = 0
    print(dp)
    # Iterate through all amounts from 1 to the target amount
    for curr_amount in range(1, amount + 1):
        # Check each coin denomination
        # print("curr_amount:", curr_amount)

        for coin in coinsList:
            print("curr_amount : ", curr_amount)
            print("Coin : ", coin)
            # print("curr_amount - coin : ", curr_amount - coin)
            if curr_amount - coin >= 0:
                # Update the minimum number of coins needed for the current amount
                # print("dp[curr_amount] : ", dp[curr_amount])
                # print("dp[curr_amount - coin]", dp[curr_amount - coin])
                # print("dp[curr_amount - coin] + 1 : ", dp[curr_amount - coin] + 1)
                dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
                print("dp[curr_amount] Element added:  ", dp[curr_amount])
                # print("dp[amount] : ", dp[amount])
                # print("------------------------------------")

    # If dp[amount] is still the initial value, it means the amount cannot be made up
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage:
coins = [5, 10, 25]
amount = 55
result = min_coins(coins, amount)
print(f"The fewest number of coins needed for amount {amount} is: {result}")
