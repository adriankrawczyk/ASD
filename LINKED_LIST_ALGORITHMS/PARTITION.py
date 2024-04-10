class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# PARTITION
def partition(head, x):
    if not head:
        return None

    less_than_head = less_than_tail = Node()
    greater_than_head = greater_than_tail = Node()

    current = head
    while current:
        if current.val < x:
            less_than_tail.next = current
            less_than_tail = less_than_tail.next
        else:
            greater_than_tail.next = current
            greater_than_tail = greater_than_tail.next
        current = current.next

    greater_than_tail.next = None
    less_than_tail.next = greater_than_head.next

    return less_than_head.next
