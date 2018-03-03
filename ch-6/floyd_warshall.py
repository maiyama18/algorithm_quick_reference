from queue import PriorityQueue

INFTY = 1000
def floyd_warshall(G, N, s):
    dist = [[0 if i == j else INFTY for i in range(N)] for j in range(N)]
    for (fr, to, d) in G:
        dist[fr][to] = d
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_dist = dist[j][i] + dist[i][k]
                dist[j][k] = min(new_dist, dist[j][k])

    for i in range(N):
        for j in range(N):
            print("{}->{}: {}".format(i, j, dist[i][j]))

if __name__ == "__main__":
    G = [(0, 1, 2), (0, 4, 4), (1, 2, 3), (2, 3, 5), (2, 4, 1), (3, 0, 8), (4, 3, 7)]
    floyd_warshall(G, 5, 0)