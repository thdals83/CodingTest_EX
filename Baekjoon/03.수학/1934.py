t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    x1 = x
    y1 = y
    while y != 0:
        x= x % y
        x,y = y,x

    print((x1 * y1) //x)