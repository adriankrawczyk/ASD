class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Delete node by value
def delete_node_by_value(head, val):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    while current:
        if current.val == val:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return dummy.next

