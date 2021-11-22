from collections import deque
#dfs문제
#dfs는 큐를 이용해서 연결되있는 곳을 하나씩 보면서 감

com = int(input())
graph = [[0 for i in range(com + 1)] for _ in range(com + 1)]
visited = [0] * (com + 1)
queue = deque()


line = int(input())
for _ in range(line):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

res = 0
queue.append(1)
visited[1] = 1
while queue:
    node = queue.popleft()

    for i in range(1, com + 1):
        if graph[node][i] and visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            res += 1

print(res)