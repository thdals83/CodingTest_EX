x = int(input())

check = 1
for i in range(1, x):
    tmp = str(i)
    res = i
    for j in range(len(tmp)):
        res += int(tmp[j])

    if res == x:
        check = 0
        break

if check == 0: print(tmp)
else: print(0)
