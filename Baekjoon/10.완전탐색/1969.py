from collections import defaultdict
n,m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(input())

res = ""
cnt = 0
for i in range(m):
    tmp  = defaultdict(int)
    for j in range(n):
        tmp[arr[j][i]] += 1
        #print(arr[j][i], end = " ")
    tmp = sorted(tmp.items(), key=lambda x: x[0])
    tmp = sorted(tmp ,key = lambda x:x[1], reverse= True)
    for i in range(1,len(tmp)):
        cnt += tmp[i][1]
    res += tmp[0][0]
print(res)
print(cnt)