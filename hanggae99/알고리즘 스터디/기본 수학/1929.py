
num = 1000001
arr = [True] * (num + 1)
arr[0] = False
arr[1] = False

for i in range(2, num + 1):
    if arr[i]:
        j = 2

        while (i * j) <= num:
            arr[i * j] = False
            j += 1

m,n = map(int,input().split())

for i in range(m, n + 1):
    if arr[i]:
        print(i)