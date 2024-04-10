# Subarray check
def find_subarray(arr, subarr):
    sub_len = len(subarr)
    for i in range(len(arr) - sub_len + 1):
        if arr[i:i + sub_len] == subarr:
            return i
    return -1

