# Find the minimum element in an array
def find_minimum(arr):
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    return min_val

