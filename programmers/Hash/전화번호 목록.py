
# 문자열의 정렬이기 때문에 숫자의 크기가 아닌 1부터 순차적으로 정렬됨
# 그걸 이용해서 정렬후 첫번째와 두번째만 숫자를 올려가며 비교해주면 됨
# zip 은 두 값을 한번에 사용할 수 있는 용도
def solution(phone_book):
    phone_book.sort()

    for x,y in zip(phone_book,phone_book[1:]):
        if y.startswith(x):
            return False
    return True



if __name__ == "__main__":
    p=["12","123","1235","567","88"]
    print(solution((p)))