'''
버블 정렬 O(N^2)
이중 반복문을 돌면서 앞 뒤 수를 비교해 정렬해줍니다.
'''
def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

'''
선택 정렬 O(N^2)
전체 배열에서 가장 작은 수를 선택해 순차적으로 맨 앞으로 옮겨 줍니다.
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
첫번째 수는 정렬이 되었다고 가정하고, 두번째 수부터 앞에 수들과 비교를 해가며, 적절한 위치에 삽입해 줍니다.
'''
def insertesort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                break
    return nums


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(insertesort(nums))
