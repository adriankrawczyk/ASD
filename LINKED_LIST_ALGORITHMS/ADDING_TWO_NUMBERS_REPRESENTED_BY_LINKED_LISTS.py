class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Adding Two Numbers Represented by Linked Lists
def add_linked_lists(head1, head2):
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    head1 = reverse_list(head1)
    head2 = reverse_list(head2)

    dummy = Node(0)
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        carry, digit = divmod(val1 + val2 + carry, 10)
        current.next = Node(digit)
        current = current.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return reverse_list(dummy.next)

