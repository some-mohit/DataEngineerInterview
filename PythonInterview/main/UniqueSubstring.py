"""


Given a string str and an integer L. The task is to print all the unique substring of
length L from string str.
Examples: Input: str = “abca”, L=3
Output: “abc”, “bca” Input: str = “aaaa”, L=3
Output: “aaa”
Example case : aab, length=2; result is aa, ab
"""
def print_unique_substrings(str_input, L):
    if len(str_input) < L:
        print("Invalid input: Length of string is less than L.")
        return

    unique_substrings = set()

    for i in range(len(str_input) - L + 1):

        substring = str_input[i:i + L]
        unique_substrings.add(substring)

    for substring in unique_substrings:
        print(substring)

# Example usage:
str_input1 = "abca"
L1 = 3
print("Input: str =", str_input1, ", L =", L1)
print("Output:")
print_unique_substrings(str_input1, L1)

str_input2 = "aaaa"
L2 = 3
print("\nInput: str =", str_input2, ", L =", L2)
print("Output:")
print_unique_substrings(str_input2, L2)

str_input3 = "aab"
L3 = 2
print("\nInput: str =", str_input3, ", L =", L3)
print("Output:")
print_unique_substrings(str_input3, L3)
