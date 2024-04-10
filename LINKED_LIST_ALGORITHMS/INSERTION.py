class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Insertion
def insert_at_beginning(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insert_at_end(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, val, position):
    if position < 0:
        print("Invalid position")
        return head
    if position == 0:
        return insert_at_beginning(head, val)
    new_node = Node(val)
    current = head
    for _ in range(position - 1):
        if not current:
            print("Invalid position")
            return head
        current = current.next
    if not current:
        print("Invalid position")
        return head
    new_node.next = current.next
    current.next = new_node
    return head

