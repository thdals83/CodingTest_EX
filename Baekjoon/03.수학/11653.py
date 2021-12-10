import sys

x = int(sys.stdin.readline())
i = 2
while x != 1:
    if x % i == 0:
        x /= i
        print(i)

    else:
        i += 1