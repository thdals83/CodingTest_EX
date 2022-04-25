'''
퀵정렬 평균: O(NlogN),
최악: O(N^2) => 이미 정렬된 배열에 대해서는 효과가 좋지 않다.
피벗값을 기준으로 큰 데이터와 작은 데이터의 위치를 바꾸다가 위치가 엇갈리는 경우
피벗값의 위치와 변경 시켜주고 피벗값을 기준으로 재귀가 돌면서 계속 이를 반복해준다.
'''
def queicsort(array, start, end):
    if start >= end: return
    pivot = start
    left = start + 1
    right = end

    while left < right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    queicsort(array,start,right - 1)
    queicsort(array,right + 1, end)



if __name__  == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    queicsort(array, 0, len(array) -1)
    print(array)