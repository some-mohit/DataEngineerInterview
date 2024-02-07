"""22. Simple implementation of Reversing each word in String.
Conditions :
1. Retain the case of the alphabet at particular Index.#
Example:
Input - I am Robot
Output - I ma Tobor
2. The special characters should retain the position.
Example:
Input - I am, Robot!
Output - I ma, Tobor! """

def reverse_each_word(input_string):
    words = input_string.split()
    reversed_words = []

    for word in words:
        # Extracting the alphabets and special characters
        alphabets = [char for char in word if char.isalpha()]
        specials = [char for char in word if not char.isalpha()]

        # Reversing the alphabets
        reversed_word = ''.join(reversed(alphabets))

        # Combining reversed alphabets and special characters
        reversed_word_with_specials = ''
        alpha_index, special_index = 0, 0
        for char in word:
            if char.isalpha():
                reversed_word_with_specials += reversed_word[alpha_index]
                alpha_index += 1
            else:
                reversed_word_with_specials += specials[special_index]
                special_index += 1

        reversed_words.append(reversed_word_with_specials)

    # Joining the reversed words to form the final string
    result = ' '.join(reversed_words)
    return result

# Example usage:
input_str = "I am, Robot!"
output_str = reverse_each_word(input_str)

print(f"Input: {input_str}")
print(f"Output: {output_str}")
