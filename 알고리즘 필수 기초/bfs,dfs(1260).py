'''
DFS와 BFS로 탐색한 결과 출력
- 방문할 수 있는 정점이 여러 개면 가장 작은 것 부터
'''
from collections import deque
'''
# dfs - stack
def dfs(graph, num, target):
    res = ""
    visited = [0 for _ in range(num + 1)]
    stack = [target]

    while stack:
        node = stack.pop()

        if visited[node] == 0:
            visited[node] = 1
            res += str(node) + " "

            for i in range(num, 0, -1):
                if visited[i] == 0 and graph[node][i] == 1:
                    stack.append(i)

    return res
'''

def dfs(target):
    visited[target] = 1
    print(target, end = ' ')

    for i in range(1, n + 1):
        if visited[i] == 0 and graph[target][i] == 1:
            dfs(i)

# bfs
def bfs(graph, num, target):
    visited = [0 for _ in range(num + 1)]
    queue = deque([target])
    visited[target] = 1
    res =""

    while queue:
        node = queue.popleft()
        res += str(node) + " "

        for i in range(1, num + 1):
            if visited[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited[i] = 1

    return res

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    visited = [0 for _ in range(n + 1)]
    dfs(v)
    print("")
    print(bfs(graph, n, v))