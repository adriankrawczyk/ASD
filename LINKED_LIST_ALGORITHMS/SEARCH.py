class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Search
def search(head, val):
    current = head
    while current:
        if current.val == val:
            return True
        current = current.next
    return False

