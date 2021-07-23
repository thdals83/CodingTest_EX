import heapq

def solution(sco,k):
    answer = 0
    heapq.heapify(sco)

    while len(sco) != 1:
        x = heapq.heappop(sco)
        if x >= k: return answer
        else:
            y = heapq.heappop(sco)
            heapq.heappush(sco, x + (y * 2))
        answer = answer + 1

    if sco[0] >= k: return answer
    else: return -1

if __name__ =="__main__":
    s = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(s, k))