def count_duplicates(input_str):
    # Convert the input string to lowercase for case-insensitive comparison
    input_str_lower = input_str.lower()

    # Use a dictionary to track the count of each character
    char_count = {}

    # Iterate through each character in the input string
    for char in input_str_lower:
        if char.isalnum():  # Check if the character is an alphabet or numeric digit
            print("character", char)
            #print(char_count.get(char, 0))
            char_count[char] = char_count.get(char, 0) + 1
            print(char_count[char])
    print(char_count)

    # Count the number of characters that occur more than once
    duplicates_count = sum(count > 1 for count in char_count.values())

    return duplicates_count


# Example usage:
# print(count_duplicates("abcde"))               # 0
print(count_duplicates("aabbcde"))  # 2
# print(count_duplicates("aabBcde"))             # 2
# print(count_duplicates("indivisibility"))     # 1
# print(count_duplicates("Indivisibilities"))   # 2
# print(count_duplicates("aA11"))                # 2
# print(count_duplicates("ABBA"))                # 2
