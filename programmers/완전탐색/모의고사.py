def solution(arr):
    res = [0, 0, 0]
    answer = []
    check =[0,0,0]
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(arr)):
        if A[check[0]] == arr[i]: res[0] = res[0] + 1
        if B[check[1]] == arr[i]: res[1] = res[1] + 1
        if C[check[2]] == arr[i]: res[2] = res[2] + 1

        for i in range(3):
            check[i] = check[i] + 1
            if check[0] == 5: check[0] = 0
            if check[1] == 8 : check[1] = 0
            if check[2] == 10 : check[2] = 0

    for i in range(len(res)):
        if res[i] == max(res): answer.append(i+1)

    return answer