class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Conversion to/from Array
def to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def from_array(arr):
    head = None
    for val in arr:
        head = insert_at_end(head, val)
    return head

