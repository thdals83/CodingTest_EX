

import sys
input = sys.stdin.readline


n,m = map(int,input().split())
dict = {}

for i in range(1, n + 1):
    x = input().rstrip()
    dict[x] = i
    dict[i] = x


for _ in range(m):
    res = input().rstrip()

    if res.isdigit():
        print(dict[int(res)])
    else:
        print(dict[res])