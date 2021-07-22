def solution(length,weight,truck):
    answer = 1
    ing = []
    timeset = []
    ing.append(truck.pop(0))
    timeset.append(0)

    while True:
        if len(ing) == 0: break
        answer += 1

        for i in range(len(timeset)):
            timeset[i] += 1

        if timeset[0] == length:
            ing.pop(0), timeset.pop(0)

        if len(truck) != 0:
            if sum(ing) + truck[0] <= weight:
                ing.append(truck.pop(0))
                timeset.append(0)

    return answer

if __name__ =="__main__":
    l = 100
    w = 100
    t = [10,10,10,10,10,10,10,10,10,10]
    print(solution(l,w,t))