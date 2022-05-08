

def solution(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == "__main__":
    target = 7
    arr = [1, 3, 5, 6, 7, 9, 11, 15, 19, 17]
    print(solution(target,arr))
