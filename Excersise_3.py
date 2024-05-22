
#ADRIAN KRAWCZYK
""" THE ALGORITHM RETURNS THE POINT WITH THE HIGHEST SUM OF OTHER DOMINATED POINTS, CHECKS ONLY POINTS SELECTED BY THE FILTER_SORTED AND QUICKSORT FUNCTIONS, IN WHICH THERE IS ALWAYS A POINT THAT IS THE MOST DOMINANT

Time complexity: 
-Quicksort: The average time complexity of Quicksort is O(n log n), where n is the number of points. 
-Filter_sorted: Assuming that the filter_sorted function iterates through a sorted list of points of length n and performs constant complexity operations inside the loop, the time complexity is O(n). 
-is_dominant: Comparison operations in the is_dominant function are of constant complexity, so the time complexity of this function is O(1). -get_sum: The get_sum function iterates through a list of points of length n, performing constant complexity operations, so its time complexity is also O(n). 
-Max: The max function iterates through a list of points of length n, performing constant complexity operations, so its time complexity is O(n). The total time complexity of the algorithm is therefore O(n log n), as Quicksort dominates over the other operations. """

def dominance(P):
    return max(get_sum(point, P) for point in filter_sorted(quicksort(P)))
def quicksort(points):
    n = len(points) 
    if n < 2:
        return points
    pivot = points[n-1]
    return quicksort([x for x in points if x[0] > pivot[0] or x[1] > pivot[1]]) + [pivot]
def filter_sorted(sorted_p):
    return [p for p in sorted_p if not any(is_dominant(d, p) for d in sorted_p)]
def is_dominant(t, b):
    return t[0] > b[0] and t[1] > b[1]
def get_sum(point, points):
    return sum(is_dominant(point, p) for p in points)
