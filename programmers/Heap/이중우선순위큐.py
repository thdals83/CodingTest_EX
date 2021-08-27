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
    o = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(o))