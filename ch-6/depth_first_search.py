def dfs(L, color, v):
    color[v] = 'grey'
    for nv in L[v]:
        if color[nv] == 'white':
            dfs(L, color, nv)
    color[v] = 'black'
    print("visited " + str(v))

if __name__ == "__main__":
    L = [
        [1],
        [2, 3],
        [],
        [2]
    ]

    color = ['white'] * len(L)
    dfs(L, color, 0)