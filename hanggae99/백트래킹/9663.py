def check(x):
    for i in range(x):
        # 앞에꺼, 열에서 겹치는지 확인,
        # 뒤에꺼 대각선 겹치는지 확인
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False

    return True

def dfs(x):
    global res

    # x( = lv n(x는 행의 번째를 의미해, n과 같으면 성공이므로, 추가)
    if x == n:
        res += 1

    else:
        #dfs(x)에서 x가 행을 의미한다면, row배열은 말 그대로 row를 의미.
        for i in range(n):
            row[x] = i

            if check(x):
                dfs(x + 1)


n = int(input())
row = [-1] * n
res = 0

dfs(0)

print(res)
