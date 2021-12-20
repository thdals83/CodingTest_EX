t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())

    dp = [0 for i in range(m + 1)]
    dp[0] = 1

    for i in arr:
        for j in range(1, m + 1):

            print(dp)
            print(i,j)
            if j - i >= 0:
                dp[j] += dp[j - i]

    print(dp[m])
