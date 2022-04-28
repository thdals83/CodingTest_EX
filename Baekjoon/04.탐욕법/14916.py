'''
그리디 알고리즘
2원, 5원 동전의 개수가 최소가 되도록

- 큰 액수가 많을 수록 동전의 개수가 줄어 들 수 있다.
- 13원의 경우 5를 두번 하게 하는 방법이있지만
이로써는 나올 수 없다.

N원이 들어오면 가장 큰 액수가 5*N개 < N원이 안되도록 해야함
'''
import sys
input = sys.stdin.readline

x = int(input())

startmax = x // 5

for i in range(startmax, -1, -1):

    # 5로만 이루어져 있을 경우
    if i * 5 == x:
        print(i)
        exit(0)


    # 2, 5로 이루어져 있을 경우
    tmp = x - (i * 5)
    if tmp < 2: continue

    if tmp % 2 == 0:
        print(i + tmp // 2)
        exit(0)

print(-1)

'''
import sys
input = sys.stdin.readline


x = int(input())
num = x % 5

if x == 1 or x == 3:
    print(-1)
elif num % 2 == 0:
    print(x//5 + num//2)
else:
    print(((x // 5) -1) + ((num + 5) //2))
'''