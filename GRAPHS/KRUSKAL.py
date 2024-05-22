def kruskal(graph):
    mst = []
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            edges.append((i, graph[i][j][0], graph[i][j][1]))
    edges.sort(key=lambda x: x[2])
    parent = list(range(len(graph)))
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, u, v)
    return mst
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]
def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if root1 != root2:
        parent[root1] = root2
