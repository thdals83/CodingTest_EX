
n,k =map(int,input().split())

arr = [[0, 0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    arr.append(list(map(int,input().split())))


for i in range(1, n + 1):
    for j  in range(1, k + 1):
        weight = arr[i][0]
        value = arr[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack)
print(knapsack[n][k])