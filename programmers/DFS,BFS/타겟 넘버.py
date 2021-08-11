
def solution(n,target):
    arr = [0]
    for i in n:
        tmp = []
        for j in arr:
            tmp.append(i + j)
            tmp.append(j - i)
        arr = tmp

    return arr.count(target)


if __name__ == "__main__":
    num = [1, 1, 1, 1, 1]
    t = 3
    print(solution(num, t))