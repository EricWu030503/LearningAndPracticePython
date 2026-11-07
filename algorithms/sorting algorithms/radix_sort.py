# A utility function to get the maximum value in an array
def get_max(arr):
    max_val = arr[0]
    for num in arr:
        max_val = max(max_val, num)
    return max_val

# Counting Sort used as a subroutine for Radix Sort
def counting_sort(arr, exp):
    # Stable sorting algorithm that maintains the relative order of numbers with the same digit
    n = len(arr)
    output = [0] * n  # Output array to hold sorted elements
    count = [0] * 10  # Count array for the range of digits (0–9)

    # Count the occurrences of each digit at the current place value
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # Modify count array to store cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (right to left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy the sorted elements back into the original array
    for i in range(n):
        arr[i] = output[i]

# Radix Sort function
def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_val = get_max(arr)

    # Sort the array for each digit's place value (1s, 10s, 100s, etc.)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Main execution
arr = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)

"""
Time Complexity Analysis of Radix Sort:
---------------------------------------
Let:
- n = Number of elements in the array.
- d = Number of digits in the largest number.
- k = Range of digits (for base 10, k = 10).

For each digit (d passes), we perform Counting Sort, which takes:
- O(n + k), where n is the size of the array and k is the range of digits.

Total time complexity:
- O(d * (n + k))

Special Cases:
1. When k is constant (e.g., base 10):
   - Time complexity simplifies to O(d * n)

Radix Sort is efficient when:
- The number of digits (d) is small
- The range of digits (k) is small relative to n
"""
