from typing import List
import heapq
# prev_elements, next_elements

'''
# heapify 사용 방법
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
'''

'''
# -n 하는 방법
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for n in nums:
            heapq.heappush(arr, -n)

        for _ in range(1,k):
            heapq.heappop(arr)

        return -heapq.heappop(arr)
'''

'''
# nlargest 방법
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
'''

# 파이썬 내장 정렬함수
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

if __name__ == "__main__":
    x = Solution()
    nums = [3,2,1,5,6,4]
    k = 2

    print(x.findKthLargest(nums, k))