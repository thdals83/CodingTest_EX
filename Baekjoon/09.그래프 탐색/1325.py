import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    d = 0
    queue = deque()
    queue.append(s)
    visited = [0] * (n + 1)
    visited[s] = 1

    while queue:
        node = queue.popleft()
        d += 1

        for i in arr[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    return d


n,m = map(int,input().split())
arr = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)

mxd = 0
res = []

for i in range(1,n+1):
    if arr[i]:
        tmp = bfs(i)
        if mxd <= tmp:
            if mxd < tmp:
                res = []
            mxd = tmp
            res.append(i)

print(*res)