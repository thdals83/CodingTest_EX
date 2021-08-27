import heapq

def solution(jobs):
    answer = len(jobs)
    res = 0
    time = 0

    jobs = sorted(jobs, key = lambda x:x[1])
    while len(jobs) != 0:

        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                res += time - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                time += 1

    return res//answer

if __name__ =="__main__":
    j = [[0, 3], [1, 9], [2, 6]]
    print(solution(j))