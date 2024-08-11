def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    numbers = [14, 2, 34, 14, 25, 6, 27, 28, 9, 310]
    print(sequential_search(numbers, 9))