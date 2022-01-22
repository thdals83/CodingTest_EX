from typing import List

# prev_elements, next_elements
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                res.append(prev_elements.copy())

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements.copy()
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return res


if __name__ == "__main__":
    x = Solution()
    nums = [1,2,3]

    print(x.permute(nums))