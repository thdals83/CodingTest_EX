def solution(price):
    answer = []

    for i in range(len(price)):
        count = 0
        for j in range(i+1,len(price)):
            count += 1
            if price[i] > price[j]:break
        answer.append(count)

    return answer

if __name__ =="__main__":
    p = [1, 2, 3, 2, 3]
    print(solution(p))