from collections import deque
def bfs(graph, start):
    traversal_order = []
    queue = deque([start])
    visited = [False] * len(graph)
    while queue:
        node = queue.popleft()
        index = list(graph.keys()).index(node)
        if not visited[index]:
            traversal_order.append(node)
            visited[index] = True
            for neighbor in graph[node]:
                index = list(graph.keys()).index(neighbor)
                if not visited[index]:
                    queue.append(neighbor)
    return traversal_order