def boruvka_mst(graph):
    mst = []
    components = list(range(len(graph)))
    edges = [(cost, frm, to) for frm, row in enumerate(graph) for to, cost in enumerate(row) if cost != 0]
    edges.sort()
    while edges:
        cost, frm, to = edges.pop(0)
        if components[frm] != components[to]:
            mst.append((frm, to, cost))
            old_id, new_id = components[frm], components[to]
            for i in range(len(components)):
                if components[i] == old_id:
                    components[i] = new_id
    return mst