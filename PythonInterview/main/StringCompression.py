def compress_string(s):
    result = []
    count = 1

    # Handle edge case of an empty string
    if not s:
        return ""

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            print("One :", s[i], "Two :", s[i - 1])
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            print("Found New Character so adding it in list :", s[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    result.append(s[-1] + str(count))
    print(result)
    # Join the compressed characters into a single string
    compressed_string = ''.join(result)

    # Return the compressed string only if it is shorter than the original string
    return compressed_string if len(compressed_string) < len(s) else s


# Example usage:
original_string = "aaabbccdd"
compressed_result = compress_string(original_string)
print(f"Original String: {original_string}")
print(f"Compressed String: {compressed_result}")
