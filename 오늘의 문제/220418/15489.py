r, c, w = map(int,input().split())

arr = [[1]]
n = 0
while n < 32:
    tmp = []
    for i in range(len(arr[-1]) + 1):
        if i == 0:
            tmp.append(arr[-1][0])
        elif i == len(arr[-1]):
            tmp.append(arr[-1][-1])
        else:
            tmp.append(arr[-1][i-1] + arr[-1][i])

    arr.append(tmp)
    n += 1

r -= 1
c -= 1
sum = 0
for i in range(w):
    for j in range(i + 1):
        sum += arr[r + i][c + j]
        # print(arr[r + i][c + j], end=" ")
    # print()

print(sum)