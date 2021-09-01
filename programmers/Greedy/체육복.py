
def solution(n,lost,reserve):
    reserve1=list(set(reserve)-set(lost))
    lost1=list(set(lost)-set(reserve))

    res = n - len(lost1)
    for i in lost1:
        if i - 1 in reserve1:
            res += 1
            reserve1.remove(i - 1)
        elif i + 1 in reserve1:
            res += 1
            reserve1.remove(i + 1)
    return res


if __name__ == "__main__":
    n = 3
    l = [3]
    r = [1]
    print(solution(n,l,r))