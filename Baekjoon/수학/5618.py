import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

def gcd(a,b):
    if a == 0: return b
    return gcd(b % a, a)

res = gcd(arr[0], gcd(arr[1], arr[-1]))

for i in range(1, (res//2) + 1):
    if res % i == 0:
        print(i)

print(res)