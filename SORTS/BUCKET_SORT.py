# BUCKET SORT
def bucket_sort(arr):
    # Find the minimum and maximum values in the input array
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1
    
    # Create empty buckets
    buckets = [[] for _ in range(range_val)]
    
    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    
    # Sort each bucket (using insertion sort in this case)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr
