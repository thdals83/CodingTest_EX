import heapq
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    maxq,minq = [],[]
    heapq.heapify(maxq)
    heapq.heapify(minq)
    visited = [0] * 1000001

    for key in range(num):
        x, y = input().split()
        if x == "I":
            heapq.heappush(minq, (int(y), key))
            heapq.heappush(maxq, (-int(y), key))
            visited[key] = 1
        else:
            if int(y) == 1:
                while maxq and visited[maxq[0][1]] == 0:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]] = 0
                    heapq.heappop(maxq)
            else:
                while minq and visited[minq[0][1]] == 0:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]] = 0
                    heapq.heappop(minq)
        print(maxq,minq)

    while minq and visited[minq[0][1]] == 0:
        heapq.heappop(minq)
    while maxq and visited[maxq[0][1]] == 0:
        heapq.heappop(maxq)

    if maxq and minq:
        print(-maxq[0][0], minq[0][0])
    else:
        print('EMPTY')