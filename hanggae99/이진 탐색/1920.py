import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

arr.sort()

def checktarge(target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return True
    return False

# 걍 dic 쓰자

for target in check:
    if checktarge(target):
        print(1)
    else:
        print(0)