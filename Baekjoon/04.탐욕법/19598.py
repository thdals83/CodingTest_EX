'''
- N개의 회의를 모두 진행할 수 있는 최소 회의실 개수

- 한 회의실에 동시에 두개 이상 진행 안됨
- 끝나는 것과 동시에 시작 가능
'''
import heapq
import sys
input = sys.stdin.readline
n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int,input().split())))

sorted_meetings = sorted(meetings, key=lambda x:x[0])
heap = [sorted_meetings[0][1]]

for i in range(1, len(sorted_meetings)):
    num = heapq.heappop(heap)
    if num <= sorted_meetings[i][0]:
        heapq.heappush(heap, sorted_meetings[i][1])
    else:
        heapq.heappush(heap, num)
        heapq.heappush(heap, sorted_meetings[i][1])


print(len(heap))