# ADRIAN KRAWCZYK
"""
Algorithm:
-Selects the number T[i]
-Puts all smaller numbers behind it and sets its rank to that amount
-Takes the maximum of these amounts and returns it The computational complexity is O(n^2)"""
def maxrank(T):
    max_rank = 0
    n = len(T)
    for i in range(n):
        rank = 0
        for j in range(i):
            if T[i-j-1] < T[i]:
                rank += 1
        max_rank = max(max_rank, rank)
    return max_rank
