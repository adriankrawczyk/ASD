class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Finding the Middle Element
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

