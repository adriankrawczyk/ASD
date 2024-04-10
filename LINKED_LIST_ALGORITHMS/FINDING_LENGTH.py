class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Finding Length
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

