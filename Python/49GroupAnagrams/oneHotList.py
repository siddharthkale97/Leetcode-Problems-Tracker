from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord("a")] += 1
            # print(count)
            # print(tuple(count))
            res[tuple(count)].append(x) 
        return res.values()