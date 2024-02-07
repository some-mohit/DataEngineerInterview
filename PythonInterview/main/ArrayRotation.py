def left_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than the array length

    return arr[k:] + arr[:k]

# Example usage:
original_array = [1, 2, 3, 4, 5]
rotation_count = 3
rotated_array = left_rotate_array(original_array, rotation_count)

print(f"Original Array: {original_array}")
print(f"Left Rotated Array: {rotated_array}")

def right_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than the array length

    return arr[-k:] + arr[:-k]

# Example usage:
original_array = [1, 2, 3, 4, 5]
rotation_count = 3
rotated_array = right_rotate_array(original_array, rotation_count)

print(f"Original Array: {original_array}")
print(f"Right Rotated Array: {rotated_array}")
