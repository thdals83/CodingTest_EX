# 서로 다른 L개의 알파벳 소문자들
# 최소 한 개의 모음(a, e, i, o, u)
# 최소 두개의 자음으로 구성
# 중복없이 알파벳 순서로 순열로
def findtrue(cnt):
    cnt = set(cnt)
    tt = set(["a", "e", "i", "o", "u"])

    numbermo = len(cnt & tt)
    if numbermo >= 1 and len(cnt)  - len(cnt & tt) >= 2:
        return True
    else:
        return False

def check(lv,idx, path):

    if l == len(path):
        tmp = path.copy()

        if findtrue(tmp):
            tmp.sort()
            #print(''.join(tmp))
            final.append(''.join(tmp))
        return

    for i in range(idx,c):
        path.append(arr[i])
        check(lv + 1, i+1, path)
        path.pop()


l, c = map(int,input().split())
arr = list(input().split())
final = []

check(0,0,[])

final.sort()

for fi in final:
    print(fi)