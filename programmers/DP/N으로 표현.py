'''
def solution(n,number):
    arr = [set() for i in range(8)]

    for i in range(0,8):
        if int(str(n)*(i+1)) == number:
            return i+1
        arr[i].add(int(str(n)*(i+1)))

    for i in range(1,8):
        for op1 in arr[i-1]:
            print("현재수: " + str(op1) +" ")
            arr[i].add(op1 + n)
            arr[i].add(op1 * n)
            arr[i].add(op1 - n)
            arr[i].add(op1 // n)
        print(arr[i])
        if number in arr[i]: return i+1

    return -1
'''

def solution(n, number):
    arr = [set() for i in range(8)]
    for i in range(8):
        if int(str(n)*(i+1)) == number: return i+1
        arr[i].add(int(str(n)*(i+1)))

    for i in range(1,8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i-j-1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0: arr[i].add(op1 // op2)

        if number in arr[i]: return i+1
    return -1


if __name__ == "__main__":
    N = 5
    num = 12
    print(solution(N,num))
