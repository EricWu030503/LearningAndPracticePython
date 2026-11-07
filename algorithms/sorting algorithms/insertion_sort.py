def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at the correct position
        arr[j + 1] = key

# Example usage
arr = [7, 3, 5, 2]

print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
