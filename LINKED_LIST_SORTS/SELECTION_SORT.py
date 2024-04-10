class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Selection sort
def swap_nodes(node1, node2):
    temp = node1.val
    node1.val = node2.val
    node2.val = temp

def selection_sort(head):
    if not head or not head.next:
        return head
    
    current = head
    while current:
        min_node = current
        next_node = current.next
        while next_node:
            if next_node.val < min_node.val:
                min_node = next_node
            next_node = next_node.next
        if min_node != current:
            swap_nodes(current, min_node)
        current = current.next
    return head
