from collections import deque
n = int(input())
par = list(map(int,input().split()))
x = int(input())
tree = {}

for i in range(n):
    if i == x or par[i] == x:continue
    if par[i] in tree:
        tree[par[i]].append(i)
    else:
        tree[par[i]] = [i]

print(tree)
res = 0
queue = deque()
if -1 in tree: queue.append(-1)

while queue:
    node = queue.popleft()
    if node not in tree:
        res += 1
    else:
        queue += tree[node]

print(res)