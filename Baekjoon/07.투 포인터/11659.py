import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))
add = [0]

for i in range(n):
    add.append(add[-1] + arr[i])

for _ in range(m):
    x, y = map(int,input().split())
    if x == 1: print(add[y])
    else:
        print(add[y] - add[x-1])