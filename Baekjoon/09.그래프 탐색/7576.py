'''
가로:m 세로: n

- 창고에 보관된 토마토들이 며칠이 지나면 다 익는지 최소일수
- 익은 토마토 4방향 있는 토마토 하루 지나면 영향받아 익음
'''
from collections import deque

m, n = map(int,input().split())
box = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    box.append(list(map(int,input().split())))
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))


while queue:
    x, y = queue.popleft()

    for i in range(4):
        ex = x + dx[i]
        ey = y + dy[i]

        if 0 <= ex < n and 0 <= ey < m and box[ex][ey] == 0:
            queue.append((ex,ey))
            box[ex][ey] = box[x][y] + 1
res = 0

for i in box:
    if 0 in i:
        print(-1)
        exit(0)
    res = max(res, max(i))

print(res - 1)
