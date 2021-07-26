# 이중우선순위 큐 사용법
# heapq.nlargest(최대값 갯수, 리스트) 를 하게되면 배열 형태로 출력됨 그래서 값 하나만 사용하면 앞에 [0]을 사용하기
# 리스트.index() 를 하게되면 해당 값이 있는 위치를 출력시켜 줌
import heapq

def solution(op):
    res = []
    heapq.heapify(res)

    for i in op:
        a,b = i.split(" ")
        if a == 'I': heapq.heappush(res,int(b))
        else:
            if len(res) > 0:
                if b == '1':
                    res.pop(res.index(heapq.nlargest(1, res)[0]))
                else:
                    heapq.heappop(res)

    if len(res) == 0: return [0,0]
    else: return [max(res),min(res)]

if __name__ =="__main__":
    o = ["I 7","I 5","I -5","D 1"]
    print(solution(o))