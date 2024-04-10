class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# INSERTION SORT
def insertion_sort(head):
    if not head or not head.next:
        return head
    sorted_head = Node(float('-inf'))
    current = head
    while current:
        prev, next_node = sorted_head, sorted_head.next
        while next_node and next_node.val < current.val:
            prev, next_node = next_node, next_node.next
        temp = current.next
        current.next = next_node
        prev.next = current
        current = temp
    return sorted_head.next
