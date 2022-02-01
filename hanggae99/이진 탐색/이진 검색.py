import bisect
from typing import List


'''
# 이진 탐색 재귀 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left,right):
            if left <= right:
                mid = (left + right)//2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0,len(nums) - 1)
'''

'''
# 반복문
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return - 1
'''

# 이진 검색 알고리즘 bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums,target)

        if index < len(nums) and nums[index] == target:
            return  index
        else:
            return -1


if __name__ == "__main__":
    x = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9

    print(x.search(nums,target))