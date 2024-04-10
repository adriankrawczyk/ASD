class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Reversal
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

