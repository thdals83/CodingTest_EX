
def solution(progresses,speeds):
    answer = []
    boxs = []
    for x,y in zip(progresses,speeds): boxs.append([x,y])
    n = -1
    while len(boxs) != 0:
        check = True
        num = 0
        while num != len(boxs):
            if boxs[num][0] < 100: break
            else:
                boxs.pop(num)
                if not check:
                    answer[n] += 1
                else:
                    answer.append(1)
                    n += 1
                    check = False

        for box in boxs:
            box[0] += box[1]
    return answer

if __name__ =="__main__":
    p = [93, 30, 55]
    s= [1, 30, 5]
    p1=[95, 90, 99, 99, 80, 99]
    s1=[1, 1, 1, 1, 1, 1]
    print(solution(p,s))