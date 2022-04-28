
'''
s에서 시작해 t로 끝나는 n개의 수업
최소의 강의실 사용해 모든 수업 가능하게 해야함

수업이 끝난 직후 다음 수업ㅇㄹ 시작
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
studys = []
for _ in range(n):
    s, t = map(int,input().split())
    studys.append([s, t])

studys = sorted(studys, key=lambda x:x[0])

rooms = []
heapq.heappush(rooms, studys[0][1])

for i in range(1, len(studys)):
    if studys[i][0] < rooms[0]:
        heapq.heappush(rooms, studys[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, studys[i][1])
print(len(rooms))