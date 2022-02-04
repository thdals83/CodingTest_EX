import bisect
from typing import List
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        pivot = nums.index(min(nums))

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1
'''
class Solution:
    def bs_rotated(self,nums, target):

        def bs(lst, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if lst[mid] < target:
                return bs(lst, mid + 1, end)
            elif lst[mid] > target:
                return bs(lst, start, mid - 1)
            else:
                return mid

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        added = nums + nums[:left]
        print(added,left,len(added) - 1)

        result = bs(added, left, len(added) - 1)

        return result if result == -1 else result % len(nums)



if __name__ == "__main__":
    x = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0

    print(x.bs_rotated(nums,target))