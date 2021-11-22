from collections import deque

n, m, v = map(int,input().split())

graph = [[0 for i in range(n + 1)] for _ in range(n + 1)]
visited1, visited2 = [0] * (n + 1), [0] * (n + 1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

#dfs
stack = [v]
res = []
while stack:
    node = stack.pop()

    if str(node) not in str(res):
        res.append(str(node))
        for i in range(n, 0, -1):
            if graph[node][i] == 1 and visited1[i] == 0:
                stack.append(i)
                visited1[node] = 1

print(' '.join(res))
#-------------------------------------------------
#bfs
queue = deque()
queue.append(v)
res = []
while queue:
    node = queue.popleft()

    if str(node) not in str(res):
        res.append(str(node))
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited2[i] = 1
print(' '.join(res))
