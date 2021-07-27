def solution(arr,com):
    res = []

    for i in range(len(com)):
        tmp = []
        for j in range(com[i][0]-1,com[i][1]):
            tmp.append(arr[j])
        tmp.sort()
        res.append(tmp[com[i][2]-1])

    return res

if __name__ == "__main__":
    a = [1, 5, 2, 6, 3, 7, 4]
    c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(a,c))