'''
- 장르 별로 가장 많이 재생된 노래를 두 개씩 모아
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
'''

def solution(genres,plays):
    song = {}
    maxgen = {}
    i = 0
    for x, y in zip(genres,plays):
        song[x] = song.get(x,[]) + [[y,i]]
        maxgen[x] = maxgen.get(x, 0) + y
        i += 1

    sortgen = sorted(maxgen.items(), key = lambda x:x[1], reverse=True)
    res = []
    for i in sortgen:
        sortsong = sorted(song[[i[0]][0]], key= lambda x:x[0], reverse= True)
        if len(sortsong)  < 2:
            res.append(sortsong[0][1])
        else:
            res.append(sortsong[0][1])
            res.append(sortsong[1][1])

    return res


if __name__ =="__main__":
    g = ["classic", "pop", "classic", "classic", "pop"]
    p = [500, 600, 150, 800, 2500]
    print(solution(g,p))