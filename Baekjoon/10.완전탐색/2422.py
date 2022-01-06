import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]
print(ice)
for _ in range(m):
    x, y = map(int, input().split())
    ice[x - 1][y - 1] = True
    ice[y - 1][x - 1] = True
print(ice)
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1

print(result)