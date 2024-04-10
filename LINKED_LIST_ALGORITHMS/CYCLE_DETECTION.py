class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Cycle Detection
def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

