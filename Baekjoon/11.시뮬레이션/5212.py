import copy
r, c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

res = copy.deepcopy(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(r):
    for y in range(c):
        if graph[x][y] == '.': continue
        cnt = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                cnt += 1
                continue
            elif graph[nx][ny] == '.':
                cnt += 1

        if cnt >= 3:
            res[x][y] = '.'
            
start_y, end_y = 0, 0
for i in range(r):
    if 'X' in res[i]:
        start_y = i
        break
for i in range(r - 1, -1, -1):
    if 'X' in res[i]:
        end_y = i
        break

tmp = []
for j in range(c):
    for i in range(start_y, end_y + 1):

        if 'X' == res[i][j]:
            tmp.append(j)
            break

for y in range(start_y, end_y + 1):
    print("".join(res[y][tmp[0]:tmp[-1] + 1]))