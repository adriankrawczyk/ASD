class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# QUICK SORT
def quick_sort(head):
    def partitionLast(start, end):
        if start == end or start is None or end is None:
            return start
        pivot_prev = start
        curr = start
        pivot = end.val
        while start != end:
            if start.val < pivot:
                pivot_prev = curr
                temp = curr.val
                curr.val = start.val
                start.val = temp
                curr = curr.next
            start = start.next
        temp = curr.val
        curr.val = pivot
        end.val = temp
        return pivot_prev
    def sort(start, end):
        if start is None or start == end or start == end.next:
            return
        pivot_prev = partitionLast(start, end)
        sort(start, pivot_prev)
        if pivot_prev and pivot_prev == start:
            sort(pivot_prev.next, end)
        elif pivot_prev and pivot_prev.next:
            sort(pivot_prev.next.next, end)
    def get_tail(head):
        tail = head
        while tail.next:
            tail = tail.next
        return tail
    tail = get_tail(head)
    sort(head, tail)
    return head

