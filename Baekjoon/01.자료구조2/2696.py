import heapq as hq
import sys
input = sys.stdin.readline

def solution(data):
    min_q = []
    max_q = []
    mid = data[0]
    result = [mid]

    for idx, val in enumerate(data[1:]):
        if val > mid:
            hq.heappush(min_q, val)
        else:
            hq.heappush(max_q, (-val, val))

        if idx % 2 == 1:
            if len(max_q) < len(min_q):
                hq.heappush(max_q, (-mid, mid))
                mid = hq.heappop(min_q)
            elif len(max_q) > len(min_q):
                hq.heappush(min_q, mid)
                mid = hq.heappop(max_q)[1]
            result.append(mid)

    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


x = int(input().rstrip())
for _ in range(x):
    arr = []
    n = int(input().rstrip())
    if n % 10 == 0:
        for _ in range(n // 10):
            arr.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(n // 10 + 1):
            arr.extend(list(map(int, input().rstrip().split())))
    solution(arr)