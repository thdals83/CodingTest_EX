import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
res = [0 for _ in range(n)]
stack = []

for i in range(len(arr)-1, -1, -1):
    if len(stack) == 0:
        stack.append([i, arr[i]])
    else:
        while stack:
            if arr[i] < stack[-1][1]:break
            tmp = stack.pop()
            res[tmp[0]] = i + 1

        stack.append([i, arr[i]])

print(' '.join(map(str,res)))