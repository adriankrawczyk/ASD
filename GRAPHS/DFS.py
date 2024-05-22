def dfs(graph, start):
    visited = [False] * len(graph)
    traversal_order = []
    def dfs_helper(node):
        visited[graph.index(node)] = True
        traversal_order.append(node)
        for neighbor in graph[node]:
            if not visited[graph.index(neighbor)]:
                dfs_helper(neighbor)
    dfs_helper(start)
    return traversal_order

