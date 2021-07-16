'''
def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            print("check1")
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer
'''
import collections


def solution(participant, completion):
    print(collections.Counter(participant)),print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]

#collection.Counter(배열) => dic 값 형태로 해당 이름의 개수를 세준다.


if __name__ =="__main__":
    pa= ["mislav", "stanko", "mislav", "ana"]
    co= ["stanko", "ana", "mislav"]
    pa1=["marina", "josipa", "nikola", "vinko", "filipa"]
    co1=["josipa", "filipa", "marina", "nikola"]
    print(solution(pa,co))