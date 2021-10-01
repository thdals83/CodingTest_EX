import sys
input = sys.stdin.readline

x, n = input().split()

cnt, res = 0, 0

for i in x[::-1]:
    if i.isalpha():
        num = ord(i) - 55
    else:
        num = i

    res += (int(num) * (int(n) ** cnt))
    cnt += 1

print(res)