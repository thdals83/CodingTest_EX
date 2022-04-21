'''
1. 123456까지의 소수를 다 구한다.
- 에라스토테네스 체 방식을 구현
'''
num = 246912
arr = [True] * (num + 1)
arr[0] = False
arr[1] = False

for i in range(2,num + 1):
    if arr[i]:
        j = 2

        while (i * j) <= num + 1:
            arr[i * j] = False
            j += 1

# TestCase Start
while True:
    x = int(input())
    if x == 0: break
    cnt = 0
    for i in range(x + 1, (2 * x) + 1):
        if arr[i]: cnt += 1

    print(cnt)