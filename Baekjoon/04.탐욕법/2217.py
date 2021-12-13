n = int(input())


arr = []
res = 0
for _ in range(n):
    arr.append(int(input()))

arr.sort()

while arr:
    if res == 0:
        res = len(arr) * arr[0]
    else:
        if res < len(arr) * arr[0]:
            res = len(arr) * arr[0]

    arr.pop(0)


print(res)