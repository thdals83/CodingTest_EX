import math
import time
from typing import List

# 내가 푼 풀이
def twoSum(nums: List[int], target: int) -> List[int]:

    for i in range(len(nums)):
        tmp = target - nums[i]

        if tmp in nums[i+1:]:
            y = nums[i+1:].index(tmp) + (i + 1)
            break
            # print(i, y)

    return [i,y]

# 책 풀이
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):

        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


if __name__ == "__main__":
    start = time.time()
    math.factorial(100000)

    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums,target))

    end = time.time()
    print(f"{end - start:.5f} sec")
