import heapq
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
num = 1
while True:
    n = int(input())
    if n == 0: break
    graph = []

    for _ in range(n):
        graph.append(list(map(int,input().split())))
    distance = [[INF for _ in range(n)] for _ in range(n)]

    queue = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist: continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue,(cost,nx,ny))

    print("Problem " + str(num) + ": "  + str(distance[-1][-1]))
    num += 1