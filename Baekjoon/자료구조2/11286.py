import heapq
import sys
input = sys.stdin.readline


arr = []
heapq.heapify(arr)

x = int(input())

for _ in range(x):
    n = int(input())
    if n == 0:
        if len(arr) == 0:
            print(0)
            continue
        else:
            print(heapq.heappop(arr)[1])
    else:
        if n < 0:
            heapq.heappush(arr, (-n,n))
        else:
            heapq.heappush(arr, (n,n))


