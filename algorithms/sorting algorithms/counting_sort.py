def counting_sort(arr, value_range):
    """
    Counting Sort Algorithm
    Time Complexity: O(n + k), where
        - n is the number of elements in the array
        - k is the range of input values (i.e., the maximum value)
      → When k = O(n), the algorithm runs in linear time: O(n)

    Requirements:
    - Input must consist of **non-negative integers**
    - The **maximum value (range)** of the input data must be known in advance

    Limitations:
    - Not efficient if the range (k) is much larger than n
    - This version is not stable (doesn't preserve the relative order of equal elements)

    Parameters:
    - arr: list of non-negative integers to sort
    - value_range: maximum possible value in arr
    """
    # Step 1: Create a count array to store frequency of each value from 0 to value_range
    count = [0] * (value_range + 1)

    # Step 2: Count the occurrences of each element
    for num in arr:
        count[num] += 1  # O(n)

    # Step 3: Reconstruct the sorted array based on the count array
    index = 0 # final sorted array index
    for i in range(value_range + 1):  # Include 0 if needed
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1  # O(n + k)

# Example usage:
arr = [3, 5, 2, 5, 1, 4, 2]
counting_sort(arr, value_range=5)
print(arr)  # Output: [1, 2, 2, 3, 4, 5, 5]
