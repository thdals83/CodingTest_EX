from collections import Counter

# Counter을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        count = Counter(stones)
        for word in jewels:
            res += int(count[word])
        return res


if __name__ == "__main__":
    x = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(x.numJewelsInStones(jewels,stones))