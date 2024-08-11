def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    # Test the binary_search function with a sample array and target value
    arr = [1, 2, 3, 4, 5, 6]
    x = 3
    result = binary_search(arr, x)
    print(f"The index of {x} in the array is {result}")

if __name__ == "__main__":
    main()

