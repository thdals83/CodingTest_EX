x=int(input())

def aa(e):
    a = 1
    c = 0
    d = 0
    cnt = 1
    while True:
        for i in range(2):
            c += a
            if d + 1 <= e <= c:
                return cnt
            d = c
            cnt += 1
        a += 1

for i in range(x):
    a,b=map(int,input().split())
    print(aa(b-a))