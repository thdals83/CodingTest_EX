import sys
input = sys.stdin.readline

dic = {}
cnt = 0
while True:
    str = input().strip()
    if not str: break

    dic.setdefault(str, 0)
    dic[str] += 1
    cnt += 1

arr = sorted(dic.keys())
for i in arr:
    print("%s %.4f" % (i, dic[i]*100/cnt))
