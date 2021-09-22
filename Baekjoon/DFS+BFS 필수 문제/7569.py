import sys
from collections import deque

if __name__ == "__main__":
    queue = deque()
    x, y, z = map(int,input().split())
    graph = [[] for i in range(z)]

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(z):
        for j in range(y):
            graph[i].append(list(map(int,sys.stdin.readline().split())))
            for k in range(x):
                if graph[i][j][k] ==1:
                    queue.append([i,j,k])

    while queue:
        a1, b1, c1 =queue.popleft()

        for i in range(6):
            a = a1 + dx[i]
            b = b1 + dy[i]
            c = c1 + dz[i]

            if 0<= a < z and 0<= b < y and 0<= c < x and graph[a][b][c] == 0:
                queue.append([a,b,c])
                graph[a][b][c] = graph[a1][b1][c1] +1

    res = 0

    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            res = max(res, max(j))

print(res - 1)


