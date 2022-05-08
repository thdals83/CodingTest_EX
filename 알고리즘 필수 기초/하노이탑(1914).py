'''
하노이탑

하노이탑 (O(2^n)
개수 ( 2^n - 1)
1개일 때 - 1개
2개일 때 - 3개
3개일 때 - 7개
'''


def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end, sep=" ")
    else:
        # n - 1개를 잠시 b로 옮겨준다.
        hanoi(n - 1, start, end, mid)
        # start에 남은 1개를 c로 옮겨준다.
        hanoi(1, start, mid, end)
        # b로 이동 시켜 준 n  1개를 c로 이동 시켜 준다.
        hanoi(n - 1, mid, start, end)

n = int(input())

print(2 ** n - 1)
# 20 이하일 때
if n <= 20:
    hanoi(n, 1, 2, 3)
