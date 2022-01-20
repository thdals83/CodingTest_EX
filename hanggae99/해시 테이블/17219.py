from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dic = defaultdict(str)

for _ in range(n):
    address, pwd = input().split()
    dic[address] = pwd

for _ in range(m):
    res = input().rstrip()
    print(dic.get(res))