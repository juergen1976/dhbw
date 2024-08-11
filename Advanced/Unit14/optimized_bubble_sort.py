def optimized_bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        # Last i elements are already sorted, so inner loop will only consider unsorted part
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, then the array is sorted
        if not swapped:
            break

arr = [12, 34, 56, 78, 90]
optimized_bubble_sort(arr)
print("Sorted array is:", arr)