def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # 9

    while low <= high:
        mid = (low + high) // 2
        print("MID : " ,mid)
        # Check if the target is present at the middle
        if arr[mid] == target:
            return mid

        # If target is greater, ignore the left half
        elif target > arr[mid] :
            low = mid + 1
        # If target is smaller, ignore the right half
        else:
            high = mid - 1

    # Target is not present in the array
    return -1


# Example usage:
sorted_array = [11, 22, 13, 14, 16, 15, 17, 18, 20, 19]
target_value = 14

result = binary_search(sorted(sorted_array), target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}")
else:
    print(f"Element {target_value} is not present in the array")
