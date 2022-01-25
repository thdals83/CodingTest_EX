from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
res = [0] * (n+1)
arr = [[] for _ in range(n+1)]

print(arr)
for _ in range(n - 1):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

queue = deque()
queue.append(1)

while queue:
    node = queue.popleft()

    for i in arr[node]:
        if res[i] == 0:
            res[i] = node
            queue.append(i)

for i in range(2, n+1):
    print(res[i])