

def queicsort(array, start, end):
    if start >= end: return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]


    queicsort(array, start, right - 1)
    queicsort(array, right + 1, end)


if __name__  == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    queicsort(array, 0, len(array) -1)
    print(array)
