def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n-1):
        # Last i elements are already sorted, so inner loop will only consider unsorted part
        for j in range(0, n-i-1):
            # If current element is greater than next one, swap both of them.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [12, 34, 56, 78, 90]
bubble_sort(arr)
print("Sorted array is:", arr)