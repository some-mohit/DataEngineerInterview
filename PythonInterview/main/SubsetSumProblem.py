"""Given a set of non-negative integers and a value sum,
the task is to check if there is a subset of the given set whose sum is equal to the given sum.

Examples:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
Explanation: There is no subset that add up to 30."""


# A recursive solution for subset sum
# problem


# Returns true if there is a subset
# of set[] with sum equal to given sum
def isSubsetSum(set, n, sum):

    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False

    # If last element is greater than sum, then ignore it
    if set[n - 1] > sum:
        print("Ignored", set[n - 1])
        return isSubsetSum(set, n - 1, sum)

    print("Kept : ", set[n - 1])
    # Else, check if sum can be obtained by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


# Driver code
if __name__ == '__main__':
    set = [3, 34, 4, 12, 5, 10]
    sum = 7
    n = len(set)
    print(n)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")


