class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Swapping Nodes
def swap_nodes(head, x, y):
    if x == y:
        return head

    prevX = None
    currX = head
    while currX and currX.val != x:
        prevX = currX
        currX = currX.next

    prevY = None
    currY = head
    while currY and currY.val != y:
        prevY = currY
        currY = currY.next

    if not currX or not currY:
        return head

    if prevX:
        prevX.next = currY
    else:
        head = currY

    if prevY:
        prevY.next = currX
    else:
        head = currX

    temp = currX.next
    currX.next = currY.next
    currY.next = temp

    return head

