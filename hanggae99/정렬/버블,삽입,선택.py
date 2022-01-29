

def bubblesort(nums):

    for num in range(len(nums) - 1):
        for cur in range(len(nums) -1 -num):
            if nums[cur] > nums[cur + 1]:
                nums[cur],nums[cur + 1] = nums[cur + 1], nums[cur]

    return nums


def selectesort(nums):

    for num in range(len(nums)):
        minindex  = num
        for j in range(num + 1, len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j

        if minindex != num:
            nums[num], nums[minindex] = nums[minindex], nums[num]

    return nums


def insertesort(nums):

    for n in range(1, len(nums)):
        for j in range(n, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

    return nums


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(insertesort(nums))

