#bfs
from collections import deque


def solution(n,path,arr):
    res = 0
    visited = [0] * (n+1)
    queue = deque()
    queue.append(1)

    while queue:
        node = queue.popleft()
        visited[node] = 1

        for i in range(1, n+1):
            if visited[i] == 0 and arr[node][i] == 1:
                queue.append(i)
                visited[i] = 1

    return visited.count(1) - 1

if __name__ == "__main__":
    n = int(input())
    path = int(input())
    graph = [[0 for i in range(n+1)] for _ in range(n+1)]
    for _ in range(path):
        x, y = map(int,input().split())
        graph[x][y] = graph[y][x] = 1

    print(solution(n,path,graph))

