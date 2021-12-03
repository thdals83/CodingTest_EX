import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict


maxq, minq = [], []
element = defaultdict(int)

n = int(input())
for _ in range(n):
    p,l = map(int, input().split())
    heapq.heappush(minq, [l, p])
    heapq.heappush(maxq, [-l, -p])
    element[p] += 1

m = int(input())
for _ in range(m):
    arr = input().split()
    if arr[0] == "recommend":
        if arr[1] == '1':
            while True:
                if element[-maxq[0][1]] == 0:
                    heapq.heappop(maxq)
                else: break
            print(-maxq[0][1])
        else:
            while True:
                if element[minq[0][1]] == 0:
                    heapq.heappop(minq)
                else: break
            print(minq[0][1])

    elif arr[0] == "solved":
        element[int(arr[1])] = 0
    else:
        while True:
            if element[-maxq[0][1]] == 0:
                heapq.heappop(maxq)
            else:
                break
        while True:
            if element[minq[0][1]] == 0:
                heapq.heappop(minq)
            else:
                break
        element[int(arr[1])] += 1
        heapq.heappush(minq, [int(arr[2]), int(arr[1])])
        heapq.heappush(maxq, [-int(arr[2]), -int(arr[1])])