import heapq

def solution(sco,k):
    answer = 0
    heapq.heapify(sco)

    while True:
        if len(sco) == 0: return -1
        if len(sco) == 1:
            if sco[0] >= k: break
            else: return -1
        if sco[0] >= k: break

        heapq.heappush(sco,heapq.heappop(sco) + (heapq.heappop(sco)) *2)
        answer += 1
    return  answer


if __name__ =="__main__":
    s = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(s, k))