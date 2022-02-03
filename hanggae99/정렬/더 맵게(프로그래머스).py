import heapq


def solution(sco,k):
    answer = 0
    heapq.heapify(sco)

    while True:
        if len(sco) == 0: return -1
        if len(sco) == 1:
            if sco[0] >= k: return answer
            else: return -1

        if sco[0] >= k: return answer

        heapq.heappush(sco,heapq.heappop(sco) + heapq.heappop(sco) * 2)
        answer += 1

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville,k))