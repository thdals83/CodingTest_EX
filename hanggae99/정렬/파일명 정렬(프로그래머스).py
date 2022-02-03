#파일을 HEAD, NUM, TAIL 순으로 나누기

def solution(files):
    answer = []
    index= []

    for file in files:
        head, number, tail = "","",""
        check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                check = True

            elif not check:
                head += file[i]
            else:
                tail += file[i:]
                break

        index.append([head,number,tail])

    index.sort(key=lambda x:(x[0].lower(),int(x[1])))

    for i in index:
        answer.append(''.join(i))

    return answer

if __name__ == "__main__":
    arr = ["img12.png", "foo010bar020.zip	", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    arr2 = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
    print(solution(arr))
