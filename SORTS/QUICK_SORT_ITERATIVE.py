# QUICK SORT ITERATIVE
def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1 
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))
    return arr

