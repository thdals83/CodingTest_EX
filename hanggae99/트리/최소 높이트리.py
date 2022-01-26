from typing import List
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1: return [0]

        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

if __name__ == "__main__":
    x = Solution()
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(x.findMinHeightTrees(n,edges))