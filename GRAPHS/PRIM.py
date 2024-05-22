def prim_mst(graph):
    mst = []
    visited = [False] * len(graph)
    start_vertex = 0
    visited[start_vertex] = True
    edges = [(cost, start_vertex, to) for to, cost in enumerate(graph[start_vertex])]
    while edges:
        edges.sort()
        cost, frm, to = edges.pop(0)
        if not visited[to]:
            visited[to] = True
            mst.append((frm, to, cost))
            for to, cost in enumerate(graph[to]):
                if not visited[to]:
                    edges.append((cost, to, frm))
    return mst