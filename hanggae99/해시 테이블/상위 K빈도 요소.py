from typing import List
from collections import Counter
# Counter을 이용한 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        x = Counter(nums).most_common(k)
        for i in x:
            res.append(i[0])

        return res


if __name__ == "__main__":
    x = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(x.topKFrequent(nums,k))