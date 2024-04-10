class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Traversal
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next

