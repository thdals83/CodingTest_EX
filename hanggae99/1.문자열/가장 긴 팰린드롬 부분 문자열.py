from typing import List

'''
가장 쉬운방법은 문자열 1개 ~ len(s) 비교 해보기
=> 역순으로 가장 큰 문자열 부터 순차적으로 내려가면서 팬린드롬을 검사
=> 시간 효율이 어떨까 - 시간초과
def longestPalindrome(s: str) -> str:
    if len(s) == 1: return s
    # s = s.lower()

    for i in range(len(s)-1 , 0, -1):
        tmp = 0
        while i + tmp != len(s):

            use = s[tmp: tmp + i + 1]
            print(use)
            print(tmp,tmp + i + 1)
            if use == use[::-1]:
                return use
            tmp +=1
        print("")

    return s[0]
'''

def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(left+1, right)
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) == 1 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result

if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))