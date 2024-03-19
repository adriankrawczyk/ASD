# ADRIAN KRAWCZYK
"""
IN THIS ALGORITHM, DEPENDING ON K, WHICH REPRESENTS THE CHAOTICITY OF THE LIST, I USE ONE OF TWO SORTING ALGORITHMS:
FOR LARGE K, MERGE SORT
FOR SMALL K, BUBBLE SORT

Time complexity for k = Θ(1): O(n^2) - bubble sort
Time complexity for k = Θ(log n): O(n log n) - merge sort
Time complexity for k = Θ(n): O(n log n) - merge sort
"""

class Node:
    def init(self):
        self.val = None # stores a real number
        self.next = None # reference to the next element

def SortH(p, k):
    def bubble_sort(p):
        # check if the list has at least two elements
        if not (p and p.next):
            return p
            # bubble sort loop
        while True:
            any_swapped = False
            cur = p
            last = None

            # iteration through the list
            while cur.next is not last:
                # if the current element is greater than the next one, swap them
                if cur.val > cur.next.val:
                    cur.next.val, cur.val  = cur.val, cur.next.val 
                    any_swapped = True
                cur = cur.next
            last = cur

            # if there were no swaps, break the loop
            if not any_swapped:
                break
        return p

    def merge_two_lists(left, right):
        # initialize node
        tail = to_return = Node()

        # while both lists are not empty
        while left and right:
            # compare the values of elements from both lists
            if left.val > right.val:
                right, tail.next = right.next, right
            else:
                left, tail.next = left.next, left
            tail = tail.next

        # add remaining elements from the left or right list
        tail.next = right or left
        return to_return.next

    def merge_sort(p):
        # check if the list has at least two elements
        if not (p and p.next):
            return p

        # split the list into two parts
        first = second = p
        while first.next and first.next.next:
            first, second = first.next.next, second.next
        second_half = second.next
        second.next = None

        # sort both halves and merge them
        left_ok = merge_sort(p)
        right_ok = merge_sort(second_half)
        return merge_two_lists(left_ok, right_ok)

    # if k is less than 8, use bubble sort, otherwise use merge sort
    return bubble_sort(p) if k < 8 else merge_sort(p)
