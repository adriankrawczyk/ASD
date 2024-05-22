class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

def adj_matrix_to_adj_list(adj_matrix):
    adj_list = [[] for _ in range(len(adj_matrix))]
    for i, row in enumerate(adj_matrix):
        for j, val in enumerate(row):
            if val != 0:
                adj_list[i].append(j)
    return adj_list

def adj_matrix_to_adj_list_linked(adj_matrix):
    adj_list = [LinkedList() for _ in range(len(adj_matrix))]
    for i, row in enumerate(adj_matrix):
        for j, val in enumerate(row):
            if val != 0:
                adj_list[i].append(j)
    return adj_list

def adj_matrix_to_edge_list(adj_matrix):
    edge_list = []
    for i, row in enumerate(adj_matrix):
        for j, val in enumerate(row):
            if val != 0:
                edge_list.append((i, j))
    return edge_list

def adj_list_to_adj_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = 1
    return adj_matrix

def adj_list_to_edge_list(adj_list):
    edge_list = []
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            edge_list.append((i, neighbor))
    return edge_list

def adj_list_linked_to_adj_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i, linked_list in enumerate(adj_list):
        current = linked_list.head
        while current:
            adj_matrix[i][current.value] = 1
            current = current.next
    return adj_matrix

def adj_list_linked_to_edge_list(adj_list):
    edge_list = []
    for i, linked_list in enumerate(adj_list):
        current = linked_list.head
        while current:
            edge_list.append((i, current.value))
            current = current.next
    return edge_list

def edge_list_to_adj_matrix(edge_list, n):
    adj_matrix = [[0] * n for _ in range(n)]
    for i, j in edge_list:
        adj_matrix[i][j] = 1
    return adj_matrix

def edge_list_to_adj_list(edge_list, n):
    adj_list = [[] for _ in range(n)]
    for i, j in edge_list:
        adj_list[i].append(j)
    return adj_list

def edge_list_to_adj_list_linked(edge_list, n):
    adj_list = [LinkedList() for _ in range(n)]
    for i, j in edge_list:
        adj_list[i].append(j)
    return adj_list
