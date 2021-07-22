def solution(price):
    answer = []

    for i in range(len(price) -1):
        count = 0
        check = True
        for j in range(i+1, len(price)):
            count = count +1
            if price[i] > price[j]:
                answer.append(count)
                check = False
                break

        if check == True:answer.append(count)

    answer.append(0)

    return answer

if __name__ =="__main__":
    p = [1, 2, 3, 2, 3]
    print(solution(p))