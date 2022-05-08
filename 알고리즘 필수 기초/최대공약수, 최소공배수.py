x, y = map(int, input().split())

x1 = x
y1 = y

while y != 0:
    x = x % y
    x, y = y, x

# 최대 공약수
print(x)
# 최소 공배수
print(x1 * y1 // x)
