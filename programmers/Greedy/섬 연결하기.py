'''
크루스칼 알고리즘 정석
'''
def solution(n, costs):
    answer = 0

    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트가 아니라면 찾을 때까지 재귀 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 찾기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 부모 테이블
    parent = [0] * n
    # 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i

    # 크루스칼 알고리즘을 위해 비용순으로 정렬
    costs = sorted(costs, key=lambda x: x[2])

    # 크루스칼 알고리즘 수행
    # 간선을 하나씩 확인하며
    for edge in costs:
        a, b, cost = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer


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


if __name__ == "__main__":
    n = 7
    costs = [[0,5,10],[3,4,22],[1,6,15],[1,2,16],[2,3,12],[3,6,18],[4,5,27],[4,6,25],[0,1,29]]
    print(solution(n,costs))