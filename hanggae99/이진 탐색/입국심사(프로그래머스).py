
def solution(n, times):
    times.sort()
    start, end = 1, times[-1] * n

    while start <= end:
        mid = (start + end) // 2
        sum = 0

        for time in times:
            sum += mid // time

        if sum < n:
            start = mid + 1
        else:
            end = mid - 1

    return start


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n,times))