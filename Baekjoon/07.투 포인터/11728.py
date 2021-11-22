import sys
input = sys.stdin.readline
a,b = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

arr = sorted(x + y)

for i in arr:
    print(i,end = " ")