def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found target at index i
    return -1  # Target not found
