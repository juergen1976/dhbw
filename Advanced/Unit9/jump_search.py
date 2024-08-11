def jump_search(arr, target):
    step = int(len(arr) ** 0.5)
    prev = 0

    while arr[min(step, len(arr)) - 1] < target:
        prev += step
        step += int(len(arr) ** 0.5)
        if prev >= len(arr):
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, len(arr)):
            return -1

    if arr[prev] == target:
        return prev
    else:
        return -1

numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40]
print(jump_search(numbers, 25))