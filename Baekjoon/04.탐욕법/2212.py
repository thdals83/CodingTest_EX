'''
- 고속도로 위 N개 센서 설치
- 최대 K개 집중국 설치

- 집중국은 센서의 수신 가능 영역 조절
- N개의 센서가 적어도 하나의 집중국과는 통신이 가능

- 각 집중국의 수신 가능 영역의 길이의 합을 최소화

'''

n = int(input())
k = int(input())
arr = list(map(int,input().split()))
arr.sort()

if k >= n:
    print(0)
    exit(0)

dist = []
for i in range(1, n):
    dist.append(arr[i] - arr[i - 1])

dist.sort()
print(dist)
for _ in range(k - 1):
    dist.pop()

print(sum(dist))