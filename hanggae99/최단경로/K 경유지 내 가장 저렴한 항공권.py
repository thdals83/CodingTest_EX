import collections
from typing import List
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0
        d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            d[u] += [(v, p)]

        queue = [(src, -1, 0)]

        while queue:
            pos, k, cost = queue.pop(0)
            if pos == dst or k == K: continue
            for nei, p in d[pos]:
                if cost + p >= seen[nei]:
                    continue
                else:
                    seen[nei] = cost + p
                    queue += [(nei, k + 1, cost + p)]

        return seen[dst] if seen[dst] < float('inf') else -1

if __name__ == "__main__":
    x = Solution()
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1

    print(x.findCheapestPrice(n, flights, src, dst, k))