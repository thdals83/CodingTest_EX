
n = int(input())

dp = [1, 2, 4]
for i in range(3,10):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for _ in range(n):
    x = int(input())
    print(dp[x - 1])

'''

def check(lv, path):
    global res
    if len(path) != 0:
        if n == sum(path):
            #print(path)
            res += 1
            return

        if n < sum(path):
            return

    for num in arr:
        path.append(num)
        check(lv + 1, path)
        path.pop()


arr = [1, 2, 3]
t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    check(0,[])
    print(res)
'''