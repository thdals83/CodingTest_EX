from typing import List
import heapq
INF = int(1e9)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [INF] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        for time in times:
            graph[time[0]].append((time[1],time[2]))


        queue = [(k, 0)]
        distance[k] = 0

        while queue:
            node, dist = heapq.heappop(queue)

            if distance[node] < dist: continue

            for i in graph[node]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (i[0], cost))

        if max(distance[1:]) == INF: return -1
        return max(distance[1:])


if __name__ == "__main__":
    x = Solution()
    times = [[1,2,1]]
    n = 2
    k = 2
    print(x.networkDelayTime(times,n,k))
