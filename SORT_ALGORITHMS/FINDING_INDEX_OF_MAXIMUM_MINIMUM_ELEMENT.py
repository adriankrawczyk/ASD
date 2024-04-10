# Finding Index of Maximum/Minimum Element
def find_max_index(arr):
    max_val = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return max_index

def find_min_index(arr):
    min_val = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_index

