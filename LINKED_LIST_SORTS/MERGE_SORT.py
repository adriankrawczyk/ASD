class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# MERGE SORT
def merge_sort(head):
    if not head or not head.next:
        return head
    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left.val < right.val:
            result = left
            result.next = merge(left.next, right)
        else:
            result = right
            result.next = merge(left, right.next)
        return result
    def get_middle(head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    return merge(left, right)

