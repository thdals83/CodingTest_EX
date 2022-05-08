
n = int(input())
arr = list(map(int,input().split()))

sosu = [1] * (max(arr) + 1)
sosu[1] = 0
# 소수 체크

for i in range(2, len(sosu)):
    if sosu[i] == 1:
        j = 2

        while i * j <= len(sosu) - 1:
            sosu[i * j] = 0
            j += 1

res = 0
for i in arr:
    if sosu[i] == 1:
       res += 1

print(res)