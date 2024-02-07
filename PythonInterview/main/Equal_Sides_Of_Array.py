def find_balance_index(arr):
    total_sum = sum(arr)
    print("Total Sum :" , total_sum)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]  # Subtract the current element from the total sum
        print("total sum now : ", total_sum)
        if left_sum == total_sum:
            return i
        left_sum += arr[i]  # Add the current element to the left sum
        print("left_sum : ", left_sum)

    return -1  # Return -1 if no balance index is found

# Example usage:
arr1 = [1, 2, 3, 4, 3, 2, 1]
arr2 = [1, 100, 50, -51, 1, 1]
arr3 = [20, 10, -80, 10, 10, 15, 35]

print(find_balance_index(arr1))  # Output: 3
#print(find_balance_index(arr2))  # Output: 1
#print(find_balance_index(arr3))  # Output: 0
