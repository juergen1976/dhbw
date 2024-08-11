def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    pos = 1
    while pos < len(arr) and arr[pos] <= target:
        pos *= 2

    if pos >= len(arr) or arr[pos] > target:
        return -1

    low, high = max(0, pos//2), min(pos, len(arr))
    return binary_search(arr[low:high], target) + low

numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40]
print(binary_search(numbers, 20))