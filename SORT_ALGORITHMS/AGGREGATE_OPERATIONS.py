# Aggregate Operations
def aggregate_operations(arr):
    sum_val = sum(arr)
    mean_val = sum_val / len(arr)
    sorted_arr = sorted(arr)
    if len(arr) % 2 == 0:
        median_val = (sorted_arr[len(arr)//2 - 1] + sorted_arr[len(arr)//2]) / 2
    else:
        median_val = sorted_arr[len(arr)//2]
    variance_val = sum((x - mean_val) ** 2 for x in arr) / len(arr)
    std_dev_val = variance_val ** 0.5
    return {
        'sum': sum_val,
        'mean': mean_val,
        'median': median_val,
        'variance': variance_val,
        'standard_deviation': std_dev_val
    }

