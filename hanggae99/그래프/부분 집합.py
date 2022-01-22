from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(lv, path):
            # 매번 결과 추가
            res.append(path)

            # 경로 만들면서 DFS
            for i in range(lv, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return res


if __name__ == "__main__":
    x = Solution()
    nums = [1, 2, 3]

    print(x.subsets(nums))