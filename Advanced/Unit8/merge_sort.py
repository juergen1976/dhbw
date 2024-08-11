def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.

    The merge sort algorithm follows a divide-and-conquer approach.
    It consists of three main steps: Divide, Conquer, and Merge.

    Steps:
    1. Divide: Split the array into two halves.
    2. Conquer: Recursively sort both halves.
    3. Merge: Merge the two sorted halves into a single sorted array.
    """
    # If the array has one or no element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Call merge_sort recursively for both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    :param left: Sorted left half
    :param right: Sorted right half
    :return: Merged and sorted list

    The merging process involves:
    1. Initializing an empty list to store the merged elements.
    2. Using two pointers to track positions in the left and right lists.
    3. Comparing elements from both lists and appending the smaller element to the sorted list.
    4. If there are remaining elements in either list after the comparison, append them to the sorted list.
    """
    sorted_array = []
    i = j = 0

    # Traverse both lists and append the smaller element from either list to the sorted_array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements of left and right lists
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", array)
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)
