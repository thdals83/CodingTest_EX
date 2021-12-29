
arr = []

for _ in range(5):
    arr.append(list(map(int,input().split())))

res = 0

for _ in range(5):
    inp = list(map(int,input().split()))
    for x in inp:
        che = 0
        res += 1
        # x인 점 찾기
        for i in range(5):
            for j in range(5):
                if arr[i][j] == x:
                    arr[i][j] = 0
                    break

        # 가로 빙고 찾기

        for i in range(5):
            cnt = 0
            for j in arr[i]:
                if j == 0: cnt +=1
            if cnt == 5: che += 1

        # 세로 빙고 찾기

        for i in range(5):
            cnt = 0
            for j in range(5):
                if arr[j][i] == 0:cnt +=1
            if cnt == 5: che += 1

        # 정대각선 빙고 찾기
        cnt = 0
        for i in range(5):
            if arr[i][i] == 0: cnt +=1
        if cnt == 5: che += 1

        # 반대대각선 빙고 찾기
        cnt = 0
        tmp = 4
        for i in range(5):
            if arr[i][tmp - i] == 0: cnt +=1
        if cnt == 5: che += 1

        if che >= 3:
            break

    if che >= 3:
        break

print(res)