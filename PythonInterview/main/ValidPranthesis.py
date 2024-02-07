def is_valid_parentheses(s):
    stack = []
    # Dictionary to store the mappings of opening and closing parentheses
    mapping = {')': '(',
               '}': '{',
               ']': '['}

    for char in s:
        if char in mapping.values():  # Opening parentheses
            print("Added : ", char)
            stack.append(char)
        elif char in mapping.keys():  # Closing parentheses
            # Pop the top element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else print("Top IS Empty")
            print("top", top_element)

            # Check if the popped element matches the corresponding opening parenthesis
            print(mapping[char])
            if mapping[char] != top_element:
                return False
        else:
            # Invalid character found
            return False

    # The string is valid if the stack is empty at the end
    return not stack


# Example usage:
#print(is_valid_parentheses("()"))  # True
#print(is_valid_parentheses(")(()))"))  # False
#print(is_valid_parentheses("("))  # False
print(is_valid_parentheses("(())((()())())"))  # True
