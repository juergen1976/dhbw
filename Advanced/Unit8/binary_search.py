def binary_search(arr, target):
    # Base case: If the array is empty, return -1 (not found)
    if len(arr) == 0:
        return -1

    # Find the middle index of the array
    mid = len(arr) // 2

    # Compare the target element with the middle element of the array
    if arr[mid] == target:
        # If the target element is found at the middle index, return the index
        return mid

    # Divide the array into two halves: left and right
    left = arr[:mid]
    right = arr[mid + 1:]

    # Recursively search in the appropriate half
    if target < arr[mid]:
        # If the target element is less than the middle element, search in the left half
        return binary_search(left, target)
    else:
        # If the target element is greater than or equal to the middle element, search in the right half
        return mid + 1 + binary_search(right, target)


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)  # Output: 4