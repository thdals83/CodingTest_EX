def solution(p,l):
    arr = []
    for i in range(len(p)):
        arr.append([p[i],i])

    i = 0
    res = 1
    while len(arr) != 0:
        if i == len(arr): i = 0

        if arr[0][0] == max(t[0] for t in arr):
            if arr[0][1] == l: return res
            else:
                arr.pop(0)
                res += 1
        else:
            tmp = arr.pop(0)
            arr.append(tmp)

    return res



if __name__ =="__main__":
    p = [2, 1, 3, 2]
    p1 = [1, 1, 9, 1, 1, 1]
    l = 0
    print(solution(p1,l))