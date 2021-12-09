n = input()

# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다

cnt = 0
res = n
while True:
    cnt += 1
    res = str(res)
    if int(res) < 10:
        res = '0' + res
    tmp = 0
    for i in res:
        tmp += int(i)
    tmp = str(tmp)
    res = res[-1] + tmp[-1]
    res = int(res)

    if res == int(n):
        break

print(cnt)