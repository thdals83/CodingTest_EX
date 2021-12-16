import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    minValue = 1e9
    j = 1

    while j**2 <= i:
        minValue = min(minValue, dp[i - (j * j)])
        j += 1
        print(dp)
    dp[i] = minValue + 1

print(dp[n])