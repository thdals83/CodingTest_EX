'''
DP = 메모지제이션 방식
'''
n = int(input())
dp = [0] * (n + 1)
'''
def fibo(n):
    if n == 2 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

'''

dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]



print(dp[n])
