'''
- 정문으로 부터 가장 짧은 거리의 방 배정
- W개방, H층 엘베 왼쪽
'''

x=int(input())

for i in range(x):
    h,w,n=map(int,input().split())

    if n%h == 0:
        print("%d%02d" % (h, n//h))
    else:
        print("%d%02d" % (n % h, n//h+1))