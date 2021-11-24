a = int(input())  # 학생수
t = int(input())  # 원하는 개수
want = int(input())  # 원하는 문자

n = 2  # 반복횟수
m = 0  # t개까지의 0 or 1의 개수
total = 0
student = [i for i in range(a)]
ppun = []

while m != t:
    ppun += [0, 1, 0, 1]
    for _ in range(n): ppun.append(0)
    for _ in range(n): ppun.append(1)

    if len(ppun) // 2 >= t:
        for i in range(len(ppun)):
            total += 1
            if ppun[i] == want:
                m += 1
                if m == t:
                    # print(total, m)
                    break

    else:
        n += 1

print(student[total % a - 1])
