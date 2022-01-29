from typing import List
import heapq
# prev_elements, next_elements


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        arr = sorted(nums, key = lambda x:x*10, reverse= True)

        return str(int(''.join(arr)))


if __name__ == "__main__":
    x = Solution()
    nums = [3,30,34,5,9]
    print(x.largestNumber(nums))