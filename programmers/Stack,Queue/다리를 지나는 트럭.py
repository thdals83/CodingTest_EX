from collections import deque
# 경과시간 1씩 추가
# 건너고 있는 트럭 (ing) 1씩 증가
# 대기 트럭에 트럭이 있는 경우
# => 현재 ing 와 대기트럭을 더했을 때 weight보다 작은 경우
#  => ing.apppend 트럭(0)
# 대기 트럭에 트럭이 없는 경우
#
def solution(length,weight,truck):
    answer = 1
    truck = deque(truck)
    ingweight = deque()
    ingtruck = deque()

    ingtruck.append(0)
    ingweight.append(truck[0])
    truck.popleft()

    while ingtruck:
        answer += 1

        for i in range(len(ingtruck)):
            ingtruck[i] += 1

        while ingtruck:
            if ingtruck[0] == length:
                ingtruck.popleft()
                ingweight.popleft()
            else:
                break

        if truck:
            if sum(ingweight) + truck[0] <= weight:
                ingtruck.append(0)
                ingweight.append(truck[0])
                truck.popleft()

    return answer

if __name__ =="__main__":
    l = 2
    w = 10
    t = [7,4,5,6]
    print(solution(l,w,t))