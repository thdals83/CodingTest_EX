from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =  [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            print(i,cur)

            while stack:
                if cur > temperatures[stack[-1]]:
                    last = stack.pop()
                    res[last] = i -last
                else:
                    break

            stack.append(i)

        return res

if __name__ == "__main__":
    x = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(x.dailyTemperatures(temperatures))







