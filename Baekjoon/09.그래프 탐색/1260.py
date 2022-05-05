'''
DFS와 BFS로 탐색한 결과 출력
- 방문할 수 있는 정점이 여러 개면 가장 작은 것 부터
'''
from collections import deque


# dfs - stack
def dfs(graph, num, target):
    res = []
    visited = [0 for _ in range(num + 1)]
    stack = [target]

    while stack:
        node = stack.pop()

        if str(node) not in str(res):
            res.append(str(node))
            for i in range(num, 0, -1):
                if visited[i] == 0 and graph[node][i] == 1:
                    stack.append(i)
                    visited[node] = 1


    return ' '.join(res)


# bfs
def bfs(graph, num, target):
    res = [str(target)]
    visited = [0 for _ in range(num + 1)]
    queue = deque()
    queue.append(target)
    visited[target] = 1

    while queue:
        node = queue.popleft()

        for i in range(1, num + 1):
            if visited[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited[i] = 1
                res.append(str(i))
    return ' '.join(res)


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    print(dfs(graph, n, v))
    print(bfs(graph, n, v))
