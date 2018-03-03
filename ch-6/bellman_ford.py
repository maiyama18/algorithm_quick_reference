INFTY = 1000
def bellman_ford(G, N, s):
    dist = [INFTY] * N
    dist[s] = 0

    for i in range(len(G)):
        for (fr, to, d) in G:
            new_dist = dist[fr] + d
            if new_dist < dist[to]:
                dist[to] = new_dist
                if i == N - 1:
                    print("negative loop exists!")

    for (v, d) in enumerate(dist):
        print("{}: {}".format(v, d))

if __name__ == "__main__":
    G = [(0, 4, 2), (4, 3, 4), (4, 1, 5), (1, 3, -2), (3, 2, 6), (2, 1, -3)]
    bellman_ford(G, 5, 0)