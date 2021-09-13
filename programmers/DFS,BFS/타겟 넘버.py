'''
def solution(n,target):
    arr = [0]
    for i in n:
        tmp = []
        for j in arr:
            tmp.append(i + j)
            tmp.append(j - i)
        arr = tmp

    return arr.count(target)
'''
from collections import deque

def solution(n,target):
    answer = 0
    queue = deque()
    num = len(n)
    queue.append([n[0],0])
    queue.append([-1*n[0],0])


    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < num:
            queue.append([temp + n[idx], idx])
            queue.append([temp - n[idx], idx])
        else:
            if temp == target:
                answer +=1



    return answer




if __name__ == "__main__":
    num = [1, 1, 1, 1, 1]
    t = 3
    print(solution(num, t))