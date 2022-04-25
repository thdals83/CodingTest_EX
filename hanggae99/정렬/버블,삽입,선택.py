
'''
버블 정렬 O(N^2)
버블 정렬은 앞에 수와 뒤의 수를 비교해 정렬해 주는 것입니다.
'''
def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

'''
선택 정렬 O(N^2)
전체 배열에서 가장 작은 수를 선택해 앞에서 부터 차례대로 바꿔 줍니다.
'''
def selectesort(nums):
    for i in range(len(nums)):
        tmp = i
        for j in range(i + 1, len(nums)):
            if nums[tmp] > nums[j]:
                tmp = j
        if tmp != i:
            nums[i], nums[tmp] = nums[tmp], nums[i]
    return nums

'''
삽입 정렬 O(N^2)
두번째 수 부터 차례로 수를 골라 앞에서 비교하면서 적절하 위치에 삽입해 주는 것입니다.
'''
def insertesort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(insertesort(nums))

