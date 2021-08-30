
def solution(scores):
    res = ''
    n = 0
    for _ in range(len(scores)):
        arr = []
        for i in range(len(scores)):
            arr.append(scores[i][n])

        #print(arr)
        # 자기가 준 값이 최대면서 갯수가1개일때
        if arr[n] == max(arr) and arr.count(max(arr)) == 1 :
            arr.pop(n)
        elif arr[n] == min(arr) and arr.count(min(arr)) == 1 :
            arr.pop(n)
        n += 1

        avg = sum(arr) //len(arr)
        if avg >= 90:
            res += 'A'
        elif 80 <= avg < 90:
            res += 'B'
        elif 70 <= avg < 80:
            res += 'C'
        elif 50 <= avg < 70:
            res += 'D'
        else:
            res += 'F'

    return res

if __name__ == "__main__":
    a = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
    b = [[50,90],[50,87]]
    c = [[70,49,90],[68,50,38],[73,31,100]]
    print(solution(c))
