import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
    exit(0)

cnt = 1
best = sum(arr[0:x])
tmp = best

for i in range(x, n):
    tmp -= arr[i - x]
    tmp += arr[i]
    if best <= tmp:
        if best == tmp:
            cnt += 1
        else:
            best = tmp
            cnt = 1

print(best)
print(cnt)
