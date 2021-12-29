from collections import defaultdict
n = int(input())

arr = [-1] * 11
res = 0

for _ in range(n):
    x,y = map(int,input().split())
    if arr[x] == -1:
        arr[x] = y
    else:
        if arr[x] == y:
            continue
        else:
            arr[x] = y
            res += 1

print(res)