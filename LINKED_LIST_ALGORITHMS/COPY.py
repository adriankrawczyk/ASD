class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Copy
def copy(head):
    new_head = None
    current = head
    prev_new_node = None
    while current:
        new_node = Node(current.val)
        if not new_head:
            new_head = new_node
        if prev_new_node:
            prev_new_node.next = new_node
        prev_new_node = new_node
        current = current.next
    return new_head

