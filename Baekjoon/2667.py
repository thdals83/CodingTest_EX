# BFS 문제
from collections import deque

def solution(arr,n):
    res = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                queue.append([i,j])
                arr[i][j] = 0
                count = 1
                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        a = x + dx[k]
                        b = y + dy[k]
                        if 0 <= a < n and 0 <= b < n and arr[a][b] == 1:
                            count += 1
                            queue.append([a, b])
                            arr[a][b] = 0
                res.append(count)

    return res

if __name__ == "__main__":
    num = int(input())
    arr = []
    for _ in range(num):
        arr.append(list(map(int,input())))

    result = solution(arr,num)
    result.sort()

    print(len(result))
    for i in result:
        print(i)
