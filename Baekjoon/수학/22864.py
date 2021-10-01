import sys
input = sys.stdin.readline

a, b, c, m = map(int,input().split())
now = 0
all = 0
for _ in range(24):
    if now + a <= m:
        now += a
        all += b
    else:
        now -= c
        if now < 0:
            now = 0


print(all)

