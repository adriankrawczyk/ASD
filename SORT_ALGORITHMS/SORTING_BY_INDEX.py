# Sorting by Index
def sort_by_index(arr, index_arr):
    return [x for _, x in sorted(zip(index_arr, arr))]

