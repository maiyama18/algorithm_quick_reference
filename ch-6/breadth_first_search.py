from collections import deque

def bfs(L, s):
    color = ['white'] * len(L)
    q = deque()

    q.append(s)
    color[s] = 'grey'

    while len(q) > 0:
        v = q.popleft()
        color[v] = 'black'
        for nv in L[v]:
            if color[nv] == 'white':
                q.append(nv)
                color[v] = 'grey'

if __name__ == "__main__":
    L = [
        [1],
        [2, 3],
        [],
        [2]
    ]
    bfs(L, 0)