# Partition an array into two based on a condition
def partition_array(arr, condition):
    left, right = [], []
    for x in arr:
        if condition(x):
            left.append(x)
        else:
            right.append(x)
    return left, right

