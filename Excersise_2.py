# ADRIAN KRAWCZYK
"""
ALGORITHM OPERATION
Algorithm:
    -takes a p-element range
    -sorts it using quicksort
    -finds the k-th element and adds it to the sum
    -moves the range one index forward (removes the leftmost element, inserts the rightmost element)
COMPUTATIONAL COMPLEXITY
    -Sorting a p-element range using quicksort: O(p * log p).
    -Loop iterating through n - p elements: O(n).
    Inside the loop:
    -Binary search in the sorted range: O(log p).
    -Removal and insertion of an element in the range: O(p).
    -Adding an element to the sum: O(1).
Thus, the total time complexity of the algorithm is: O(p * log p + n * (p + log p)) ≈ O(n * p)
MEMORY COMPLEXITY
    -Storing the sorted range: O(p).
    -Additional memory for recursive quicksort calls: O(log p).
    -Other auxiliary variables: O(1).
Therefore, the memory complexity is O(p + log p)
"""
def ksum(T, k, p):
    n = len(T)
    _sum = 0 # SUM TO RETURN
    section = quicksort(T[:p]) # SORTING THE FIRST INTERVAL
    ind = p - k
    for i in range(n - p):
        _sum += section[ind] # ADDING THE VALUE AT THE SEARCHED INDEX TO THE SUM
        del section[binary_search(section, T[i], p)] # REMOVING THE LEFTMOST ELEMENT IN THE     INTERVAL
        value = T[i + p]
        section.insert(binary_search(section, value, p - 1), value) # INSERTING THE NEXT ELEMENT    INTO THE INTERVAL
    return _sum + section[ind]

def quicksort(T):
    n = len(T)
    if n < 2:
        return T
    pivot = T[n - 1]
    m = [x for x in T if x == pivot]
    r = [x for x in T if x > pivot]
    l = [x for x in T if x < pivot]
    return quicksort(l) + m + quicksort(r)

def binary_search(T, target, length):
    l, r = 0, length - 1
    while l <= r:
        m = l + ((r - l) >> 1) # FAST DIVISION, SAME AS l + (r - l) // 2
    if T[m] == target:
        return m
    elif T[m] < target:
        l = m + 1
    else:
        r = m - 1
    return l

