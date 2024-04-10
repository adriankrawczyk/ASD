class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Splitting
def split_in_half(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    return head, second_half

