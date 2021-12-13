import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

start = price[0]
distint = dist[0]
res = 0
for i in range(1, n - 1):
    if start > price[i]:
        res += start * distint
        start = price[i]
        distint = dist[i]

    else:
        distint += dist[i]

res += start * distint

print(res)