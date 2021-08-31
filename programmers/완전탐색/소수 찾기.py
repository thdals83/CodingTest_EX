from itertools import permutations


def solution(numbers):
    answer = 0
    arr = []

    for i in range(1, len(numbers) +1):
        tmp = list(permutations(numbers, i))
        tmp = list(set(tmp))
        for j in tmp:
            if int(''.join(j)) == 0 or int(''.join(j)) == 1:
                x = 1
            else:
                arr.append(int(''.join(j)))
    arr = list(set(arr))

     #소수 체크
    for i in arr:
        x = 2
        while x*x <= i:
            if i % x == 0:
                answer -= 1
                break
            x += 1
        answer += 1

    return answer


if __name__ == "__main__":
    n = "17"
    n1 = "011"
    print(solution(n1))
