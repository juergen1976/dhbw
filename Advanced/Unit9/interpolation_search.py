def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target and arr[high] >= target:
        mid = low + (target - arr[low]) * (high - low) // (arr[high] - arr[low])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40]
print(interpolation_search(numbers, 5))