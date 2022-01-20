from collections import deque

def solution(progresses,speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        res = 1
        progresse = progresses.popleft()
        speed = speeds.popleft()

        minu = (100 - progresse) //speed
        if minu * speed + progresse < 100: minu += 1

        while progresses:
            if progresses[0] + (speeds[0] * minu) >= 100:
                progresses.popleft()
                speeds.popleft()
                res += 1
            else:
                break

        answer.append(res)

    return answer

if __name__ =="__main__":
    p = [93, 30, 55]
    s= [1, 30, 5]
    p1=  [99, 99, 99, 99, 99]
    s1= [99, 99, 99, 99, 99]
    print(solution(p1,s1))