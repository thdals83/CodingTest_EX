

n, m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(input())
res = 0
for _ in range(m):
    tmp = input()
    if tmp in arr:
        res += 1

print(res)