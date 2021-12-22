from collections import defaultdict

n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = defaultdict(list)

res = 0
start = 0
for i in range(len(arr)):
    count[arr[i]].append(i)

    if len(count[arr[i]]) > k:
        res = max(res, i - start)
        start = (count[arr[i]].pop(0) + 1)

    # print(count)
    # print(arr[i], len(count[arr[i]]))
res = max(res, n - start)
print(res)