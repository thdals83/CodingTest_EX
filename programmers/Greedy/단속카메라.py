def solution(routes):
    res = 0
    routes.sort(key = lambda x:x[1])
    x = - 30000

    for route in routes:
        if x < route[0]:
            res = res + 1
            x = route[1]

    return res





if __name__ == "__main__":
    r = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(r))