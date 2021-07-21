def solution(p,l):
    res = 0
    im = max(p)
    while True:
        x = p.pop(0)
        if im == x:
            res = res + 1
            if l == 0: break
            else:
                l = l - 1
                im = max(p)
        else:
            p.append(x)
            if l == 0: l = len(p) -1
            else: l = l -1

    return res



if __name__ =="__main__":
    p = [1, 1, 9, 1, 1, 1]
    l = 0
    print(solution(p,l))