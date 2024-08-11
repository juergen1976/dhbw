def maximum_recursive_subarray_sum(arr, memo={}):
    if not arr:  # base case
        return 0

    n = len(arr)

    key = tuple(arr)  # create a tuple to use as a memoization key
    if key in memo:
        return memo[key]

    max_sum = float('-inf')  # initialize max sum to negative infinity

    for i in range(n):
        current_sum = arr[i]
        for j in range(i + 1, n):
            current_sum += arr[j]

            # recursively compute the maximum subarray sum
            left_half_sum = maximum_recursive_subarray_sum(arr[:i], memo)
            right_half_sum = maximum_recursive_subarray_sum(arr[i + 1:], memo)

            max_sum = max(max_sum, left_half_sum + current_sum, right_half_sum + current_sum, current_sum)

    memo[key] = max_sum  # store the result in the memoization dictionary
    return max_sum

# Testing
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum of a subarray:", maximum_recursive_subarray_sum(arr))