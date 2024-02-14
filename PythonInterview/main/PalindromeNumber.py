"""



Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x) :
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10 ## This will divide and tell reminder
        print(digit)
        reversed_num = reversed_num * 10 + digit
        print(reversed_num)
        temp = temp// 10  ## This is tell how many times number can be divided
        print(temp)
        print("-------------")

    return reversed_num == x

print(isPalindrome(121))
#print(isPalindrome(-121))
#print(isPalindrome(10))
#print(isPalindrome(1221))