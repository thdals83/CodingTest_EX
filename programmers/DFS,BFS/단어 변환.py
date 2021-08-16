'''
1. 찾는 단어가 없는 경우 예외처리

현재 단어 리스트: word_list
word_list에 단어를 담고 해당 단어에서
변환이 될 수 있는 단어들을 diff_list에 담는다. (words 리스트에선 삭제)
diff_list랑 비교해서 target나오면 끝
안나오면 diff_list 값을 word_list로 담아준다
'''
def solution(begin, target, words):
    if target not in words: return 0

    answer = 0
    word_len = len(begin)
    word_list = [begin]
    diff_word = list()

    while True:
        for wl in word_list:
            diff_word.clear()
            for word in words:
                diff = 0
                for idx in range(0, word_len):
                    if wl[idx] != word[idx]: diff = diff + 1
                    if diff > 1: break
                if diff == 1:  # 1글자 차이
                    diff_word.append(word)
                    words.remove(word)

        answer = answer + 1

        if target in diff_word: return answer
        else: word_list = diff_word


if __name__ == "__main__":
    b = "hit"
    t = "cog"
    w = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(b,t,w))