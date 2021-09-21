#BFS 문제
from collections import deque

def soltuon(num,x,y,arr):
    queue = deque()
    visited = [0] * (num + 1)
    queue.append([x, 0])

    while queue:
        node, count = queue.popleft()
        if node == y: return count
        count += 1

        for i in range(1, num + 1):
            if visited[i] == 0 and arr[node][i] == 1:
                queue.append([i,count])
                visited[i] = 1

    return -1


if __name__ == "__main__":
    n = int(input())
    graph = [[0 for i in range(n+1)] for _ in range(n+1)]
    x1, y1 = map(int,input().split())
    path_n = int(input())

    for _ in range(path_n):
        a, b = map(int,input().split())
        graph[a][b] = graph[b][a] = 1

    print(soltuon(n,x1,y1,graph))
