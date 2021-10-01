
if __name__ == "__main__":
    x,y = map(int,input().split())
    arr = []
    res = []
    for i in range(1, x+1):
        arr.append(i)
    num = 0


    while arr:
        num += + y - 1
        if num > len(arr) -1:
            num = num % len(arr)

        res.append(str(arr.pop(num)))

    print("<", ", ".join(res)[:], ">", sep='')

