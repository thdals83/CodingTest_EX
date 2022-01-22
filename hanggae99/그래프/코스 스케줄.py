from typing import List
from collections import defaultdict
# 순환 구조가 되면, False
# 순환 구조가 이뤄나지 않으면서, 모든 코스가 방문되면 True
# 여기서 그래프 형식 (dic)으로 만들고,

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)
        print(graph)
        for x in list(graph):
            print(x)

        return True

if __name__ == "__main__":
    x = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    prerequisites2 = [[0,1], [0,2], [1,2]]
    print(x.canFinish(numCourses, prerequisites))