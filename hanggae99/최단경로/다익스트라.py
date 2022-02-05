import heapq
INF = int(1e9)

def dijkstra(start):
    queue = []

    heapq.heappush(queue,(start, 0))
    distance[start] = 0

    while queue:
        node, dist = heapq.heappop(queue)

        if distance[node] < dist: continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(i[0],cost))


n, m = map(int,input().split())
start = int(input())

graph = [[] for _ in range (n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("fail")
    else:
        print(distance[i])
