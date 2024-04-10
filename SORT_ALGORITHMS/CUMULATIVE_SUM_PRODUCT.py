# Cumulative Sum/Product
def cumulative_sum(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])
    return result

def cumulative_product(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[-1] * arr[i])
    return result

