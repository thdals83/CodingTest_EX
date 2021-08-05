def solution(people,lim):
    people.sort()
    res, i = 0,0
    j = len(people) -1
    while i<=j:
        res=res+1
        if people[j]+people[i]<=lim:
            i=i+1
        j=j-1

    return res


if __name__ == "__main__":
    p = [70, 50, 80, 50]
    l = 100
    print(solution(p,l))