
'''
버블 정렬 O(N^2)
for문을 두번 돌려주면서, 인접한 두 원소를 비교해 정렬
'''
def bubblesort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


'''
선택 정렬 O(N^2)
가장 작은 수를 선택해 앞에서 부터 순차적으로 바꿔주는 것
'''
def selectesort(nums):
    for i in range(len(nums) - 1):
        tmp = i
        for j in range(i + 1, len(nums)):
            if nums[tmp] > nums[j]:
                tmp = j

        if tmp != i:
            nums[i], nums[tmp] = nums[tmp], nums[i]

    return nums

'''
삽입 정렬 O(N^2)
순차적으로 두번째 수부터, 원소를 골라 앞에서 부터 비교해서 삽입하는 형식
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

