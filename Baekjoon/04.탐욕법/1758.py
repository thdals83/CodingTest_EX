import heapq, sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    heapq.heappush(arr,- int(input()))

num = 1
res = 0
while arr:
    money = - heapq.heappop(arr)
    give = money - (num - 1)
    num += 1
    if give <= 0: break
    else:
        res += give

print(res)