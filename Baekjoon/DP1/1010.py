import math
'''
m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수
mCn 공식을 이용한다. m!/ (m-n)!n! 공식
'''

x = int(input())

for _ in range(x):
    n, m = map(int,input().split())
    bridge = math.factorial(m) // (math.factorial(m-n) * math.factorial(n))
    print(bridge)