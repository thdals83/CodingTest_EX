def solution(arr):
    x = [1, 2, 3, 4, 5]
    y = [2, 1, 2, 3, 2, 4, 2, 5]
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res = [0, 0, 0]

    n = 0
    for i in arr:
        if i == x[n % len(x)]:
            res[0] += 1
        if i == y[n % len(y)]:
            res[1] += 1
        if i == z[n % len(z)]:
            res[2] += 1
        n +=1

    answer = []
    for i in range(len(res)):
        if res[i] == max(res):
            answer.append(i+1)

    return answer

if __name__ == "__main__":
    n1 = [1,3,2,4,2]
    print(solution(n1))