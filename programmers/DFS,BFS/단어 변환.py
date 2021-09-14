'''
1. 찾는 단어가 없는 경우 예외처리

현재 단어 리스트: word_list
word_list에 단어를 담고 해당 단어에서
변환이 될 수 있는 단어들을 diff_list에 담는다. (words 리스트에선 삭제)
diff_list랑 비교해서 target나오면 끝
안나오면 diff_list 값을 word_list로 담아준다
'''
from collections import deque

def solution(begin, target, words):
    if target not in words: return 0

    arr = deque()
    arr.append([begin,0])
    while arr:
        word,num = arr.popleft()
        if target == word: return num

        num += 1
        for wo in words:
            check = 0
            for j in range(len(word)):
                if wo[j] != word[j]: check += 1
                if check > 1: break

            if check == 1:
                arr.append([wo, num])

        for i in arr:
            if i[0] in words:
                words.remove(i[0])


if __name__ == "__main__":
    b = "hit"
    t = "cog"
    w = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(b,t,w))