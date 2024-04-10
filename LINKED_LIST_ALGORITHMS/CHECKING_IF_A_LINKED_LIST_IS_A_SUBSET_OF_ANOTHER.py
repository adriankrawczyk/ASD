class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Checking if a Linked List is a Subset of Another
def is_subset(head1, head2):
    visited = set()
    current = head2
    while current:
        visited.add(current.val)
        current = current.next

    current = head1
    while current:
        if current.val not in visited:
            return False
        current = current.next
    return True

