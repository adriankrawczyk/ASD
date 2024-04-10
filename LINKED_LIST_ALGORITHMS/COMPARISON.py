class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Comparison
def are_equal(head1, head2):
    current1 = head1
    current2 = head2

    while current1 and current2:
        if current1.val != current2.val:
            return False
        current1 = current1.next
        current2 = current2.next

    return current1 is None and current2 is None

