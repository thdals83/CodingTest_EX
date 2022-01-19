from collections import Counter
from collections import defaultdict
from collections import deque

# 내가 푼 풀이
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = defaultdict(int)
        start = deque()
        res = 0
        i = 0
        while i != len(s):
            if dict[s[i]] == 1:
                dict.pop(start.popleft())
            else:
                dict[s[i]] = 1
                start.append(s[i])
                res = max(res, len(dict))
                i += 1

        return res
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        res, start = 0, 0

        for index, char in enumerate(s):

            if char in dict and start <= dict[char]:
                start = dict[char] + 1
            else:
                res = max(res, index - start + 1)

            dict[char] = index

        return res


if __name__ == "__main__":
    x = Solution()
    s = "pwwkew"
    print(x.lengthOfLongestSubstring(s))