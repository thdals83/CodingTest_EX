from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        res = [intervals[0]]
        idx = 0
        for s,e in intervals[1:]:
            if res[idx][1] >= e:
                continue
            if res[idx][1] >= s:
                res[idx][1] = e
            else:
                res.append([s,e])
                idx += 1

        return res

if __name__  == "__main__":
    x = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(x.merge(intervals))
