def solution(p,s):
    box=[]
    for i,j in zip(p,s):
        res= (100 - i)
        if res % j == 0:
            box.append(res // j)
        else:
            box.append((res // j) +1)
    sum = 1
    answer =[]
    che =0
    check = box.pop(0)
    while len(box) != 0:
        if check >= box[0]:
            sum = sum +1
            box.pop(0)
            che = 1
        else:
            che =0
            check = box[0]
            answer.append(sum)
            sum = 0
    if che == 1: answer.append(sum)

    return answer

if __name__ =="__main__":
    p = [93, 30, 55]
    s= [1, 30, 5]
    p1=[95, 90, 99, 99, 80, 99]
    s1=[1, 1, 1, 1, 1, 1]
    print(solution(p1,s1))