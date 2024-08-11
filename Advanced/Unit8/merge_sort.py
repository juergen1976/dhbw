def merge_sort(arr):
    if len(arr) <= 1:  # base case: single element or empty list
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # conquer: recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # combine: merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result