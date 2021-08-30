def solution(c):
    arr=sorted(c,reverse=True)


    for i in range(len(arr)):
        if(i>=arr[i]):return i

    return len(arr)