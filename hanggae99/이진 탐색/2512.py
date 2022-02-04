'''
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

res = 0
arr.sort()
arr = deque(arr)

while arr:
    check = m // len(arr)

    if arr[0] <= check:
        drop = arr.popleft()
        m -= drop
        res = max(res,drop)
    else:
        res = max(res,check)
        break

print(res)
'''

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in arr:
        if i >= mid:
            total += mid
        else:
            total += i

    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)