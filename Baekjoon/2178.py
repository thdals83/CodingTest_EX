# BFS 문제
from collections import deque

def bfs(n,m,arr):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append([[0, 0], 0])

    while queue:
        tmp = queue.popleft()
        x, y, num = tmp[0][0], tmp[0][1], tmp[1]
        num += 1

        if x == n - 1 and y == m - 1: return num
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and arr[a][b] == 1:
                queue.append([[a,b],num])
                arr[a][b] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input())))

    print(bfs(n,m,arr))
