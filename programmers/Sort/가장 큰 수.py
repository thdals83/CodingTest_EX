# lambda ?:? 사용하게 되면 함수 사용처럼 할 수 있음
# 여기다가 추가로 .sort(key = lambda 를 사용하여 정렬에 사용할 수 있음
def solution(num):
    num  = list(map(str,num))
    num.sort(key=lambda x:x*3, reverse=True)

    return str(int(''.join(num)))


if __name__ == "__main__":
    n = [6, 10, 2]
    print(solution(n))


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