from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        dfs(0, "")

        return res
'''
#반복문
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [""]
        for c in digits:
            tmp = []
            for y in res:
                for x in kvmaps[c]:
                    tmp.append(y + x)

            res = tmp
        return res
'''

if __name__ == "__main__":
    x = Solution()
    digits = "234"

    print(x.letterCombinations(digits))