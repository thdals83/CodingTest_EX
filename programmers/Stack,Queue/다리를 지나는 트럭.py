# 경과시간 1씩 추가
# 건너고 있는 트럭 (ing) 1씩 증가
# 대기 트럭에 트럭이 있는 경우
# => 현재 ing 와 대기트럭을 더했을 때 weight보다 작은 경우
#  => ing.apppend 트럭(0)
# 대기 트럭에 트럭이 없는 경우
#
def solution(length,weight,truck):
    answer = 1
    ing = []
    ing.append([truck.pop(0),0])

    while len(ing) != 0:
        answer += 1

        for i in range(len(ing)):
            ing[i][1] += 1

        if ing[0][1] == length: ing.pop(0)

        if len(truck) != 0:
            if sum(x[0] for x in ing)+ truck[0] <= weight:
                ing.append([truck.pop(0),0])

    return answer

if __name__ =="__main__":
    l = 2
    w = 10
    t = [7,4,5,6]
    print(solution(l,w,t))