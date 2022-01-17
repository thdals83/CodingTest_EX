from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    arr = defaultdict(list)

    for word in strs:
        print(sorted(word))
        arr[''.join(sorted(word))].append(word)

    print(arr)
    return list(arr.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))