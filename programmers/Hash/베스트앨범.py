
def solution(genres,plays):
    arr = {}
    sum = {}
    i = 0
    for x,y in zip(genres,plays):
        arr[x] = arr.get(x,[]) + [(y,i)]
        sum[x] = sum.get(x,0) + y
        i += 1
    max = sorted(sum.items(), key=lambda x:x[1],reverse=True)
    res =[]
    for i in range(len(max)):
        max2 = sorted(arr[max[i][0]], key=lambda x:x[0],reverse=True)
        if len(max2) < 2:
            res.append(max2[0][1])
        else:
            res.append(max2[0][1])
            res.append(max2[1][1])

    return res



if __name__ =="__main__":
    g = ["classic", "pop", "classic", "classic", "pop"]
    p = [500, 600, 150, 800, 2500]
    print(solution(g,p))