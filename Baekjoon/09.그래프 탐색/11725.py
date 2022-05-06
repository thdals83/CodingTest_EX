from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline
'''
트리의 루트 = 1
각 노드의 부모를 구하라
'''

n = int(input())
tree = defaultdict(list)

for _ in range(n - 1):
    x, y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [0] * (n + 1)
queue = deque([1])
visited[1] = 1

while queue:
    node = queue.popleft()

    for i in tree[node]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = node

for i in range(2, len(visited)):
    print(visited[i])