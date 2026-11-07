# Function to partition the array
def partition(arr, low, high):  # O(n)
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if current element is smaller than pivot

    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index

# Function to perform Quicksort
def quick_sort(arr, low, high):  # Best: O(n log n), Worst: O(n^2), Average: O(n log n)
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage
arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
