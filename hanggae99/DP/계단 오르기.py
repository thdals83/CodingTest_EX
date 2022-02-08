from typing import List
import sys
from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    x = Solution()
    n = 3
    print(x.climbStairs(n))