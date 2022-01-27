from collections import deque
from collections import defaultdict
n = int(input())
par = list(map(int,input().split()))
x = int(input())
tree = defaultdict(list)

for idx, n in enumerate(par):
    if n == x or idx == x: continue
    tree[n].append(idx)

queue = deque()

if -1 in tree:
    queue.append(tree[-1][0])

res =0
while queue:
    node =  queue.popleft()

    if tree[node]:
        for i in tree[node]:
            queue.append(i)
    else:
       res += 1

print(res)