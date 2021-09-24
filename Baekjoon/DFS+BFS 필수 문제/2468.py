from collections import deque
import copy

def dfs(m, n, arr):
    queue = deque()
    check = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] != 0:
                if check == 1: return 0
                check = 1
                queue.append([i, j])
                arr[i][j] = 0
                while queue:
                    q, w = queue.popleft()

                    for k in range(4):
                        dq = q + dx[k]
                        dw = w + dy[k]
                        if 0 <= dq < m and 0 <= dw < n and arr[dq][dw] != 0:
                            queue.append([dq, dw])
                            arr[dq][dw] = 0

    return 1

if __name__ == "__main__":
    x, y = map(int, input().split())
    a = []
    use = []
    count = 0
    for _ in range(x):
        a.append(list(map(int, input().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        che = False
        for i in range(x):
            for j in range(y):
                num = 0
                if a[i][j] != 0:
                    che = True

                    for k in range(4):
                        di = i + dx[k]
                        dj = j + dy[k]
                        if 0 <= di < x and 0 <= dj < y and a[di][dj] == 0:
                            num += 1
                    use.append([i, j, num])

        for i in range(len(use)):
            a[use[i][0]][use[i][1]] -= use[i][2]
            if a[use[i][0]][use[i][1]] < 0: a[use[i][0]][use[i][1]] = 0
        use.clear()

        tmp = copy.deepcopy(a)
        count += 1

        if che == False and dfs(x, y, tmp) == 1:
            print(0)
            break

        if dfs(x, y, tmp) == 0:
            print(count)
            break
