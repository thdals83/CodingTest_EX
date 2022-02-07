from collections import defaultdict
'''
# 재귀 브루트 포스
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        return self.fib(n - 1) + self.fib(n - 2)
'''

# 상향식 dp
class Solution:
    def fib(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

if __name__ == "__main__":
    x = Solution()
    n = 4
    print(x.fib(n))