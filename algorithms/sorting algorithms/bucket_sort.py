def bucket_sort(arr, value_range):
    # Create empty buckets
    buckets = [[] for _ in range(value_range + 1)]

    # Distribute elements into buckets
    for num in arr:
        buckets[num].append(num)

    # Concatenate sorted buckets into original array
    index = 0
    for i in range(1, value_range + 1):
        for num in buckets[i]:
            arr[index] = num
            index += 1

# Main block
arr = [4, 1, 3, 4, 2, 1, 8, 9]
value_range = 9  # Range of keys is [1, 9]

bucket_sort(arr, value_range)
print(arr)
