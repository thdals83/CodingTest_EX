from collections import defaultdict

n = int(input())

arr = [[0 for i in range (n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tmp = defaultdict(list)
res = 0

for _ in range(n**2):
    inp = list(map(int,input().split()))
    tmp[inp[0]] = inp[1:]

    maxx, maxy = 0, 0
    maxlike,maxempty = -1,-1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                likecnt = 0
                emptycnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in inp:
                            likecnt += 1

                        if arr[nx][ny] == 0:
                            emptycnt += 1

                if maxlike < likecnt or (maxlike == likecnt and maxempty < emptycnt):
                    maxx = i
                    maxy = j
                    maxlike = likecnt
                    maxempty = emptycnt
    arr[maxx][maxy] = inp[0]

for i in range(n):
    for j in range(n):
        cnt = 0
        like = tmp[arr[i][j]]

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in like:
                    cnt += 1

        if cnt != 0:
            res += 10 ** (cnt - 1)


print(res)






