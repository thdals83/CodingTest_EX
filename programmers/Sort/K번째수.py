def solution(arr,com):
    res = []

    for i in range(len(com)):
        box = []
        for j in range(int(com[i][0]) - 1, int(com[i][1])):
            box.append(arr[j])
        box.sort()
        res.append(box[com[i][2]-1])

    return res

if __name__ == "__main__":
    a = [1, 5, 2, 6, 3, 7, 4]
    c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(a,c))