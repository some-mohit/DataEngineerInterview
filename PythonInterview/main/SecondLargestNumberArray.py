def find_second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element found"
    else:
        return second_largest

# Example usage:
array = [10, 5, 8, 20, 15]
result = find_second_largest(array)

print(f"Array: {array}")
print(f"Second Largest Number: {result}")
