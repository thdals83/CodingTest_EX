from typing import List
from collections import deque
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for x in range(len(grid)):
            for y in range(len(grid[x])):

                if visited[x][y] == 0 and grid[x][y] == "1":
                    res += 1
                    queue.append([x,y])
                    visited[x][y] = 1

                    #BFS
                    while queue:
                        ex, ey = queue.popleft()

                        for i in range(4):
                            fx = ex + dx[i]
                            fy = ey + dy[i]

                            if 0 <= fx <len(grid) and 0 <= fy <len(grid[x]) \
                                    and grid[fx][fy] == "1" and visited[fx][fy] == 0:
                                queue.append([fx, fy])
                                visited[fx][fy] = 1

        return res
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        stack = []
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for x in range(len(grid)):
            for y in range(len(grid[x])):

                if visited[x][y] == 0 and grid[x][y] == "1":
                    res += 1
                    stack.append([x,y])
                    visited[x][y] = 1

                    #DFS
                    while stack:
                        ex, ey = stack.pop()

                        for i in range(4):
                            fx = ex + dx[i]
                            fy = ey + dy[i]

                            if 0 <= fx <len(grid) and 0 <= fy <len(grid[x]) \
                                    and grid[fx][fy] == "1" and visited[fx][fy] == 0:
                                stack.append([fx, fy])
                                visited[fx][fy] = 1

        return res

if __name__ == "__main__":
    x = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(x.numIslands(grid2))




