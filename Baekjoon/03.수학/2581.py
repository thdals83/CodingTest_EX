m = int(input())
n = int(input())

arr = [0]*(n+1)
arr[0] = 1
arr[1] = 1
for i in range(2, n + 1):
    if arr[i]== 0:
        for j in range(i,  n + 1, i):
            if i != j:
                arr[j] = 1

res = 0
check = False
for i in range(m,n + 1):
    if arr[i] == 0:
        res += i
        if not check: minnum = i

        check = True


if not check:
    print(-1)
else:
    print(res)
    print(minnum)



#수 올려가며 그 배수 다 지우기 이게 베스트