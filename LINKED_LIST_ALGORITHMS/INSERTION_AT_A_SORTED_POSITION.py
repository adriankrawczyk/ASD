class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Insertion at a sorted position
def insert_at_sorted_position(head, val):
    new_node = Node(val)
    if not head or val <= head.val:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.val < val:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

