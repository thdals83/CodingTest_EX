# zip 과 startswith를 이용한 풀이 방법
# zip은 두 배열 의 값을 순서대로 매칭시킴 말 그대로 zip
'''
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
'''
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


if __name__ == "__main__":
    p=["12","123","1235","567","88"]
    print(solution((p)))