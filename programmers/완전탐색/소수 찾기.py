def solution(s):
    answer = 0

    new_s = list(s)
    for i in range(2, len(s) + 1):
        pm = list(permutations(s, i))
        for j in pm:
            if len(j) <= len(s):
                new_s.append(''.join(j))
    new_s = list(set([int(x) for x in new_s]))

    if new_s.count(1):
        new_s.remove(1)
    if new_s.count(0):
        new_s.remove(0)

    for x in new_s:
        i = 2
        while i * i <= x:
            if x % i == 0:
                answer -= 1
                break
            i += 1
        answer += 1

    return answer


if __name__ == "__main__":
    n = "17"
    n1 = "011"
    print(solution(n1))

'''
- 순열을 구하는 함수 permutatinos 을 쓸 경우 모든 경우의 수를 다 
생각하기 때문에 결국 시간초과가 뜨고 만다.
from itertools import permutations
def solution(num):
    res = []
    num1=list(map(str,num))
    for i in permutations(num1,len(num)):
        res.append(''.join(i))
    return str(max(res))
'''