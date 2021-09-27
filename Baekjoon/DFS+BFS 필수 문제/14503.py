def solution(x, y, d):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    global res
    if arr[x][y] == 0:
        arr[x][y] = 2
        res += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0:
            solution(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    solution(nx, ny, d)


if __name__ == "__main__":
    n, m = map(int,input().split())
    r, c, d = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    res = 0
    solution(r, c, d)
    print(res)