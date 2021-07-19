'''
def solution(cl):
    arr={}
    for i in cl:
        if i[-1] in arr:
            arr[i[-1]] = arr[i[-1]] + 1
        else:
            arr[i[-1]] = 1

    sum = 1
    for i  in arr.values():
        sum = sum * (i+1)

    return sum-1
'''

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


if __name__ =="__main__":
    c=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(c))