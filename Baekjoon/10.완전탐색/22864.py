a, b, c, m = map(int,input().split())

res = 0
pirodo = 0
for _ in range(24):
    if pirodo + a <= m:
        res += b
        pirodo += a
    else:
        pirodo -= c
        if pirodo < 0:
            pirodo = 0

print(res)

'''
한시간 일하면 피로도 A 쌓이고 B만큼 일함
한시간 쉬면 C만큼 줄어들고 피로도는 M을 넘으면 안됨
24시간 동안 최대한 많이 일해야함

'''