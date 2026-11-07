def merge(arr, left, mid, right):
    # Create temporary arrays
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    # Merge the temporary arrays back into arr
    i = j = 0
    k = left

    # Merge while both halves have elements
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2

    # Recursively sort both halves
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    # Merge the sorted halves
    merge(arr, left, mid, right)

# Example usage
arr = [6, 3, 8, 5, 2, 7, 4, 1]

print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
