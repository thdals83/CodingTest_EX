import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

v, e = map(int,input().split())
k = int(input())

graph =  [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    x, y, w = map(int,input().split())
    graph[x].append([y, w])


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist: continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))

dijkstra(k)

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)