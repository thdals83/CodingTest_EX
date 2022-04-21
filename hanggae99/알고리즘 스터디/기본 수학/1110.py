n = int(input())

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