'''
문제를 풀기 위해선 조이스틱의 상하 값 + 좌우 값을 더해줘야 한다.

- 좌우 값 -
ord 사용법 ord 를 사용하게되면 해당 문자의 유니코드 값을 바꿔준다.
그 점을 이용해 처음 시작 A 알파벳에서 해당 알파벳 까지의 값을 숫자로 배열에 입력
- 상하 값 -
현재 가르키고 있는 인덱스 값 ing를 만들어서 ing에서 오른쪽으로 갔을 때 왼쪽으로 갔을 때
최소 거리의 값을 비교한다.
'''


def solution(name):
    res = 0
    arr=[]

    for i in name:
        arr.append(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1))

    ing = 0
    while True:
        res = res + arr[ing]
        arr[ing] = 0
        if sum(arr) == 0: break

        left,right = 1,1

        while arr[ing - left] == 0:
            left = left + 1
        while arr[ing + right] == 0:
            right = right + 1

        if left < right:
            res = res + left
        else:
            res = res + right

        if left < right:
            ing = ing - left
        else:
            ing = ing + right

    return res

if __name__ == "__main__":
    n = "JEROEN"
    print(solution(n))