
def pra(arr, n):
    res = []
    use = arr
    stack = []

    for i in use:
        stack.append(i)

    while stack:
        path = stack.pop()

        for i in use:
            temp = path + i

            if len(temp) == n:
                element = []
                res.append(temp)
            else:
                stack.append(temp)
        print(stack)
    return res



a = ['A','B','C']
print(pra(a,3))