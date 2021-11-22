x = int(input())

if x == 0:
    print(0)
    exit(0)
arr = []
arr.append(0)
arr.append(1)

for i in range(2, x+1):
    arr.append(arr[i-2]+arr[i-1])

print(arr[-1])