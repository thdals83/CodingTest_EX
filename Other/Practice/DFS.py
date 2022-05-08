'''
- 좌석에 앉거나, 떠나려고 함
- 좌석 개수 무한
- 사람은 id로 구분

좌석에 앉는 규칙
- 각 사람은 자신의 왼쪽과 오른쪽 빈 좌석이 k개씩 있는 좌석 앉는다
- 나중에 앉은 사람은 그 사람이 원했던 빈 좌석의 개수 고려해서 앉기
-
'''

def solution(records):
    answer = []
    train = []
    for record in records:
        arr = record.split(" ")

        if arr[1] == "sit":
            id = int(arr[0][3])
            k = int(arr[2][2])
            if len(train) == 0:
                train.append([k, id, k])
                continue

            #맨 앞에 들어갈 때
            if k + k <= train[0][0] - train[0][2]:
                train.append([k, id, k])
                continue

            last = True
            #사이에 들어갈 때
            for i in range(len(train) - 1):
                #앞에 값
                if train[i][2] <= k:
                    #뒤에값 사이 될 때
                    if train[i][0] + k + 1 + k <= train[i+1][0] - train[i + 1][2]:
                        last = False
                        train.append([train[i][0] + k + 1, id, k])
                        break
                else:
                    if train[i][0] + train[i][2] + 1 + k <= train[i+1][0] - train[i + 1][2]:
                        last = False
                        train.append([train[i][0] + train[-1][2] + 1, id, k])
                        break

            #마지막에 들어갈 때
            if last:
                if train[-1][2] <= k:
                    train.append([train[-1][0] + k + 1, id, k])
                else:
                    train.append([train[-1][0] + train[-1][2] + 1, id, k])

        # 좌석 뺄 때
        else:
            for i in range(len(train)):
                if train[i][1] == int(arr[0][3]):
                    train.pop(i)
                    break
        train.sort()

    train = sorted(train, key=lambda x:x[1])
    for i in train:
        answer.append([i[1],i[0]])
    return answer


if __name__ == "__main__":
    record = ["id=1 sit k=1","id=2 sit k=3","id=1 leave","id=3 sit k=1"]
    print(solution(record))
