import heapq
INF = int(1e9)

def dijkstra(start):
    queue = [(start, 0)]
    distance[start] = 0

    while queue:
        node, dist =heapq.heappop(queue)

        if distance[node] < dist: continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(i[0],cost))

n, m = map(int,input().split())

distance = [INF]  * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))


start = 1
dijkstra(start)

distance.pop(0)
idx = distance.index(max(distance))
cnt = distance.count(distance[idx])
print(idx + 1, distance[idx], cnt)