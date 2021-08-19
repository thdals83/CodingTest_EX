def solution(arr):
    res = [-1] * len(arr)
    stack = []
    #원소값, 인덱스 값, 카운트
    box = []
    box.append([arr[0], 0, 1])

    for i in range(1,len(arr)):
        for j in range(len(box)):
            if box[j][0] < arr[i]:
                res[box[j][1]] = box[j][2]
                stack.append(j)
                #여기서 box 인덱스 삭제해줘야하는데 계속 list 길이 걸려서 오류뜸

            else:
                box[j][2] += 1

        box.append([arr[i],i,1])

    return res


if __name__ =="__main__":
    a = [3, 3, 1, 3, 3, 3, 3, 5, 3]
    print(solution(a))
    #[7, 6, 1, 4, 3, 2, 1, -1, -1]
