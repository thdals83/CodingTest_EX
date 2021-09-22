
from collections import deque


def solution(f, s, g, u, d):
    visited = [0] * (f + 1)
    queue = deque()
    queue.append([s,0])
    visited[s] = 1

    while queue:
        node, num = queue.popleft()
        if node == g: return num
        num += 1

        if node - d >= 1 and visited[node - d] == 0:
            queue.append([node - d, num])
            visited[node - d] = 1
        if node + u <= f and visited[node + u] == 0:
            queue.append([node + u, num])
            visited[node + u] = 1

    return "use the stairs"


if __name__ == "__main__":
    x, y, z, a, b = map(int,input().split())
    print(solution(x, y, z, a, b))