def solution(dirs):
    answer = 0
    visited = []
    ing = [0,0]

    for dir in dirs:
        if dir == "U":
            if ing[1] + 1 < 6:
                back = [ing[0], ing[1], ing[0], ing[1] + 1]
                back2 = [ing[0], ing[1] + 1, ing[0], ing[1]]
                ing[1] += 1

                if (back and back2) not in visited:
                    answer += 1
                    visited.append(back)
                    visited.append(back2)

        elif dir == "D":
            if -6 < ing[1] - 1:
                #print("d", end = " ")
                back = [ing[0], ing[1], ing[0], ing[1] - 1]
                back2 = [ing[0], ing[1] - 1, ing[0], ing[1]]
                ing[1] -= 1

                if (back and back2) not in visited:
                    answer += 1
                    visited.append(back)
                    visited.append(back2)

        elif dir == "R":
            if ing[0] + 1 < 6:
                back = [ing[0], ing[1], ing[0] + 1, ing[1]]
                back2 = [ing[0] + 1, ing[1], ing[0], ing[1]]
                ing[0] += 1

                if (back and back2) not in visited:
                    answer += 1
                    visited.append(back)
                    visited.append(back2)

        elif dir == "L":
            if -6 < ing[0] - 1:

                back = [ing[0], ing[1], ing[0] - 1, ing[1]]
                back2 = [ing[0] - 1, ing[1], ing[0], ing[1]]
                ing[0] -= 1

                if (back and back2) not in visited:
                    answer += 1
                    visited.append(back)
                    visited.append(back2)
    print(visited)
    return answer

if __name__ == "__main__":
    d = "ULURRDLLU"
    d2 = "LLLLRLRLRLL"
    print(solution(d))