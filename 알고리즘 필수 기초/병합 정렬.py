'''
병합정렬 두개가 남을때까지 쪼개고 이를 계쏙 합치면서 정렬 O(NlogN)
'''

def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1

    return res

def mergesort(lst):
    if len(lst) <= 1: return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


if __name__  == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    print(mergesort(array))