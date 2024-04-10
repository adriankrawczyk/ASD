class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Delete Nodes Greater Than X
def delete_nodes_greater_than_x(head, x):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    while current:
        if current.val > x:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return dummy.next
