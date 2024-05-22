from collections import deque
def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[graph.index(start)] = 0
    previous_nodes = [None] * len(graph)
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        for neighbor, weight in enumerate(graph[current_node]):
            distance = distances[graph.index(current_node)] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                queue.append(neighbor)
    return distances, previous_nodes