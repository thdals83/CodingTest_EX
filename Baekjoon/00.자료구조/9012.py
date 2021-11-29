n = int(input())

for _ in range(n):
    arr = list(input())
    cnt = 0
    che = True
    for i in arr:
        if cnt == 0:
            if i == ')':
                cnt -= 1
                break
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0: print("YES")
    else:
        print("NO")