

def solution(tickets):
    routes = dict()

    for (s,e) in tickets:
        routes[s] = routes.get(s,[]) + [e]

    # 2. 시작점 끝점 역순정렬
    for i in routes.keys():
        routes[i].sort(reverse = True)

    #DFS 알고리즘
    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]


    answer = path[::-1]
    return answer





if __name__ == "__main__":
    t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(t))
