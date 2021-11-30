from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    arr = list(input().split())

    if arr[0] == 'push_front':
        queue.appendleft(arr[1])
    elif arr[0] == 'push_back':
        queue.append(arr[1])
    elif arr[0] == 'pop_front':
        if len(queue) == 0: print(-1)
        else:
            print(queue.popleft())
    elif arr[0] == 'pop_back':
        if len(queue) == 0: print(-1)
        else:
            print(queue.pop())
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    elif arr[0] == 'front':
        if len(queue) == 0: print(-1)
        else:
            print(queue[0])
    elif arr[0] == 'back':
        if len(queue) == 0: print(-1)
        else:
            print(queue[-1])