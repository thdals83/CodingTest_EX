import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

res = [0]

'''
for target in arr:
    if res[-1] < target:
        res.append(target)

    else:
        left = 0
        right = len(res)

        while left < right:
            mid = (left + right) // 2
            if res[mid] < target:
                left = mid + 1
            else:
                right = mid

        res[right] = target
'''

for target in arr:
    if res[-1] < target:
        res.append(target)

    else:
        che = bisect_left(res,target)
        print(res,target)
        print(che)
        res[che] = target

print(len(res) - 1)
