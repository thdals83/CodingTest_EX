import heapq
from collections import defaultdict
import sys
input = sys.stdint.readline

t = int(input())

for _ in range(t):
    maxq, minq = [], []
    cnt = 0
    element  = defaultdict(int)

    x = int(input())
    for _ in range(x):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
            element[num] += 1
            cnt +=1
        else:
            if cnt > 0:
                if num == 1:
                    while True:
                        del_num = -heapq.heappop(maxq) # ele 가 이미 0이면 빠져나간 수이므로 계속 삭제
                        if element[del_num] != 0:
                            element[del_num] -= 1
                            break
                else:
                    while True:
                        del_num = heapq.heappop(minq)  # ele 가 이미 0이면 빠져나간 수이므로 계속 삭제
                        if element[del_num] != 0:
                            element[del_num] -= 1
                            break
            cnt -= 1


if cnt:
    while True:
        max_v = -heapq.heappop(maxq)
        if element[max_v] != 0:
            break
    while True:
        min_v = heapq.heappop(minq)
        if element[min_v] != 0:
            break
    print(max_v, min_v)
else:
     print('EMPTY')