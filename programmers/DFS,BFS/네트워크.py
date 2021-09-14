from collections import deque

def solution(n, com):
    answer = 0
    bfs = deque()
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        while bfs:
            node = bfs.popleft()
            visited[node] = 1

            for i in range(n):
                if visited[i] == 0 and com[node][i] ==1:
                    bfs.append(i)
                    visited[i] = 1

        answer += 1

    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))