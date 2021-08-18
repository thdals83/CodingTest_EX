def solution(n, times):
    # binary search를 위한 sorting
    times.sort()
    # 초기 값 1로 지정(기다리는 사람 1명, 심사관 1분일 때 최소시간)
    min_time = 1
    # 기다리는 사람 모두 심사시간이 가장 긴 심사관에게 갈 때 최대시간
    max_time = times[len(times) - 1] * n

    answer = max_time

    while min_time <= max_time:
        mid_time = int((min_time + max_time) / 2)
        sum = 0

        # mid time일 때, 몇 명 검사할 수 있을지 체크
        for i in range(len(times)):
            sum += int(mid_time / times[i])
        print(sum)
        # n명보다 더 많은 사람을 검사할 수 있을 때 최대시간 감소
        if sum >= n:
            if answer > mid_time: answer = mid_time
            max_time = mid_time - 1
        # n명보다 더 적은 사람을 검사할 수 있을 때 최소시간 증가
        else:
            min_time = mid_time + 1
    return answer


if __name__ == "__main__":
    n = 6
    t = [7, 10]
    print(solution(n,t))