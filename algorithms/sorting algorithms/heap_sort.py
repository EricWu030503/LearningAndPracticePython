# Function to heapify a subtree rooted at index 'i' in an array of size 'n'
def heapify(arr, n, i):
    largest = i         # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Main function to perform heap sort
def heap_sort(arr):
    n = len(arr)

    # Build a max-heap (bottom-up heapify)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)

# Example usage
arr = [4, 10, 3, 5, 1]

print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)
