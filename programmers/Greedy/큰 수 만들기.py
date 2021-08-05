'''
- 스택을 활용하여 풀이 -
스택에 넣으려는 수와 마지막 인덱스와 비교해 수가 더 크면
마지막 인덱스를 삭제 하고 k의 개수를 줄여준다.
아니면 push 해주게 된다. 마지막에 k가 0이 아니게 끝나게 되는
경우가 있는데 이는 0이 연속해 나올 경우다. 그래서 스택을 꺼꾸로 바꿈
'''
def solution(num,k):
    stack = [num[0]]

    for i in num[1:]:
        while len(stack) > 0 and stack[-1] < i and k>0:
            k = k - 1
            stack.pop()

        stack.append(i)

    if k != 0: stack = stack[:-k]

    return ''.join(stack)

if __name__ == "__main__":
    n = "4177252841"
    k = 4
    print(solution(n, k))


'''
역시나 안된다 비 효율적
from itertools import combinations
def solution(num,k):

    arr = combinations(num,len(num)-k)
    res = []
    for i in combinations(num,len(num)-k):
        res.append(''.join(i))

    ans= str(max(res))
    return  ans
'''