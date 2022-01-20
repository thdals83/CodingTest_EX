import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
needs = list(map(int,input().split()))

dict = defaultdict(int)

for i in arr:
    dict[i] = 1

res = []
for need in needs:
    if dict[need] == 1:
        res.append(1)
    else:
        res.append(0)

for i in res:
    print(i)


