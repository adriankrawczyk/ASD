class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Deletion
def delete_at_beginning(head):
    if not head:
        print("Linked list is empty")
        return None
    return head.next

def delete_at_end(head):
    if not head:
        print("Linked list is empty")
        return None
    if not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

def delete_at_position(head, position):
    if not head or position < 0:
        print("Invalid position")
        return head
    if position == 0:
        return delete_at_beginning(head)
    current = head
    for _ in range(position - 1):
        if not current.next:
            print("Invalid position")
            return head
        current = current.next
    if not current.next:
        print("Invalid position")
        return head
    current.next = current.next.next
    return head

