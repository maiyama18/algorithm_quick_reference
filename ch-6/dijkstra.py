INFTY = 1000
def dijkstra(L, s):
    X = set(range(len(L)))
    dist = [INFTY] * len(L)
    dist[s] = 0

    while len(X) > 0:
        v = nearest_node(dist, X)
        for (nv, dv) in L[v]:
            dist[nv] = min(dist[nv], dist[v] + dv)

        X.remove(v)
    
    for (v, d) in enumerate(dist):
        print("{}: {}".format(v, d))

def nearest_node(dist, X):
    mini = 0
    mind = INFTY
    for i in X:
        d = dist[i]
        if d < mind:
            mini = i
            mind = d
    
    return mini

if __name__ == "__main__":
    L = [
        [(1, 6), (2, 8), (3, 18)],
        [(4, 11)],
        [(3, 9)],
        [],
        [(5, 3)],
        [(3, 4), (2, 7)]
    ]
    dijkstra(L, 0)