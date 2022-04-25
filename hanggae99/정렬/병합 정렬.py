'''
병합정렬 두개가 남을때까지 쪼개고 이를 계쏙 합치면서 정렬 O(NlogN)
'''
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))

if __name__  == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    print(mergesort(array))