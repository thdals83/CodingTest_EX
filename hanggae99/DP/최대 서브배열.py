import bisect
from typing import List
import sys
'''
# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            if nums[i] + nums[i - 1] < nums[i]:
                continue
            else:
                nums[i] += nums[i - 1]

        return max(nums)
'''
# 카테인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__ == "__main__":
    x = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print(x.maxSubArray(nums))