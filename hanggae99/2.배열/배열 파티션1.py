from typing import List

# n개의 페어기 때문에 짝수로 진행된다.
'''
min(a,b)의 합으로 가장 큰 수를 만드려면, 작은 수 끼리 묶고 큰 수끼리 묶어야 한다.
 => 그럼 만들수있는 것들이 뭐가 있을까?
 => 정렬하면 되겠네
 => num.length 도 짝수
'''


#파이썬다운 방식
def arrayPairSum (nums: List[int]) -> int:
    print(sorted(nums)[::2])
    return sum(sorted(nums)[::2])

'''
# 내가 푼 풀이
def arrayPairSum (nums: List[int]) -> int:
    res = 0
    #정렬
    nums.sort()

    for i in range(0, len(nums),2):
        print(i)
        res += nums[i]

    return res
'''
if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    nums2 = [6, 2, 6, 5, 1, 2]
    print(arrayPairSum(nums2))