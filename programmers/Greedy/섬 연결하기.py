
'''
Kruskal 알고리즘 사용 하지만 정석대로 사용하진 않은 방법
이 방법은 오름차순으로 정리 한것 까진 같지만, 그 뒤 노드를 이어지는 것들 순으로
삽입하는방법, 그리고 두 노드가 있을 경우 패스

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    conn = [costs[0][0]]
    while len(conn) != n:
        for i, cost in enumerate(costs):
            if cost[0] in conn and cost[1] in conn:continue
            if cost[0] in conn or cost[1] in conn:
                answer = answer + cost[2]
                conn.append(cost[0])
                conn.append(cost[1])
                conn = list(set(conn))
                costs.pop(i)
                break
    return answer
'''
'''
크루스칼 알고리즘 정석
1. 간선의 길이가 짧은 순으로 정렬
2. 간선을 선택 하며 => 사이클이 발생하지 않는지 확인 (union find 기법)
3. union find 기법 => 추가하려는 간선의 양 끝점이 같은 집합에 있지 않아야 함
'''

def solution(n, costs):
    answer = 0

    #특정 원소가 속한 집합을 찾기기
    def find_parent(x):
        # 루트가 아니라면 찾을 때 까지 재귀 호출
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(a,b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 부모 테이블
    parent = [0] * n
    # 부모 테이블 자기 자신으로 초기화
    for i in range(n): parent[i] = i

    #스루스칼 알고리즘 비용순 정렬
    costs.sort(key = lambda x:x[2])
    print(costs)
    #크루스칼 알고리즘 수행
    #간선을 하나씩 확인
    for edge in costs:
        a, b, cost = edge
        if find_parent(a) !=find_parent(b):
            union_parent(a,b)
            answer += cost
        # 사이클이 발생하지 않는 경우에만 집합에 포함한다.
    return answer





if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n,costs))