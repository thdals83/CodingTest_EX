import sys
input = sys.stdin.readline
# 높이 h로 설정하면 그 위로 잘림
# M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을

n, m = map(int,input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for tree in arr:
        if tree > mid:
            total += tree - mid

    if total >= m:
        start = mid + 1
    elif total < m:
        end = mid - 1

print(end)