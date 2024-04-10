class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# RADIX SORT
def radix_sort_linked_list(head):
    if head is None or head.next is None:
        return head
    def get_max_value(head):
        max_value = head.val
        current = head.next
        while current:
            if current.val > max_value:
                max_value = current.val
            current = current.next
        return max_value
    def counting_sort(head, exp):
        if head is None or head.next is None:
            return head
        count = [0] * 10
        output = [None] * 10
        current = head
        while current:
            index = (current.val // exp) % 10
            count[index] += 1
            current = current.next
        current = head
        while current:
            index = (current.val // exp) % 10
            if output[index] is None:
                output[index] = Node(current.val)
            else:
                temp = output[index]
                while temp.next:
                    temp = temp.next
                temp.next = Node(current.val)
            current = current.next
        head = None
        for i in range(10):
            if output[i]:
                if head is None:
                    head = output[i]
                else:
                    temp = head
                    while temp.next:
                        temp = temp.next
                    temp.next = output[i]
        return head
    max_value = get_max_value(head)
    exp = 1
    while max_value // exp > 0:
        head = counting_sort(head, exp)
        exp *= 10
    return head

