class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Iterators
def iterate_linked_list(head):
    current = head
    while current:
        yield current.val
        current = current.next

