from collections import defaultdict

n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = defaultdict(list)

res = 0
start = 0
for i in range(len(arr)):
    count[arr[i]].append(i)

    if len(count[arr[i]]) > k:
        res = max(res, i - start)
        start = (count[arr[i]].pop(0) + 1)

    # print(count)
    # print(arr[i], len(count[arr[i]]))
res = max(res, n - start)
print(res)

'''
N, K = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0

counter = [0] * (max(numbers) + 1)
answer = 0
while right < N:
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        right += 1
    else:
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
'''