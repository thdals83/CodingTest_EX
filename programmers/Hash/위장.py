
def solution(clothes):
    arr = {}
    for i in clothes:
        if i[-1] in arr:
            arr[i[-1]] += 1
        else:
            arr[i[-1]] = 1

    res = 1
    for i in arr.values():
        res *= (i+1)

    return res -1

if __name__ =="__main__":
    c=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(c))