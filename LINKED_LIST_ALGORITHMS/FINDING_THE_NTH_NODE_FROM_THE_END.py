class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Finding the Nth Node from the End
def find_nth_from_end(head, n):
    if not head:
        return None
    fast = head
    for _ in range(n):
        if fast:
            fast = fast.next
        else:
            return None
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.val if slow else None

