def solution(genres,plays):
    d = {}
    playsDict = {}

    x = 0
    for i, j in zip(genres, plays):
        playsDict[i] = playsDict.get(i, 0) + j
        d[i] = d.get(i, []) + [(j, x)]
        x = x + 1
    arr = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(len(arr)):
        arr2 = sorted(d[arr[i][0]], key=lambda x: x[0], reverse=True)
        if(len(arr2)==1):res.append(arr2[0][1])
        else:
            res.append(arr2[0][1])
            res.append(arr2[1][1])

    return res

if __name__ =="__main__":
    g = ["classic", "pop", "classic", "classic", "pop"]
    p = [500, 600, 150, 800, 2500]
    print(solution(g,p))