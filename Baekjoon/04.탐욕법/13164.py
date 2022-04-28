'''
N명의 원생 키 순 정렬
총 K개의 조 => 적어도 원생이 한명 이상, 같은 조 원생들 서로 인접
조별 != 인원수

조마다 티셔츠 맞추는 비용 = 가장 큰애 - 가장 작은애
티셔츠 비용 합 최소로
'''

n, k = map(int,input().split())
arr = list(map(int,input().split()))

costs = []
for i in range(n -1):
    costs.append(arr[i+1] - arr[i])

costs.sort()

res = 0
for i in range(n - k):
    res += costs[i]
print(res)