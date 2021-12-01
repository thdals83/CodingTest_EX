import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
heap = []

for _ in range(n):
    arr = (list(map(int,input().split())))
    print(heap)
    if not heap:
        for x in arr:
            heapq.heappush(heap,x)
    else:
        for x in arr:
            if heap[0] < x:
                heapq.heappush(heap,x)
                heapq.heappop(heap)

print(heap[0])
