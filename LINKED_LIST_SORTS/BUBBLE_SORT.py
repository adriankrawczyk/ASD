class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Bubble sort 
def bubble_sort(p):
    def swap_nodes(node1, node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
    if not (p and p.next):
        return p
    while True:
        any_swapped = False
        cur = p
        last = None
        while cur.next is not last:
            if cur.val > cur.next.val:
                swap_nodes(cur, cur.next)
                any_swapped = True
            cur = cur.next
        last = cur
        if not any_swapped:
            break
    return p


