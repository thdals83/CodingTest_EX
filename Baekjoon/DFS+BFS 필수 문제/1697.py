
from collections import deque


def solution(n, k):
    res = 0
    visited = [0] * 100001
    queue = deque()
    queue.append([n,0])
    visited[n] = 1

    while queue:
        node, num = queue.popleft()
        if node == k: return num
        num += 1

        if node - 1 >= 0 and visited[node - 1] == 0:
            queue.append([node - 1, num])
            visited[node - 1] = 1
        if node + 1 <= 100000 and visited[node + 1] == 0:
            queue.append([node + 1, num])
            visited[node + 1] = 1
        if node * 2 <= 100000 and visited[node * 2] == 0:
            queue.append([node * 2, num])
            visited[node * 2] = 1
    return res


if __name__ == "__main__":
    x, y = map(int,input().split())
    print(solution(x,y))