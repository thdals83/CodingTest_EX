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