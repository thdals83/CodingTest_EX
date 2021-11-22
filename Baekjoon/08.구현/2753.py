#연도가 4의 배수, 100의 배수가 아닌 것또는 400의 배수

x = int(input())

if x % 4 == 0:
    if x % 100 != 0 or x % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)