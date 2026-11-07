def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the index of the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main execution
arr = [7, 3, 5, 2]

print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
