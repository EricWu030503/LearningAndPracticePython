def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False

        # Last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the last pass, the array is sorted
        if not swapped:
            break

# Main block
arr = [64, 34, 25, 12, 22, 11, 92]

print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
