from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])

    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n,edge):
    answer = 0
    #그래프 보관 배열 선언
    adj = [[] for _ in range(n + 1)]

    # 방문 횟수 기록 배열
    visited = [-1] * (n + 1)

    #그래프 만들어 주기
    for i in edge:
        x = i[0]
        y = i[1]
        adj[x].append(y)
        adj[y].append(x)

    #최단거리 입력 bfs
    bfs(1,visited,adj)

    # 먼 노드 개수
    for i in visited:
        if i == max(visited):
            answer += 1
    return answer


if __name__ == "__main__":
    n = 6
    v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n,v))
