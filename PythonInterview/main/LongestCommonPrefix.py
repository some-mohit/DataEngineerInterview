"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(listStr):

    if not listStr:
        return ""  # If the input list is empty, there is no common prefix.

    # Find the shortest string in the list (the minimum length determines the common prefix length).
    min_len = min(len(s) for s in listStr)
    #min_len = (len(s) for s in listStr)
    common_prefix = ""
    for i in range(min_len):
        # Compare the current character of all strings with the character at the same position in the first string.
        current_char = listStr[0][i]
        for string in listStr:
            if string[i] != current_char:
                return common_prefix  # If characters don't match, return the common prefix found so far.

        common_prefix += current_char  # If characters match, add the character to the common prefix.

    return common_prefix



