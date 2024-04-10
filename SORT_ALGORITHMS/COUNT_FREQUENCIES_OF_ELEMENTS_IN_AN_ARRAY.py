# Count frequencies of elements in an array
def count_frequencies(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    return counts

