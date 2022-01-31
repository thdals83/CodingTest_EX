import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    tmp = list(input().split())
    tmp[0] = int(tmp[0])
    arr.append(tmp)

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0],i[1])