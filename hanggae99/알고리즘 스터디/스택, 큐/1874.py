import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range (n):
    arr.append(int(input()))

idx = 0
tmp = 1
stack = []
res = []
for i in range(1, n + 1):
    stack.append(i)
    res.append('+')
    while stack:
        if stack[-1] == arr[idx]:
            res.append('-')
            stack.pop()
            idx += 1
        else:
            break

if len(stack) == 0:
    for word in res:print(word)
else:
    print("NO")