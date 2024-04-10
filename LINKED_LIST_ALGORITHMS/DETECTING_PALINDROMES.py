class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Detecting Palindromes
def is_palindrome(head):
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def compare_lists(list1, list2):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse_list(slow)

    return compare_lists(head, reversed_second_half)


