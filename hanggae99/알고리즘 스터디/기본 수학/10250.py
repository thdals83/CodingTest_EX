'''
- 정문으로 부터 가장 짧은 거리의 방 배정
- W개방, H층 엘베 왼쪽
'''

x = int(input())
for _ in range(x):
    h, w, n = map(int,input().split())
    if n % h == 0:
        print(str(h) + "0" + str(n // h))
    else:
        print(str(n % h) + "0" + str(n // h + 1))