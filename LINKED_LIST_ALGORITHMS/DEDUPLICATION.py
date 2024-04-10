class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Deduplication
def remove_duplicates(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

