n,m = map(int,input().split())

arr = list(map(int,input().split()))

for _ in range(m):
    a, b, c = map(int,input().split())
    b -= 1
    if a == 1:
        arr[b] = c
    elif a == 2:
        for i in range(b, c):
            if arr[i] == 0: arr[i] = 1
            else: arr[i] = 0
    elif a == 3:
        for i in range(b, c): arr[i] = 0
    elif a == 4:
        for i in range(b, c): arr[i] = 1


for i in arr:
    print(i, end = " ")