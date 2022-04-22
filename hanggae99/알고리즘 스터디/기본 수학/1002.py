x = int(input())

for _ in range(x):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)

    add = (r1 + r2) ** 2
    sub = (r1 - r2) ** 2

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d < add and d > sub:
            print(2)
        elif d == add or d == sub:
            print(1)
        else:
            print(0)