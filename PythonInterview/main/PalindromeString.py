def is_palindrome(input_str):
    # Convert the input string to lowercase and remove non-alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    #cleaned_str_test = ''.join(char.lower() for char in input_str if char.isalnum())
    print(cleaned_str)
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
string1 = "A man, a plan, a canal, Panama!"
string2 = "hello"

print(f"Is '{string1}' a palindrome? {is_palindrome(string1)}")  # Output: True
print(f"Is '{string2}' a palindrome? {is_palindrome(string2)}")  # Output: False

print(f"Is '{string2}' a palindrome? {is_palindrome("civic")}")