import sys
input = sys.stdin.readline

def check(res):
    res.sort()
    print(res)
    for i in range(len(res) - 1):
        if res[i] in res[i + 1][:len(res[i])]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input().strip())

    print(check(arr))