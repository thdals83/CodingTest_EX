'''
퀵정렬 평균: O(NlogN)
최악: O(N^2) => 만약 정렬이 되어 있는 배열에 경우 피벗이 효율적이게 작동하지 않는다
사용법
피벗을 중심으로 오름차순을 한다고 가정할때, 왼쪽은 피벗보다 값이 큰값, 오른쪽은 피벗보다 값이 작은 값을 선택해
위치를 바꿔준다. 만약 왼쪽과 오른쪽이 서로 크로스 되게 되면 작은 값과 피벗을 바꿔주고
이 과정을 재귀로 반복해서 돌게 된다.
'''
def queicsort(arr, start, end):
    if start >= end: return
    pivot = start
    left = start + 1
    right = end

    #엇갈리기 전까지
    while left < right:
        # left 수 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # right 수 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    queicsort(arr,start, right - 1)
    queicsort(arr, right + 1, end)



if __name__  == "__main__":
    arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    queicsort(arr, 0, len(arr) - 1)
    print(arr)