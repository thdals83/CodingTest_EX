import sys
input = sys.stdin.readline

k, n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for lansun in arr:
        total += lansun // mid

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)