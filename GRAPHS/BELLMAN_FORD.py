def bellman_ford(graph, source):
    distance = [float("Inf")] * len(graph)
    distance[source] = 0
    for _ in range(len(graph) - 1):
        for u, v, w in graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for u, v, w in graph:
        if distance[u] != float("Inf") and distance[u] + w < distance[v]:
            print("Graph contains a negative-weight cycle")
            return
    return distance
