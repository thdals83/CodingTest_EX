import sys
n,m=map(int,input().split())
card=list(map(int,input().split()))

res=0
max=0
for i in range(len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1,len(card)):
            res=card[i]+card[j]+card[k]
            if(res==m):
                print(res)
                sys.exit()
            if(res<m):
                if (res > max):
                    max = res

print(max)