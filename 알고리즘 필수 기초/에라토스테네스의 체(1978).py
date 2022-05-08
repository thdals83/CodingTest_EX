n = int(input())
che = list(map(int,input().split()))
arr = [1] * (max(che) + 1)
arr[1] = 0

for i in range(2, max(che) + 1):
    if arr[i] == 1:
        j = 2
        while i * j <= max(che):
            arr[i * j] = 0
            j += 1

res = 0
for num in che:
    if arr[num] == 1:
        res += 1

print(res)

