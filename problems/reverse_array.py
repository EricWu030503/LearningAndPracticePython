def array_reversal(array, start, end):
    if start >= end:
        return
    else:
        array[start],array[end] = array[end],array[start]
        array_reversal(array, start+1, end-1)

array = [0, 1, 2, 3, 4, 5]
array_reversal(array, 0, len(array)-1)
print(array)
