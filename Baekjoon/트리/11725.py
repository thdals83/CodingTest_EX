from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
queue = deque()

for _ in range(n - 1):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

queue.append(1)
while queue:
    node = queue.popleft()
    for i in arr[node]:
        if visited[i] == 0:
            visited[i] = node
            queue.append(i)

for i in visited[2:]:
    print(i)

