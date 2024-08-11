def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Base case: target found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # Search the right half
    else:
        return binary_search(arr, target, low, mid - 1)  # Search the left half


# create array with values from 1 to 100000
arr = [i for i in range(1, 100001)]
target = 50000
result = binary_search(arr, target, 0, len(arr) - 1)

# create numpy array with values from 1 to 100000
import numpy as np
numpy_array = np.arange(1, 100001)
target = 50000
np.where(numpy_array == target)


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")