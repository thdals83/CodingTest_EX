
from collections import deque

def bfs(graph, num, n):
    res = []
    queue = deque()
    visited = [0] * (num + 1)
    queue.append(n)

    while queue:
        node = queue.popleft()

        if node not in res:
            res.append(node)
            for i in range(1, num + 1):
                if visited[i] == 0 and graph[node][i] == 1:
                    queue.append(i)
                    visited[i] = 1
    x = ""
    for i in res:
        x += str(i)+" "
    return x

def dfs(graph, num, n):
    res = []
    stack = [n]
    visited = [0] * (num + 1)

    while stack:
        node = stack.pop()

        if node not in res:
            res.append(node)
            for i in range(num, 0, -1):
                if visited[i] == 0 and graph[node][i] == 1:
                    stack.append(i)
                    visited[node] = 1


    x = ""
    for i in res:
        x += str(i)+" "
    return x


n,m,v = map(int, input().split())
g = [[0 for i in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x][y] = g[y][x] = 1

print(dfs(g, n, v))
print(bfs(g, n, v))