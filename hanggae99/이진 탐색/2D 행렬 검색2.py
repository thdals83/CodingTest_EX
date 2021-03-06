import bisect
from typing import List


# 이진 검색 알고리즘 bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if target in mat:
                return True
        return False


if __name__ == "__main__":
    x = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5

    print(x.searchMatrix(matrix,target))